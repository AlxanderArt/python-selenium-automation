import logging

from behave import when, then

from features.pages.target_cart_page import TargetCartPage


log = logging.getLogger(__name__)


@when("user clicks the cart icon")
def step_click_cart(context):
    log.info("Clicking cart icon")
    context.cart_page = TargetCartPage(context.driver)
    context.cart_page.open_cart()


@then("empty cart message is displayed")
def step_cart_empty(context):
    assert context.cart_page.is_cart_empty(), "'Your cart is empty' message not visible"
