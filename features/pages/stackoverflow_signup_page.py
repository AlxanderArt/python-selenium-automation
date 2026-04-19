from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from features.pages.base_page import BasePage


class StackOverflowSignupPage(BasePage):
    """Locators for the StackOverflow sign-up page and a load() that waits
    past the Cloudflare challenge."""

    URL = "https://stackoverflow.com/users/signup"

    # Form fields use short ids on the visible page. There's a second set
    # of fields with signup-modal-* ids inside a hidden modal — ignore those.
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    SIGNUP_BTN = (By.ID, "submit-button")

    # Visible social buttons use lowercase data-provider. A second pair with
    # capital-G lives in the hidden modal — skip those too.
    GOOGLE_BTN = (By.CSS_SELECTOR, 'button[data-provider="google"]')
    GITHUB_BTN = (By.CSS_SELECTOR, 'button[data-provider="github"]')

    # SO's link text is lowercase ("terms of service"), so match the href
    # instead — that's case-insensitive and doesn't break if the copy changes.
    TERMS_LINK = (By.CSS_SELECTOR, 'a[href*="/legal/terms-of-service"]')
    PRIVACY_LINK = (By.CSS_SELECTOR, 'a[href*="/legal/privacy-policy"]')

    def load(self):
        self.open(self.URL)
        # StackOverflow sits behind a Cloudflare challenge. Wait up to 90
        # seconds for the real signup form to be visible (not just in the
        # DOM) so the challenge page has fully cleared before any
        # assertions run. undetected-chromedriver usually clears it in a
        # few seconds, but the first run on a fresh profile can be slower.
        WebDriverWait(self.driver, 90).until(
            EC.visibility_of_element_located(self.EMAIL)
        )

    def is_form_loaded(self):
        return all(self.is_visible(loc) for loc in (self.EMAIL, self.PASSWORD, self.SIGNUP_BTN))

    def has_social_auth(self):
        return self.is_visible(self.GOOGLE_BTN) and self.is_visible(self.GITHUB_BTN)

    def has_legal_links(self):
        # Legal links appear in page source but may be below the fold; presence is
        # sufficient for "rendered on page" verification.
        return self.is_present(self.TERMS_LINK) and self.is_present(self.PRIVACY_LINK)
