import logging
import os
import re
import shutil
import ssl
import subprocess
import tempfile
from datetime import datetime

import certifi

# macOS Python installs don't see the system keychain by default, which
# breaks undetected-chromedriver when it fetches its patched chromedriver.
# Point Python's SSL layer at certifi's bundle before uc imports do any
# network work.
os.environ.setdefault("SSL_CERT_FILE", certifi.where())
ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())

import undetected_chromedriver as uc

from app.application import Application


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("behave")

SCREENSHOT_DIR = "screenshots"

# Shared Chrome profile used only by scenarios that need cookies to persist
# between runs — for example, StackOverflow signup, which sits behind a
# Cloudflare challenge. Scenarios opt in by adding the @persistent_profile
# tag in their .feature file. Every other scenario gets a fresh throwaway
# profile so cart state, logins, and dismissed banners don't leak between
# tests.
AUTOMATION_PROFILE_DIR = os.path.expanduser("~/.chrome-automation-profile")


CHROME_BINARY = "/Users/alxanderart/Desktop/Google Chrome.app/Contents/MacOS/Google Chrome"


def _detect_chrome_major_version():
    # Ask the Chrome binary for its version and pull the major. Without this
    # undetected-chromedriver downloads the latest stable chromedriver, which
    # fails with "session not created" whenever the installed Chrome is one
    # release behind. Returning None lets uc fall back to its default
    # behavior so this never breaks the environment if the binary moves.
    try:
        out = subprocess.check_output(
            [CHROME_BINARY, "--version"], stderr=subprocess.STDOUT, timeout=5
        ).decode("utf-8", errors="ignore")
    except Exception:
        return None
    match = re.search(r"(\d+)\.\d+\.\d+\.\d+", out)
    return int(match.group(1)) if match else None


def browser_init(context):
    # undetected-chromedriver handles the anti-bot flags on its own (patches
    # chromedriver and drops navigator.webdriver, among other things), so
    # the usual --disable-blink-features / excludeSwitches lines are gone.
    # With uc, Cloudflare's "verify you are human" check clears on its own
    # without a manual click.
    options = uc.ChromeOptions()

    if "persistent_profile" in (context.scenario.tags or []):
        os.makedirs(AUTOMATION_PROFILE_DIR, exist_ok=True)
        profile_dir = AUTOMATION_PROFILE_DIR
        context._temp_profile = None
    else:
        profile_dir = tempfile.mkdtemp(prefix="chrome-test-profile-")
        context._temp_profile = profile_dir
    options.add_argument(f"--user-data-dir={profile_dir}")
    options.add_argument("--window-size=1920,1080")

    if os.environ.get("HEADLESS") == "1":
        options.add_argument("--headless=new")

    context.driver = uc.Chrome(
        options=options,
        browser_executable_path=CHROME_BINARY,
        use_subprocess=True,
        version_main=_detect_chrome_major_version(),
    )
    context.driver.implicitly_wait(4)


def before_scenario(context, scenario):
    log.info("Scenario START: %s", scenario.name)
    browser_init(context)
    # Wire every page object up front so step files can reach them through a
    # single context.app namespace instead of new-ing pages one at a time.
    context.app = Application(context.driver)


def before_step(context, step):
    log.info("  Step: %s", step)


def after_step(context, step):
    if step.status == "failed":
        log.warning("  Step FAILED: %s", step)
        _save_screenshot(context, step.name)


def after_scenario(context, scenario):
    log.info("Scenario END: %s (%s)", scenario.name, scenario.status)
    if getattr(context, "driver", None):
        context.driver.quit()
    # Clean up any throwaway per-scenario profile so disk doesn't fill up.
    temp_profile = getattr(context, "_temp_profile", None)
    if temp_profile and os.path.isdir(temp_profile):
        shutil.rmtree(temp_profile, ignore_errors=True)


def _save_screenshot(context, step_name):
    drv = getattr(context, "driver", None)
    if not drv:
        return
    try:
        os.makedirs(SCREENSHOT_DIR, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe = "".join(c if c.isalnum() else "_" for c in step_name)[:60]
        path = os.path.join(SCREENSHOT_DIR, f"{ts}_{safe}.png")
        drv.save_screenshot(path)
        log.warning("Screenshot saved: %s", path)
    except Exception as e:
        log.error("Screenshot failed: %s", e)
