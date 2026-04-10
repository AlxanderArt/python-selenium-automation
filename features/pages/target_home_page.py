from selenium.webdriver.common.by import By


class TargetHomePage:

    URL = "https://www.target.com/"

    ACCOUNT_BTN = (By.LINK_TEXT, "Account")
    SIGN_IN_BTN = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')

    SIGNIN_HEADER = (By.XPATH, '//h1[contains(text(),"Sign in or create account")]')
    SIGNIN_BUTTON = (By.ID, "login")
