from behave import given, when, then


@given('Open Help page for Returns')
def click_cart(context):
    context.app.help_page.open_help_returns()


@when('Select Help topic {option_value}')
def select_topic(context, option_value):
    context.app.help_page.select_topic(option_value)


@then('Verify help {topic} page opened')
def verify_help_topic_opened(context, topic):
    context.app.help_page.verify_help_topic_opened(topic)

#
# @then('Verify help Returns page opened')
# def verify_returns_opened(context):
#     context.app.help_page.verify_returns_opened()
