from behave import given, when, then
from time import sleep
from features.pages.target_home_page import TargetHomePage


@given("user is on Target homepage")
def step_impl(context):
    context.driver.get(TargetHomePage.URL)
    sleep(3)


@when("user opens account menu")
def step_impl(context):
    context.driver.find_element(*TargetHomePage.ACCOUNT_BTN).click()
    sleep(2)


@when("user clicks sign in")
def step_impl(context):
    context.driver.find_element(*TargetHomePage.SIGN_IN_BTN).click()
    sleep(3)


@then("sign in page is displayed")
def step_impl(context):
    assert context.driver.find_element(*TargetHomePage.SIGNIN_HEADER).is_displayed()
    assert context.driver.find_element(*TargetHomePage.SIGNIN_BUTTON).is_displayed()
