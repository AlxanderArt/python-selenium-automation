import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


DEFAULT_TIMEOUT = 10


class BasePage:
    """Base for page objects. Wraps WebDriverWait so each page can just list
    its locators and call self.click / self.is_visible without setting up
    waits every time."""

    def __init__(self, driver, timeout=DEFAULT_TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.log = logging.getLogger(self.__class__.__name__)

    def open(self, url):
        self.log.info("Navigating to %s", url)
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_element(self, locator):
        # Waits for the element to be in the DOM, then returns it — same as
        # self.find, but named to match Selenium's API so step files read nicely.
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        # Waits for at least one element to be present, then returns the whole
        # list. Good for counts (how many results / cards / items).
        self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.log.info("Clicking %s", locator)
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def input_text(self, locator, text):
        el = self.find_visible(locator)
        el.clear()
        el.send_keys(text)

    # Older code calls this `type`; keep both names so existing callers still work.
    type = input_text

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_present(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_until_url_contains(self, fragment, timeout=15):
        # Useful for verifying that a new tab landed on the right page
        # without depending on a specific element to render.
        WebDriverWait(self.driver, timeout).until(EC.url_contains(fragment))

    def get_current_window(self):
        return self.driver.current_window_handle

    def get_window_state(self):
        # Snapshot of the active handle plus every handle Selenium knows
        # about. Capture this *before* the click that opens a new window
        # so the post-click switch can pick the new handle by set diff.
        return {
            "handle": self.driver.current_window_handle,
            "handles_snapshot": list(self.driver.window_handles),
        }

    def switch_to_new_window(self, original_handles):
        # Wait until the click produces a brand-new handle (not just any
        # change), then switch to it. Set diff handles the rare case
        # where more than one tab opens — we still pick exactly one.
        self.wait.until(
            lambda d: len(d.window_handles) > len(original_handles)
        )
        new_handles = set(self.driver.window_handles) - set(original_handles)
        if not new_handles:
            raise RuntimeError("No new window detected after click")
        new_handle = new_handles.pop()
        self.driver.switch_to.window(new_handle)
        self.log.info(
            "All handles: %s; switched to new: %s",
            self.driver.window_handles, self.get_current_window()
        )

    def switch_to_window_by_id(self, window_id):
        # Fail loudly if the original handle is gone — this surfaces the
        # real cause (window closed too early) instead of letting
        # Selenium's NoSuchWindowException bubble up later.
        if window_id not in self.driver.window_handles:
            raise RuntimeError(
                f"Original window {window_id} no longer exists"
            )
        self.driver.switch_to.window(window_id)
        self.log.info("Switched back to: %s", self.get_current_window())

    def refresh_page(self):
        self.driver.refresh()

    def close_window(self):
        # Closes the active tab only — the driver itself stays alive so
        # the scenario can switch back to the original window.
        self.driver.close()
