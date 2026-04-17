from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class TargetCartPage(BasePage):
    """Cart icon on the Target header and the empty-cart message on /cart."""

    URL = "https://www.target.com/cart"

    CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartLink"]')
    EMPTY_CART_MSG = (By.XPATH, '//*[contains(text(), "Your cart is empty")]')

    def open_cart(self):
        self.click(self.CART_ICON)

    def is_cart_empty(self):
        return self.is_visible(self.EMPTY_CART_MSG)
