from behave import then

@then('Click on off plan at the left side menu')
def click_on_off_plan(context):
    context.app.off_plan_page.click_on_off_plan()

@then('Verify the right page opens')
def verify_off_plan(context):
    context.app.off_plan_page.verify_off_plan()

@then('Click on Sales status dropdown menu and Select sales status of “Out of Stocks"')
def click_on_sales_status_drop_down(context):
    context.app.off_plan_page.select_status_out_of_stocks()

@then('Verify each product contains the Out of Stocks tag')
def verify_out_of_stocks(context):
    context.app.off_plan_page.verify_out_of_stocks()
