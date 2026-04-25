"""Empty-cart scenario rewritten with the Page Object Model (HW6).

All page interactions go through context.app, which is wired up in
environment.before_scenario. The step file no longer imports page classes
directly or constructs them inline — that's the application's job."""

import logging

from behave import when, then


log = logging.getLogger(__name__)


@when("user clicks the cart icon")
def step_click_cart(context):
    log.info("Clicking cart icon")
    context.app.cart_page.open_cart()


@then("empty cart message is displayed")
def step_cart_empty(context):
    assert context.app.cart_page.is_cart_empty(), \
        "'Your cart is empty' message not visible"
