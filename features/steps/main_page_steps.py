from behave import given, when, then
import os

#Set 2 environment variables REELLY_USER_ID and REELLY_PASSWORD
USER_ID = os.getenv("REELLY_USER_ID")
PASSWORD = os.getenv("REELLY_PASSWORD")

@given('Open Reelly home page')
def open_reelly(context):
    context.app.home_page.open_home()

@when('Log in to the main page')
def sing_in(context):
    context.app.login_page.sing_in(USER_ID,PASSWORD)
