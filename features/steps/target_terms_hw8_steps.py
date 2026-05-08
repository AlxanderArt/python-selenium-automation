"""HW8 — open the Target sign-in page, click the Terms and Conditions
link in the footer, and verify the T&C page loads in a new window.
The window-handling steps live in generic_steps.py so they can be
reused by other scenarios."""

from behave import given, when, then


@given("Open sign in page")
def step_open_signin_page(context):
    context.app.signin_page.open_signin_page()


@when("Click on Target terms and conditions link")
def step_click_terms_link(context):
    context.app.signin_page.click_terms_link()


@then("Verify Terms and Conditions page is opened")
def step_verify_terms_page(context):
    context.app.terms_page.verify_terms_page_opened()
