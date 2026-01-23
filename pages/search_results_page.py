from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResultsPage(Page):
    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[contains(@class,'styles_listingPageResultsCount')]")
    FAV_ICON = (By.CSS_SELECTOR, '[data-test="FavoritesButton"]')
    FAV_TOOLTIP = (By.XPATH, "//*[text()='Click to sign in and save']")

    def hover_fav_icon(self):
        self.hover_element(*self.FAV_ICON)

    def verify_search_results(self, expected_product):
        self.verify_partial_text(expected_product, *self.SEARCH_RESULTS_TEXT)

    def verify_fav_tooltip(self):
        self.find_element(*self.FAV_TOOLTIP)