from behave import when, then
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.target_search_page import TargetSearchPage


@when('user searches for "{term}"')
def step_user_searches_for(context, term):
    context.search_page = TargetSearchPage(context.driver)
    context.search_page.search(term)


@then('product results for "{term}" are shown')
def step_product_results_shown(context, term):
    # Two checks: the search term is reflected in the URL, and at least one
    # result card came back.
    current_url = context.driver.current_url.lower()
    assert term.lower().replace(" ", "+") in current_url \
        or term.lower().replace(" ", "%20") in current_url \
        or term.lower() in current_url, \
        f'Expected "{term}" in URL but got {current_url}'

    results = context.search_page.get_results()
    assert results, f'No result cards shown for "{term}"'


@then("every result on the search page has a product name and a product image")
def step_every_result_has_name_and_image(context):
    # First make sure the result count has stabilized — the page lazy-loads
    # more cards as you scroll, so an early read can miss the bottom rows.
    context.search_page.scroll_until_all_results_loaded()
    results = context.search_page.get_results()
    assert results, "No result cards on the search page"

    title_locator = (By.CSS_SELECTOR, 'a[data-test="@web/ProductCard/title"]')
    # img src can lazy-load on srcset or data-src on Target — accept any of
    # them as proof the image is wired up.
    image_locator = (By.CSS_SELECTOR, "img")

    driver = context.driver
    missing = []
    for idx, card in enumerate(results, start=1):
        # Each card hydrates only when it enters the viewport, so scroll it
        # into view, then wait for its title link and image to actually
        # render before reading them. This keeps us from flagging cards as
        # 'missing' when they just hadn't been scrolled to yet.
        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", card
        )

        title_text = ""
        try:
            WebDriverWait(driver, 5).until(
                lambda _d, c=card: bool(
                    (c.find_element(*title_locator).text or "").strip()
                )
            )
            title_text = card.find_element(*title_locator).text.strip()
        except (TimeoutException, NoSuchElementException):
            pass

        src = ""
        try:
            WebDriverWait(driver, 5).until(
                lambda _d, c=card: bool(
                    c.find_element(*image_locator).get_attribute("src")
                    or c.find_element(*image_locator).get_attribute("data-src")
                    or c.find_element(*image_locator).get_attribute("srcset")
                )
            )
            img = card.find_element(*image_locator)
            src = (
                img.get_attribute("src")
                or img.get_attribute("data-src")
                or img.get_attribute("srcset")
                or ""
            ).strip()
        except (TimeoutException, NoSuchElementException):
            pass

        if not title_text:
            missing.append(f"card #{idx}: missing product name")
        if not src:
            missing.append(f"card #{idx}: missing product image")

    assert not missing, "Result cards failed validation:\n  " + "\n  ".join(missing)
