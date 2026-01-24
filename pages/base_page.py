from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from support.logger import logger

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.driver.wait = WebDriverWait(driver, timeout=10)
        self.base_url = 'https://www.target.com'

    def open_url(self, end_url=''):
        logger.info(f'Opening URL: {self.base_url}{end_url}')
        self.driver.get(f'{self.base_url}{end_url}')

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, *locator):
        logger.info(f'Searching for element by {locator}')
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        logger.info(f'Searching for elements by {locator}')
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        logger.info(f'Clicking on element by {locator}')
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        logger.info(f'Inputting text {text} to {locator}')
        self.driver.find_element(*locator).send_keys(text)

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def switch_to_new_window(self):
        self.driver.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print('All windows: ', all_windows)
        print('Switching to window: ', all_windows[1])
        self.driver.switch_to.window(all_windows[1])

    def switch_to_window_by_id(self, window_id):
        print('Switching to window: ', window_id)
        self.driver.switch_to.window(window_id)

    def hover_element(self, *locator):
        element = self.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

    def wait_until_element_present(self, *locator):
        self.driver.wait.until(
            EC.presence_of_element_located(locator),
            message=f'Element not present by locator {locator}'
        )

    def wait_until_element_invisible(self, *locator):
        self.driver.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element still visible by locator {locator}'
        )

    def wait_until_clickable(self, *locator):
        self.driver.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable by locator {locator}'
        )

    def wait_until_clickable_click(self, *locator):
        self.driver.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable by locator {locator}'
        ).click()

    def wait_until_url_contains(self, expected_partial_url):
        self.driver.wait.until(
            EC.url_contains(expected_partial_url),
            message=f'Expected {expected_partial_url} not in {self.driver.current_url}.'
        )

    def close_page(self):
        self.driver.close()

    def verify_partial_text(self, expected_partial_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_partial_text in actual_text, \
            f"Expected {expected_partial_text} not in actual {actual_text}"

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, \
            f"Expected {expected_text}, but got actual {actual_text}"

    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        assert actual_url == expected_url, \
            f'Expected {expected_url}, but got {actual_url}'

    def verify_url_contains(self, expected_partial_url):
        actual_url = self.driver.current_url
        assert expected_partial_url in actual_url, \
            f'Expected {expected_partial_url} not in {actual_url}'