from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class TargetCirclePage(BasePage):
    """target.com/circle — specifically the 'Unlock added value' section and
    its storycards."""

    URL = "https://www.target.com/circle"

    # The Storyblocks section whose heading is "Unlock added value". Anchoring
    # on the heading text is more stable than hardcoding an index.
    UNLOCK_SECTION = (
        By.XPATH,
        '//*[@data-test="@web/SlingshotComponents/Storyblocks"]'
        '[.//h2[contains(text(),"Unlock added value")]]',
    )

    # Storycards within a Storyblocks section. Scoped by using find_elements
    # on the section element, not the whole driver.
    STORYCARDS_IN_SECTION = (
        By.CSS_SELECTOR,
        '[data-test="@web/SlingshotComponents/common/Storycard"]',
    )

    def load(self):
        self.open(self.URL)

    def count_unlock_storycards(self):
        section = self.find_element(self.UNLOCK_SECTION)
        return len(section.find_elements(*self.STORYCARDS_IN_SECTION))
