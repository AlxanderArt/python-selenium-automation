from behave import given, when, then


@given('Store original window')
def store_window(context):
    context.original_window = context.app.base_page.get_current_window_handle()
    print('Original window: ', context.original_window)
    # print('All windows: ', context.driver.window_handles)


@when('Switch to new window')
def switch_to_new_window(context):
    context.app.base_page.switch_to_new_window()


@then('Close current page')
def close_page(context):
    context.app.base_page.close_page()


@then('Return to original window')
def return_to_window(context):
    context.app.base_page.switch_to_window_by_id(context.original_window)
