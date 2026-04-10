from selenium import webdriver


def browser_init(context):
    """
    :param context: Behave context
    """
    options = webdriver.ChromeOptions()
    options.binary_location = '/Users/alxanderart/Desktop/Google Chrome.app/Contents/MacOS/Google Chrome'
    context.driver = webdriver.Chrome(options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
