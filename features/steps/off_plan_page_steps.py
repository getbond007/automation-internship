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

@then('Verify that each product contains the Out of Stocks tag')
def verify_out_of_stocks(context):
    context.app.off_plan_page.verify_out_of_stocks()

@then('Filter the products by price range from 1200000 to 2000000 AED')
def filter_products_by_price(context):
    context.app.off_plan_page.filter_products_by_price()

@then('Verify the price in all cards is inside the range (1200000 - 2000000)')
def verify_price_in_cards(context):
    context.app.off_plan_page.verify_each_off_plan_page("PRICE_FILTER")

@then('Verify each product on this page contains a title and picture visible')
def verify_product_title_image_in_cards(context):
    context.app.off_plan_page.verify_each_off_plan_page("PRODUCT_TITLE")