"""Reusable window-handling steps. The same step bodies match both the
HW8 assignment phrasing and a generic phrasing, so future scenarios
that need to handle popups or new tabs (OAuth, payment redirects, T&C
links elsewhere) can pick whichever wording reads better."""

import logging

from behave import step


log = logging.getLogger("generic_steps")


@step("Store original window")
@step("Store current window state")
def step_store_window_state(context):
    context.window_state = context.app.home_page.get_window_state()
    context.original_window = context.window_state["handle"]
    log.info("Stored window state: %s", context.window_state)


@step("Switch to the newly opened window")
@step("Switch to newest window")
def step_switch_to_new_window(context):
    snapshot = context.window_state["handles_snapshot"]
    context.app.home_page.switch_to_new_window(snapshot)
    assert context.driver.current_window_handle != context.original_window, (
        "Window switch did not produce a different active handle"
    )


@step("User can close new window and switch back to original")
@step("Close current window and switch back to stored window")
def step_close_and_return(context):
    context.app.home_page.close_window()
    context.app.home_page.switch_to_window_by_id(context.original_window)
    assert context.driver.current_window_handle == context.original_window, (
        "Did not return to the stored original window"
    )


@step("Refresh the page")
def step_refresh_page(context):
    context.app.home_page.refresh_page()
