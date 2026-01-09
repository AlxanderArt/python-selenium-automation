from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_FIELD = (By.ID, 'search')
SEARCH_ICON = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")


@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.find_element(*SEARCH_ICON).click()
    sleep(10)


@then('Verify {expected_amount} top header links are shown')
def verify_top_links_shown(context, expected_amount):
    # print(type(expected_amount)) # "6"
    expected_amount = int(expected_amount) # "6" str => 6 int
    links = context.driver.find_elements(*HEADER_LINKS)
    # print(links)
    # assert 6 == 6
    assert len(links) == expected_amount, f'Expected {expected_amount} header links, but got {len(links)}'

