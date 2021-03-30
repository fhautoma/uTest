from selenium.webdriver.support.select import Select

from bdd.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from bdd.config.global_configuration import MOCKAROO_URL, MOCKAROO_API_PATH, MOCKAROO_API_KEY
from bdd.helpers.mappers import month_mapper
import requests
import json
import time
from bdd.helpers.mockaroo_api_call import get_user_form_data_from_api


class UserFormPage(BasePage):

    FIRST_NAME_FIELD = (By.ID, 'firstName')
    LAST_NAME_FIELD = (By.ID, 'lastName')
    EMAIL_FIELD = (By.ID, 'email')
    BIRTH_MONTH_FIELD = 'birthMonth'
    BIRTH_DAY_FIELD = 'birthDay'
    BIRTH_YEAR_FIELD = 'birthYear'
    NEXT_BUTTON = (By.XPATH, '//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[2]/a')

    def __init__(self, context):
        BasePage.__init__(self, context=context)

    def wait_until_page_load(self):
        WebDriverWait(self.context.browser, 60).until(ec.element_to_be_clickable(self.FIRST_NAME_FIELD))

    def fill_user_from_fields(self):

        mockarro_url = f"{MOCKAROO_URL}{MOCKAROO_API_PATH}?key={MOCKAROO_API_KEY}"
        data = requests.get(mockarro_url)
        if data:
            response = json.loads(data.text)
            first_name = response['first_name']
            last_name = response['last_name']
            email = response['email']
        else:
            first_name = 'Andres'
            last_name = 'Henao'
            email = 'fhautomata@gmal.com'

        mont_birth = month_mapper((response['birtdate']).split('-')[1]) if data else 'January'
        day_birth = 'number:26'
        year_birth = 'number:1993'
        WebDriverWait(self.context.browser, 30).\
            until(ec.presence_of_element_located(self.FIRST_NAME_FIELD)).send_keys(first_name)

        WebDriverWait(self.context.browser, 30).\
            until(ec.presence_of_element_located(self.LAST_NAME_FIELD)).send_keys(last_name)

        WebDriverWait(self.context.browser, 30). \
            until(ec.presence_of_element_located(self.EMAIL_FIELD)).send_keys(email)

        Select(self.context.browser.find_element_by_id(self.BIRTH_MONTH_FIELD)).select_by_value(mont_birth)
        Select(self.context.browser.find_element_by_id(self.BIRTH_DAY_FIELD)).select_by_value(day_birth)
        Select(self.context.browser.find_element_by_id(self.BIRTH_YEAR_FIELD)).select_by_value(year_birth)

    def click_in_next_button(self):
        WebDriverWait(self.context.browser, 20).until(ec.element_to_be_clickable(self.NEXT_BUTTON)).click()




