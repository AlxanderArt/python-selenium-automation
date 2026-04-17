from behave import when, then

from features.pages.target_signin_page import TargetSignInPage


@when("user clicks sign in")
def step_click_signin(context):
    context.home.click_signin_from_side_menu()


@then("sign in page is displayed")
def step_signin_page_displayed(context):
    signin = TargetSignInPage(context.driver)
    assert signin.is_chooser_displayed() or signin.is_form_loaded(), \
        "Sign in page (chooser or form) not visible"
