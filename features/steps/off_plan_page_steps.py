from selenium.webdriver.common.by import By
from behave import then
from selenium.webdriver.support import expected_conditions as EC

OUT_OF_STOCK_STATUS = (By.XPATH, "//div[@class='_5-comission']")
OFF_PLAN_MENU = (By.XPATH, "//a[@class='menu-text-link-leaderboard w--current']")


@then('Click on off plan at the left side menu')
def click_on_off_plan(context):
    context.app.off_plan_page.click_on_off_plan()
    context.driver.wait.until(
        EC.element_to_be_clickable(OFF_PLAN_MENU),
        message='off plan menu button not clickable'
    )


@then('Verify the right page opens')
def verify_off_plan(context):
    context.app.off_plan_page.verify_off_plan()


@then('Click on Sales status dropdown menu and Select sales status of “Out of Stocks"')
def click_on_sales_status_drop_down(context):
    context.app.off_plan_page.select_status_out_of_stocks()
    context.driver.wait.until(
        EC.visibility_of_element_located(OUT_OF_STOCK_STATUS),
        message='Out of stock status  not visible'
    )

@then('Verify each product contains the Out of Stocks tag')
def verify_out_of_stocks(context):
    context.app.off_plan_page.verify_out_of_stocks()
