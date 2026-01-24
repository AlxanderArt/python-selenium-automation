from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from pages.base_page import Page


class HelpPage(Page):
    RETURNS_HEADER = (By.XPATH, "//h1[text()=' Returns']")
    PROMOTIONS_HEADER = (By.XPATH, "//h1[text()=' Current promotions']")
    TARGET_CIRCLE = (By.XPATH, "//h1[text()=' About Target Circle']")
    TOPIC_HEADER = (By.XPATH, "//h1[text()=' {TOPIC_HEADER}']")
    SELECT_TOPIC_DD = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")

    # Dynamic locators
    def _get_header_topic_locator(self, topic):
        return [self.TOPIC_HEADER[0], self.TOPIC_HEADER[1].replace('{TOPIC_HEADER}', topic)]

    def open_help_returns(self):
        self.driver.get('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def select_topic(self, option_value):
        dd = self.find_element(*self.SELECT_TOPIC_DD)
        select = Select(dd)
        select.select_by_value(option_value)

    def verify_help_topic_opened(self, topic):
        locator = self._get_header_topic_locator(topic)
        self.wait_until_element_present(*locator)

    def verify_promotions_opened(self):
        self.wait_until_element_present(*self.PROMOTIONS_HEADER)

    def verify_returns_opened(self):
        self.wait_until_element_present(*self.RETURNS_HEADER)