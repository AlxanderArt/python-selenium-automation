from behave import given, when, then


@then('Verify Privacy Policy page opened')
def verify_pp_page_opened(context):
    context.app.privacy_policy_page.verify_page_opened()
