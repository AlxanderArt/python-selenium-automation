from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class TargetColorPickerPage(BasePage):
    """Product detail page that has multiple color variants. Wraps the color
    swatch links and the 'selected' indicator on Target PDPs so the test can
    loop through every color and confirm each one becomes the selected one
    after a click."""

    # Smocked blouse PDP from the HW5 prompt — pinned so the test is
    # deterministic about which page it's running against.
    URL = (
        "https://www.target.com/p/women-s-smocked-blouse-universal-thread-red"
        "/-/A-95081560?preselect=95162150"
    )

    # Each color swatch on this PDP is an <a> with aria-label like
    # 'Color, Blue' or 'Color, Blue, selected'. They navigate to a sibling
    # SKU URL when clicked, so the click is verified by waiting for the page
    # to come back with that color marked as selected.
    COLOR_SWATCH = (By.CSS_SELECTOR, 'a[aria-label^="Color, "]')

    # Variation block — wait for this to render before reading swatches so
    # the loop never runs against a half-hydrated page.
    VARIATION_COMPONENT = (
        By.CSS_SELECTOR,
        '[data-test="@web/VariationComponent"]',
    )

    def load(self):
        self.open(self.URL)
        self.find(self.VARIATION_COMPONENT)
        # Wait until at least one color swatch link is in the DOM.
        self.wait.until(
            EC.presence_of_element_located(self.COLOR_SWATCH)
        )

    def get_color_swatches(self):
        # Re-query each call — clicking a swatch navigates the page and
        # invalidates older element references.
        self.find(self.VARIATION_COMPONENT)
        return self.driver.find_elements(*self.COLOR_SWATCH)

    def get_color_names(self):
        names = []
        for sw in self.get_color_swatches():
            label = (sw.get_attribute("aria-label") or "").strip()
            name = self._color_name_from_label(label)
            if name:
                names.append(name)
        return names

    def selected_color_name(self):
        # Whichever swatch carries the 'selected' suffix is the active one.
        for sw in self.get_color_swatches():
            label = (sw.get_attribute("aria-label") or "").lower()
            if label.endswith(", selected"):
                return self._color_name_from_label(
                    sw.get_attribute("aria-label") or ""
                )
        return ""

    def click_color_by_name(self, name):
        # Build a locator that matches the swatch for this exact color, then
        # scroll-and-click. Re-querying inside the wait handles the case
        # where the page rerenders mid-click.
        locator = (
            By.CSS_SELECTOR,
            f'a[aria-label^="Color, {name}"]',
        )
        el = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", el
        )
        el.click()
        # Treat the click as 'done' only once a swatch with this color name
        # reports itself as selected on the post-navigation page.
        self.wait.until(self._color_is_selected(name))

    def _color_is_selected(self, name):
        target = name.lower()

        def _check(driver):
            elements = driver.find_elements(*self.COLOR_SWATCH)
            for el in elements:
                label = (el.get_attribute("aria-label") or "").lower()
                if label == f"color, {target}, selected":
                    return True
            return False

        return _check

    @staticmethod
    def _color_name_from_label(label):
        # aria-label is 'Color, Blue' or 'Color, Blue, selected' — pull the
        # color name out of the middle.
        parts = [p.strip() for p in label.split(",")]
        if len(parts) >= 2 and parts[0].lower() == "color":
            return parts[1]
        return ""
