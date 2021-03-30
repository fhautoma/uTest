from bdd.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time

class AddressPage(BasePage):
    NEXT_BUTTON = (By.XPATH, '//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[2]/div/a')

    def __init__(self, context):
        BasePage.__init__(self, context=context)

    def click_in_next_button(self):
        WebDriverWait(self.context.browser, 20).until(ec.element_to_be_clickable(self.NEXT_BUTTON)).click()
