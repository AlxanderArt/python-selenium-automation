from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from pages.base_page import BasePage


class TargetHelpPage(BasePage):
    """Target Help center — dropdown navigation between help topics.
    The page is a Salesforce Lightning component, which renders
    asynchronously, so the dropdown helpers wait for the <select>
    to be clickable before wrapping it in a Select()."""

    RETURNS_URL = (
        "https://help.target.com/help/SubCategoryArticle"
        "?childcat=Returns&parentcat=Returns+%26+Exchanges"
    )

    # Lightning generates a long id with a stable substring.
    DROPDOWN = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")

    HEADER_TEMPLATE = "//h1[contains(normalize-space(.), \"{}\")]"

    def open_returns_page(self):
        self.open(self.RETURNS_URL)

    def get_header_locator(self, expected_text):
        return (By.XPATH, self.HEADER_TEMPLATE.format(expected_text))

    def select_topic(self, topic):
        # Capture the URL before selection so we can assert the
        # dropdown actually triggered navigation, not just a UI swap.
        self._initial_url = self.driver.current_url
        dropdown = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.DROPDOWN)
        )
        Select(dropdown).select_by_visible_text(topic)

    def verify_header_and_url_changed(self, expected_text):
        # Two-part check: the H1 header reflects the new topic AND the
        # URL has changed since the dropdown selection. Either alone
        # could pass on a stale render.
        locator = self.get_header_locator(expected_text)
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(locator)
        )
        WebDriverWait(self.driver, 15).until(
            lambda d: d.current_url != getattr(self, "_initial_url", "")
        )
