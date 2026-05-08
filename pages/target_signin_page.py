from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class TargetSignInPage(BasePage):
    """target.com sign-in page — the chooser heading, the email/password
    form, and a check that the form has gone away after a successful login."""

    # Hitting /orders without a session redirects to the sign-in page.
    # Using /orders is what the HW8 assignment specifies for opening
    # sign-in directly.
    URL = "https://www.target.com/orders?lnk=acct_nav_my_account"

    # Some variants show a "Sign in or create account" heading before the
    # form fields render, so check for either one.
    CHOOSER_HEADER = (By.XPATH, '//h1[contains(text(),"Sign in or create account")]')

    EMAIL_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    SIGN_IN_BTN = (By.ID, "login")

    # Target reuses the same id ("login") for the Continue button on
    # the email step and the Sign in with password button on the
    # password step. Wait helpers below disambiguate by form state.
    LOGIN_BUTTON = (By.ID, "login")

    # Inline error shown when the password is wrong. Target has changed
    # the data-test value before, so the case-insensitive text fallback
    # picks up "incorrect" or "doesn't match" wording either way.
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='accountSignInError']")
    ERROR_MESSAGE_FALLBACK = (
        By.XPATH,
        "//*[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "
        "'abcdefghijklmnopqrstuvwxyz'), 'incorrect') "
        "or contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "
        "'abcdefghijklmnopqrstuvwxyz'), \"doesn't match\")]",
    )

    # The Target terms and conditions link in the legal footer. Target
    # tags its legal links with aria-label (Lana's lesson 8 uses the
    # same pattern for the privacy policy link), which is more stable
    # than visible text or href across page redesigns.
    TERMS_LINK = (By.CSS_SELECTOR, "a[aria-label*='terms']")

    def open_signin_page(self):
        # Direct navigation to /orders triggers a redirect chain into
        # the sign-in flow, and undetected-chromedriver may briefly
        # detach the active tab while it clears the bot challenge.
        # Wait for document.readyState to settle so the next step sees
        # a live window handle, then wait for the Terms link to render.
        self.open(self.URL)
        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        self.is_present(self.TERMS_LINK)

    def click_terms_link(self):
        self.click(self.TERMS_LINK)

    def wait_for_email_step(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.EMAIL_FIELD)
        )

    def wait_for_password_step(self):
        # The button id stays "login" across both steps, so visibility
        # of the password field is the only reliable signal that
        # Target's two-step form has actually advanced.
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.PASSWORD_FIELD)
        )

    def click_continue(self):
        self.wait_for_email_step()
        self.click(self.LOGIN_BUTTON)

    def click_sign_in_with_password(self):
        self.wait_for_password_step()
        self.click(self.LOGIN_BUTTON)

    def get_error_element(self):
        # Try the data-test selector first; fall back to the
        # case-insensitive text match if Target tweaks the attribute.
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            )
        except TimeoutException:
            return WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE_FALLBACK)
            )

    def verify_sign_in_error(self):
        el = self.get_error_element()
        text = (el.text or "").lower()
        assert "incorrect" in text or "doesn't match" in text, (
            f"Sign-in error text didn't match expected wording: {text!r}"
        )
        url = self.driver.current_url.lower()
        assert "login" in url or "sign-in" in url or "/orders" in url, (
            f"Expected to still be on sign-in flow, got url={url!r}"
        )

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
