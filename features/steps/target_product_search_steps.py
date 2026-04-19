from behave import when, then

from features.pages.target_search_page import TargetSearchPage


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
