from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from features.pages.base_page import BasePage


class TargetSearchPage(BasePage):
    """Search bar on the Target homepage header and the product result cards
    that come back on target.com/s."""

    SEARCH_INPUT = (By.ID, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]')
    RESULT_CARDS = (
        By.CSS_SELECTOR,
        '[data-test="@web/site-top-of-funnel/ProductCardWrapper"]',
    )
    # The clickable title link inside each result card — more reliable than
    # clicking the wrapper div.
    PRODUCT_TITLE_LINK = (By.CSS_SELECTOR, 'a[data-test="@web/ProductCard/title"]')

    def search(self, term):
        # Type the term, then submit with ENTER. Clicking the search button
        # on its own didn't always submit the form — pressing Enter while
        # the input has focus is more reliable.
        el = self.find_visible(self.SEARCH_INPUT)
        el.clear()
        el.send_keys(term)
        el.send_keys(Keys.ENTER)
        # Wait for target.com to actually navigate to the search results page
        # before returning — otherwise later steps race with the redirect.
        self.wait.until(lambda d: "searchterm=" in d.current_url.lower())

    def get_results(self):
        return self.find_elements(self.RESULT_CARDS)

    def scroll_until_all_results_loaded(self, max_iterations=20, step_timeout=3):
        # Target lazy-loads result cards as the page scrolls — anything below
        # the initial viewport renders without its title link or image, so a
        # naive validation loop will see those as 'missing' even though they
        # would render fine for a real user. Scroll in steps and wait for the
        # card count to actually grow each time; stop once it stabilizes.
        last_count = -1
        for _ in range(max_iterations):
            current = len(self.driver.find_elements(*self.RESULT_CARDS))
            if current == last_count and current > 0:
                return current
            last_count = current
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )
            try:
                WebDriverWait(self.driver, step_timeout).until(
                    lambda d: len(d.find_elements(*self.RESULT_CARDS)) > current
                )
            except TimeoutException:
                # No new cards loaded in this window — likely at the bottom.
                # One more iteration with the same count exits cleanly.
                pass
        return last_count

    def open_first_result(self):
        results = self.get_results()
        assert results, "No product result cards on the search page"
        # Navigate by href instead of clicking — Target sometimes overlays
        # result cards with a sponsored ad that intercepts the click at the
        # last moment. Pulling the product URL off the title link and
        # hitting it directly skips the overlay problem entirely.
        first_title = results[0].find_element(*self.PRODUCT_TITLE_LINK)
        href = first_title.get_attribute("href")
        assert href, "First result has no href"
        self.driver.get(href)
