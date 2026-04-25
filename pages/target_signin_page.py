from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TargetSignInPage(BasePage):
    """target.com sign-in page — the chooser heading and the sign-in form
    (email, password, login button)."""

    # Some variants show a "Sign in or create account" heading before the
    # form fields render, so check for either one.
    CHOOSER_HEADER = (By.XPATH, '//h1[contains(text(),"Sign in or create account")]')

    EMAIL_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    SIGN_IN_BTN = (By.ID, "login")

    def is_chooser_displayed(self):
        return self.is_visible(self.CHOOSER_HEADER)

    def is_form_loaded(self):
        return self.is_visible(self.EMAIL_FIELD) and self.is_visible(self.SIGN_IN_BTN)
