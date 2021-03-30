from behave import Given, When, Then
from bdd.pages.home_page.home_page import HomePage
import time


@Given('a browser is used to load the URL "{url}"')
def step_def(context, url):
    context.current_page = HomePage(context)
    context.current_page.open_url(url)


@When('make click in JoinToday button')
def step_def(context):
    context.current_page.click_in_join_button()
    

