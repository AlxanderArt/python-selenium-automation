from behave import when, then

from pages.target_signin_page import TargetSignInPage


@when("user clicks Sign In from side menu")
def step_click_signin_side(context):
    context.home.click_signin_from_side_menu()


@then("Sign In form is opened")
def step_signin_form_opened(context):
    signin = TargetSignInPage(context.driver)
    assert signin.is_form_loaded(), "Sign In form (email + login button) not visible"
