"""Sign-in side-menu navigation. Page calls go through context.app — the
Application aggregator owns the page objects."""

from behave import when, then


@when("user clicks Sign In from side menu")
def step_click_signin_side(context):
    context.app.home_page.click_signin_from_side_menu()


@then("Sign In form is opened")
def step_signin_form_opened(context):
    assert context.app.signin_page.is_form_loaded(), \
        "Sign In form (email + login button) not visible"
