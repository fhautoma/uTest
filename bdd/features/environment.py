from behave import use_fixture
from bdd.fixtures.fixtures import use_chrome_browser, close_browser


def before_tag(context, tags):
    if 'use.chrome.browser' in tags:
        use_fixture(use_chrome_browser, context)


def after_scenario(context, scenario):
    use_fixture(close_browser, context)