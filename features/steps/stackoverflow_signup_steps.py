import logging

from behave import given, then

from pages.stackoverflow_signup_page import StackOverflowSignupPage


log = logging.getLogger(__name__)


@given("user opens StackOverflow signup page")
def step_open_signup(context):
    context.page = StackOverflowSignupPage(context.driver)
    context.page.load()


@then("signup form is fully loaded")
def step_form_loaded(context):
    log.info("Validating signup form is fully loaded")
    assert context.page.is_form_loaded(), "Signup form fields not fully visible"


@then("social authentication options are available")
def step_social_auth(context):
    log.info("Validating social auth buttons are present")
    assert context.page.has_social_auth(), "Google/GitHub signup buttons not visible"


@then("legal links are present")
def step_legal_links(context):
    log.info("Validating Terms + Privacy links")
    assert context.page.has_legal_links(), "Terms or Privacy link not visible"
