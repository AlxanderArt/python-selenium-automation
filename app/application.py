"""Application — single entry point that wires every page object to the
shared driver. Steps reach pages through context.app.<page>, so feature
files don't have to import page classes one by one or rebuild them every
scenario."""

from pages.amazon_signin_page import AmazonSignInPage
from pages.stackoverflow_signup_page import StackOverflowSignupPage
from pages.target_cart_page import TargetCartPage
from pages.target_circle_page import TargetCirclePage
from pages.target_color_picker_page import TargetColorPickerPage
from pages.target_home_page import TargetHomePage
from pages.target_product_page import TargetProductPage
from pages.target_search_page import TargetSearchPage
from pages.target_signin_page import TargetSignInPage


class Application:
    """Holds one instance of every page object, all sharing the same driver.
    Adding a new page means adding one line here and the steps can read it
    via context.app.<new_page>."""

    def __init__(self, driver):
        self.driver = driver

        # Target
        self.home_page = TargetHomePage(driver)
        self.search_page = TargetSearchPage(driver)
        self.product_page = TargetProductPage(driver)
        self.cart_page = TargetCartPage(driver)
        self.signin_page = TargetSignInPage(driver)
        self.circle_page = TargetCirclePage(driver)
        self.color_picker_page = TargetColorPickerPage(driver)

        # Amazon
        self.amazon_signin_page = AmazonSignInPage  # plain locator class, no driver needed

        # StackOverflow
        self.stackoverflow_signup_page = StackOverflowSignupPage(driver)
