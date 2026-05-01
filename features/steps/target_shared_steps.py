"""Target.com steps shared across feature files. Both calls go through
context.app.home_page — the Application aggregator wired up in
environment.before_scenario already holds the page object, so the step
file doesn't import TargetHomePage or build it inline."""

from behave import given, when


@given("user opens Target homepage")
def step_open_target_homepage(context):
    context.app.home_page.load()


@when("user opens account menu")
def step_open_account_menu(context):
    context.app.home_page.open_account_menu()
