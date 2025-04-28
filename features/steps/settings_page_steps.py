from behave import then

@then('Click on Settings at the left side menu')
def click_on_settings(context):
    context.app.settings_page.click_on_settings()

@then('Verify the Settings page opens')
def verify_settings_page(context):
    context.app.settings_page.verify_settings_page()

@then('Verify there are 13 options for the settings')
def verify_settings_option(context):
    context.app.settings_page.verify_settings_option()

@then('Verify “connect the company” button is available')
def verify_connect_the_company_option(context):
    context.app.settings_page.verify_connect_the_company_option()