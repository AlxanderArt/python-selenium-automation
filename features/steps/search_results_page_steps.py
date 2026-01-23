from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


SEARCH_RESULTS_TEXT = (By.XPATH, "//div[contains(@class,'styles_listingPageResultsCount')]")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()  # always clicks on 1st Add to cart btn
    context.driver.wait.until(
        EC.element_to_be_clickable(SIDE_NAV_ADD_TO_CART_BTN),
        message='Side navigation Add To Cart Btn not clickable'
    )


@when('Store product name')
def store_product_name(context):
    context.product_before_adding = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    # print("Name saved: ")
    # print(context.product_before_adding)


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
    sleep(2)


@when('Hover favorites icon')
def hover_fav_icon(context):
    context.app.search_results_page.hover_fav_icon()


@then('Search results for {expected_product} are shown')
def verify_search_results(context, expected_product):
    context.app.search_results_page.verify_search_results(expected_product)


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    # context.driver.execute_script("window.scrollBy(0,2000)", "")
    # sleep(0.5)
    # context.driver.execute_script("window.scrollBy(0,2000)", "")
    # sleep(0.5)
    # If you ever need to scroll up, use negative numbers: context.driver.execute_script("window.scrollBy(0, -2000)", "")

    products = context.driver.find_elements(*LISTINGS)  # [WebEl1, WebEl2, WebEl3, WebEl4]
    for product in products[:8]:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(f'🟢{title}')
        product.find_element(*PRODUCT_IMG)


@then('Favorites tooltip is shown')
def verify_fav_tooltip(context):
    context.app.search_results_page.verify_fav_tooltip()