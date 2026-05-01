"""Add-to-cart scenario rewritten with the Page Object Model (HW7).

Every page interaction goes through context.app, which is wired up in
environment.before_scenario. The step file no longer imports page classes
or constructs them inline — that's the Application aggregator's job."""

from behave import when, then


@when("user opens the first search result")
def step_open_first_result(context):
    context.app.search_page.open_first_result()


@when("user adds the product to cart")
def step_add_to_cart(context):
    context.app.product_page.add_to_cart()


@then("cart has at least {count:d} item")
def step_cart_has_items(context, count):
    actual = context.app.cart_page.item_count()
    assert actual >= count, f"Expected at least {count} item(s) in cart, got {actual}"
