from behave import when, then

from features.pages.target_cart_page import TargetCartPage
from features.pages.target_product_page import TargetProductPage


@when("user opens the first search result")
def step_open_first_result(context):
    # context.search_page is set by the "user searches for ..." step, so
    # the add-to-cart scenario relies on search happening first.
    context.search_page.open_first_result()
    context.product_page = TargetProductPage(context.driver)


@when("user adds the product to cart")
def step_add_to_cart(context):
    context.product_page.add_to_cart()


@then("cart has at least {count:d} item")
def step_cart_has_items(context, count):
    # The cart_page was set earlier by "user clicks the cart icon", but if
    # this scenario ever runs that step against a fresh driver, it still has
    # a driver reference; create one here just in case.
    cart = getattr(context, "cart_page", None) or TargetCartPage(context.driver)
    actual = cart.item_count()
    assert actual >= count, f"Expected at least {count} item(s) in cart, got {actual}"
