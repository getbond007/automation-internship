from behave import then

@then('Click on “Secondary” option at the left side menu')
def click_on_secondary(context):
    context.app.secondary_deals_page.click_on_secondary()

@then('Verify the Secondary deals page opens')
def verify_secondary_page(context):
    context.app.secondary_deals_page.verify_secondary_page()

@then('Click on filter option')
def click_on_filter(context):
    context.app.secondary_deals_page.click_on_filter()

@then('Filter the products by “want to buy” and Click on Apply Filter')
def filter_by_products(context):
    context.app.secondary_deals_page.filter_by_products()

@then('Verify all cards have “Want to buy” tag')
def verify_each_listing(context):
    context.app.secondary_deals_page.verify_each_secondary_listings("LISTING_TYPE")

@then('Filter the listings by price range from 1200000 to 2000000 AED')
def filter_by_price(context):
    context.app.secondary_deals_page.filter_by_price()

@then('Verify the price in all listings is inside the range (1200000 - 2000000)')
def verify_price(context):
    context.app.secondary_deals_page.verify_each_secondary_listings("PRICE_RANGE")