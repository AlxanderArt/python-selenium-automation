"""HW9 part 1 — open the Target Help center on the Returns page,
pick a different topic from the dropdown, verify the new help page
loads. The actual dropdown + verification steps live in
generic_steps.py so they can be reused by other dropdown scenarios."""

from behave import given


@given("Open Help page for Returns")
def step_open_help_returns(context):
    context.app.help_page.open_returns_page()
