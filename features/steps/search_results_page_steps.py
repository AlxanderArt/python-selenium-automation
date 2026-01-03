from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_RESULTS_TEXT = (By.XPATH, "//div[contains(@class,'styles_listingPageResultsCount')]")


@then('Search results for {expected_product} are shown')
def verify_search_results(context, expected_product):
    actual_text = context.driver.find_element(*SEARCH_RESULTS_TEXT).text
    assert expected_product in actual_text, f'Expected text {expected_product} not in actual text {actual_text}'

