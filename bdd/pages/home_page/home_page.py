from bdd.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class HomePage(BasePage):
    JOIN_TODAY_BUTTON = \
        (By.XPATH, '/html/body/ui-view/unauthenticated-container/div/div/unauthenticated-header/div/div[3]/ul[2]/li['
                   '2]/a')

    def __init__(self, context):
        BasePage.__init__(self, context=context)

    def open_url(self, url):
        self.context.browser.get(url)

    def click_in_join_button(self):
        WebDriverWait(self.context.browser, 20).until(ec.element_to_be_clickable(self.JOIN_TODAY_BUTTON)).click()






