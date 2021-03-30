from behave import Given, When, Then
from bdd.pages.home_page.home_page import HomePage
from bdd.pages.user_form_page.user_form_page import UserFormPage
import time


@Given('a browser is used to load the URL "{url}"')
def step_def(context, url):
    context.current_page = HomePage(context)
    context.current_page.open_url(url)


@When('make click in JoinToday button')
def step_def(context):
    context.current_page.click_in_join_button()


@Then('wait until user form page loads')
def step_def(context):
    context.current_page = UserFormPage(context)
    context.current_page.wait_until_page_load()


@When('fill user fields in form')
def step_def(context):
    context.current_page.fill_user_from_fields()


@Then('click in next button')
def step_def(context):
    context.current_page.click_in_next_button()





