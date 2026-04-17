"""Target.com steps that more than one feature file uses — opening the
homepage and opening the account menu."""

from behave import given, when

from features.pages.target_home_page import TargetHomePage


@given("user opens Target homepage")
def step_open_target_homepage(context):
    context.home = TargetHomePage(context.driver)
    context.home.load()


@when("user opens account menu")
def step_open_account_menu(context):
    context.home.open_account_menu()
