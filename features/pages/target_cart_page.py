from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class TargetCartPage(BasePage):
    """Cart icon on the Target header, the empty-cart message on /cart, and
    the cart items / order total for when the cart has something in it."""

    URL = "https://www.target.com/cart"

    CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartLink"]')
    EMPTY_CART_MSG = (By.XPATH, '//*[contains(text(), "Your cart is empty")]')

    # Individual items in the cart — plural on purpose so find_elements can
    # count them.
    CART_ITEMS = (By.CSS_SELECTOR, '[data-test="cartItem"]')
    ORDER_TOTAL = (By.CSS_SELECTOR, '[data-test="cart-summary-total"]')

    def open_cart(self):
        self.click(self.CART_ICON)

    def is_cart_empty(self):
        return self.is_visible(self.EMPTY_CART_MSG)

    def item_count(self):
        return len(self.find_elements(self.CART_ITEMS))
