from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TargetHomePage(BasePage):
    """target.com homepage header — the account button and the sign-in link
    that appears inside the right-side menu."""

    URL = "https://www.target.com/"

    # Top-right button that opens the account menu. Target shows "Account"
    # when logged in and "Sign in" when logged out, so match by data-test
    # instead of link text.
    HEADER_SIGN_IN = (By.CSS_SELECTOR, '[data-test="@web/AccountLink"]')

    # The Sign In button inside the right-side menu that opens after clicking
    # HEADER_SIGN_IN.
    SIDE_NAV_SIGN_IN = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')

    def load(self):
        self.open(self.URL)

    def open_account_menu(self):
        self.click(self.HEADER_SIGN_IN)

    def click_signin_from_side_menu(self):
        self.click(self.SIDE_NAV_SIGN_IN)
