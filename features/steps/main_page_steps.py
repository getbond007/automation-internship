from behave import given, when, then
import os

#Set 2 environment variables REELLY_USER_ID and REELLY_PASSWORD
USER_ID = os.getenv("REELLY_USER_ID")
PASSWORD = os.getenv("REELLY_PASSWORD")

@given('Open Reelly main page')
def open_reelly(context):
   context.app.main_page.open_main()


@when('Log in to the page')
def sing_in(context):
    context.app.main_page.sing_in(USER_ID,PASSWORD)