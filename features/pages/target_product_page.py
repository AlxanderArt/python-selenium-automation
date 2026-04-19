from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class TargetProductPage(BasePage):
    """A Target product detail page — the Add to cart button and the
    Choose options button that appears for products with variants."""

    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[data-test="addToCartButton"]')
    # Fallback button that Target sometimes uses for pickup-eligible items;
    # it also says "Add to cart" and actually adds the item.
    ORDER_PICKUP_BTN = (By.CSS_SELECTOR, '[data-test="orderPickupButton"]')
    # If this shows up, the product needs a variant (color/size) selected
    # before it can be added. The test picks a product where this isn't
    # expected, but the locator is here so we can detect and fail loudly.
    CHOOSE_OPTIONS_BTN = (By.CSS_SELECTOR, '[data-test="chooseOptionsButton"]')

    def add_to_cart(self):
        # Target sometimes overlays the Add to cart button with a shipping /
        # fulfillment prompt, so scrolling the button into view and falling
        # back to a JS click if a normal click gets intercepted avoids flaky
        # ElementClickInterceptedException errors.
        for locator in (self.ADD_TO_CART_BTN, self.ORDER_PICKUP_BTN):
            if self.is_visible(locator):
                self._safe_click(locator)
                return
        if self.is_visible(self.CHOOSE_OPTIONS_BTN):
            raise AssertionError(
                "This product needs variant selection (Choose options). "
                "Pick a different search term for the add-to-cart test."
            )
        raise AssertionError("Could not find any Add to cart button on the product page")

    def _safe_click(self, locator):
        el = self.find_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
        try:
            self.click(locator)
        except ElementClickInterceptedException:
            self.log.info("Normal click intercepted, falling back to JS click")
            self.driver.execute_script("arguments[0].click();", el)
