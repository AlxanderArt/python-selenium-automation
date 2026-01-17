from behave import given, when, then


@given('Open Target App page')
def open_target_app_page(context):
    context.app.target_app_page.open_target_app()


@when('Click Privacy Policy link')
def click_pp_link(context):
    context.app.target_app_page.click_pp_link()
