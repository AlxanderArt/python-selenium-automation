from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.amazon_signin_page import AmazonSignInPage


@given("user is on Amazon sign in page")
def step_impl(context):
    context.driver.get(AmazonSignInPage.URL)
    wait = WebDriverWait(context.driver, 10)
    # Wait for the account link to be clickable instead of sleeping for 2s —
    # it appears as soon as the homepage header renders, no need to guess.
    wait.until(EC.element_to_be_clickable(AmazonSignInPage.ACCOUNT_LIST)).click()
    # Wait for the sign-in page to actually load by watching for the email
    # input. Replaces the old sleep(3).
    wait.until(EC.visibility_of_element_located(AmazonSignInPage.EMAIL_INPUT))


@then("all primary elements are visible")
def step_impl(context):
    assert context.driver.find_element(*AmazonSignInPage.LOGO).is_displayed()
    assert context.driver.find_element(*AmazonSignInPage.EMAIL_INPUT).is_displayed()
    assert context.driver.find_element(*AmazonSignInPage.CONTINUE_BTN).is_displayed()


@then("all secondary elements are visible")
def step_impl(context):
    assert context.driver.find_element(*AmazonSignInPage.CONDITIONS_LINK).is_displayed()
    assert context.driver.find_element(*AmazonSignInPage.PRIVACY_LINK).is_displayed()
    assert context.driver.find_element(*AmazonSignInPage.NEED_HELP_LINK).is_displayed()
    assert context.driver.find_element(*AmazonSignInPage.CREATE_ACCOUNT_LINK).is_displayed()
