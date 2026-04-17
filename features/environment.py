import logging
import os
from datetime import datetime

from selenium import webdriver


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("behave")

SCREENSHOT_DIR = "screenshots"


def browser_init(context):
    options = webdriver.ChromeOptions()
    options.binary_location = "/Users/alxanderart/Desktop/Google Chrome.app/Contents/MacOS/Google Chrome"
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    if os.environ.get("HEADLESS") == "1":
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    context.driver = webdriver.Chrome(options=options)
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)


def before_scenario(context, scenario):
    log.info("Scenario START: %s", scenario.name)
    browser_init(context)


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
