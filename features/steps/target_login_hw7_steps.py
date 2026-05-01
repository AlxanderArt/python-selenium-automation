"""Login steps for the HW7 bonus scenario. Credentials are read from the
TARGET_EMAIL and TARGET_PASSWORD environment variables — never hardcoded.
The scenario is tagged @requires_credentials, and environment.before_scenario
skips it when the env vars aren't set."""

import os

from behave import when, then


@when("user enters email and password")
def step_enter_credentials(context):
    email = os.environ["TARGET_EMAIL"]
    password = os.environ["TARGET_PASSWORD"]
    context.app.signin_page.enter_email(email)
    context.app.signin_page.enter_password(password)


@when("user submits the sign-in form")
def step_submit_signin(context):
    context.app.signin_page.click_sign_in()


@then("user is signed in")
def step_user_is_signed_in(context):
    assert context.app.signin_page.is_signed_in(), \
        "Sign in form is still visible — login may have failed"
