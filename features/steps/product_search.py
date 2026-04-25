from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')


@given('Open Google page')
def open_google(context):
    context.driver.get('https://www.google.com/')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    # Wait for the input to actually be there before typing — replaces
    # sleep(4) which was just hoping the page had loaded.
    wait = WebDriverWait(context.driver, 10)
    search = wait.until(EC.visibility_of_element_located(SEARCH_INPUT))
    search.clear()
    search.send_keys(search_word)


@when('Click on search icon')
def click_search_icon(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.element_to_be_clickable(SEARCH_SUBMIT)).click()
    # Wait for the URL to actually reflect the search before letting the
    # next step run — replaces sleep(1).
    wait.until(lambda d: "search" in d.current_url.lower())


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), \
        f'Expected query not in {context.driver.current_url.lower()}'
