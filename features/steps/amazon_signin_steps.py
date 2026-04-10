from behave import given, when, then
from time import sleep
from features.pages.amazon_signin_page import AmazonSignInPage


@given("user is on Amazon sign in page")
def step_impl(context):
    context.driver.get(AmazonSignInPage.URL)
    sleep(2)
    context.driver.find_element(*AmazonSignInPage.ACCOUNT_LIST).click()
    sleep(3)


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
