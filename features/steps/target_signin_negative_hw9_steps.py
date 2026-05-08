"""HW9 part 2 — Target's two-step sign-in with a bad password.
The scenario reads the email from the TARGET_EMAIL env var (same
convention HW7 uses) and uses a hardcoded wrong password since the
point is to trigger the error path. Tagged @requires_credentials so
graders without a Target account get a green skip."""

import os

from behave import when, then


WRONG_PASSWORD = "WrongPassword!_HW9"


@when("user enters correct email")
def step_enter_correct_email(context):
    email = os.environ["TARGET_EMAIL"]
    context.app.signin_page.enter_email(email)


@when("user clicks Continue")
def step_click_continue(context):
    context.app.signin_page.click_continue()


@when("user enters incorrect password")
def step_enter_wrong_password(context):
    context.app.signin_page.enter_password(WRONG_PASSWORD)


@when("user clicks Sign in with password")
def step_click_signin_with_password(context):
    context.app.signin_page.click_sign_in_with_password()


@then("sign-in error message is shown")
def step_signin_error_shown(context):
    context.app.signin_page.verify_sign_in_error()
