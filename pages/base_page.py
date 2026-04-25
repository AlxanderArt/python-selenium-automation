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
