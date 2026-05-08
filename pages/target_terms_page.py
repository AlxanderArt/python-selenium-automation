from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class TargetTermsPage(BasePage):
    """Target Terms and Conditions page — verifies the new window
    landed on the T&C URL, with title as a fallback in case the
    URL slug shifts."""

    URL_FRAGMENT = "target-terms-conditions"

    def verify_terms_page_opened(self):
        WebDriverWait(self.driver, 15).until(
            lambda d: self.URL_FRAGMENT in d.current_url
            or "terms" in (d.title or "").lower()
        )
        url = self.driver.current_url
        title = (self.driver.title or "").lower()
        assert self.URL_FRAGMENT in url or "terms" in title, (
            f"Terms and Conditions page did not open — "
            f"url={url!r}, title={title!r}"
        )
