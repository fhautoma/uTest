from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def use_chrome_browser(context, **kwargs):
    context.browser = webdriver.Chrome(ChromeDriverManager().install())
    context.browser.maximize_window()


def close_browser(context):
    context.browser.quit()
