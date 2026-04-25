from selenium.webdriver.common.by import By


class AmazonSignInPage:

    URL = "https://www.amazon.com"

    # Homepage locator to navigate to Sign In
    ACCOUNT_LIST = (By.ID, "nav-link-accountList")

    # Sign In page locators
    LOGO = (By.CSS_SELECTOR, "i.a-icon-logo")
    EMAIL_INPUT = (By.ID, "ap_email_login")
    CONTINUE_BTN = (By.ID, "continue")

    CONDITIONS_LINK = (By.LINK_TEXT, "Conditions of Use")
    PRIVACY_LINK = (By.LINK_TEXT, "Privacy Notice")

    NEED_HELP_LINK = (By.LINK_TEXT, "Need help?")

    CREATE_ACCOUNT_LINK = (By.ID, "ab-registration-ingress-link")
