from behave import given, when, then

from pages.target_color_picker_page import TargetColorPickerPage


@given("user opens the Target smocked blouse product page")
def step_open_blouse_pdp(context):
    context.color_page = TargetColorPickerPage(context.driver)
    context.color_page.load()


@when("user clicks every available color swatch")
def step_click_every_color(context):
    # Read all color names up front so the loop drives off a stable list,
    # not off element references that can go stale after each click
    # navigates to a different SKU URL.
    color_names = context.color_page.get_color_names()
    assert color_names, "No color swatches found on the product page"

    context.checked_colors = []
    for name in color_names:
        context.color_page.click_color_by_name(name)

        selected = context.color_page.selected_color_name().lower()
        assert selected == name.lower(), (
            f'After clicking "{name}", selected color is "{selected}" '
            f'— expected the swatch for "{name}" to report as selected'
        )
        context.checked_colors.append(name)


@then("every color reports as selected after its click")
def step_every_color_selected(context):
    assert context.checked_colors, "Loop did not click any colors"
    print(f"Verified {len(context.checked_colors)} colors: "
          f"{', '.join(context.checked_colors)}")
