from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
TOTAL_TXT = (By.CSS_SELECTOR, "h2 [class*='styles_cart-summary-span']")


@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    context.driver.wait.until(
        EC.presence_of_element_located(TOTAL_TXT),
        message='Subtotal text did not appear'
    )

    cart_summary = context.driver.find_element(*TOTAL_TXT).text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"


@then('Verify product in cart is correct')
def verify_product(context):
    product_in_cart = context.driver.find_element(*PRODUCT_NAME).text
    # print('\nProduct in cart:')
    # print(product_in_cart)
    expected = context.product_before_adding
    assert product_in_cart[:20] == expected[:20],\
        f'Expected product {expected[:20]} but got {product_in_cart[:20]}'


@then('Empty Cart message is shown')
def verify_empty_cart_msg(context):
    context.app.cart_page.verify_empty_cart_msg()