from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class TargetSignInPage(BasePage):
    """target.com sign-in page — the chooser heading, the email/password
    form, and a check that the form has gone away after a successful login."""

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

    def enter_email(self, email):
        self.input_text(self.EMAIL_FIELD, email)

    def enter_password(self, password):
        self.input_text(self.PASSWORD_FIELD, password)

    def click_sign_in(self):
        self.click(self.SIGN_IN_BTN)

    def is_signed_in(self, timeout=15):
        # After a successful login, target navigates away from the sign-in
        # page so the email field is no longer visible. Wait until that's
        # the case; treat a timeout as login failure.
        try:
            WebDriverWait(self.driver, timeout).until_not(
                EC.visibility_of_element_located(self.EMAIL_FIELD)
            )
            return True
        except TimeoutException:
            return False
