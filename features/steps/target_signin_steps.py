"""Sign-in navigation steps. Page calls go through context.app so the step
file doesn't build pages itself."""

from behave import when, then


@when("user clicks sign in")
def step_click_signin(context):
    context.app.home_page.click_signin_from_side_menu()


@then("sign in page is displayed")
def step_signin_page_displayed(context):
    signin = context.app.signin_page
    assert signin.is_chooser_displayed() or signin.is_form_loaded(), \
        "Sign in page (chooser or form) not visible"
