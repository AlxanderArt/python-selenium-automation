from behave import given, then

from features.pages.target_circle_page import TargetCirclePage


@given("user opens Target Circle page")
def step_open_circle(context):
    context.circle = TargetCirclePage(context.driver)
    context.circle.load()


@then('there are {count:d} storycards under "Unlock added value"')
def step_storycard_count(context, count):
    actual = context.circle.count_unlock_storycards()
    assert actual == count, (
        f'Expected {count} storycards under "Unlock added value", got {actual}'
    )
