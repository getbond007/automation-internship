from time import sleep

from selenium.common import NoSuchElementException

from pages.base_page import Page
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class OffPlanPage(Page):

    OFF_PLAN_MENU = (By.XPATH, "//a[@class='menu-text-link-leaderboard w--current']")
    SALES_STATUS = (By.CSS_SELECTOR,"#Location-2")
    OUT_OF_STOCK_STATUS = (By.XPATH, "//div[@class='_5-comission']")
    OFF_PLAN_TITLE = (By.CSS_SELECTOR,"div.page-title.off_plan")

    FILTER_ICON = (By.CSS_SELECTOR, 'a .filter-text')
    FILTER_PRICE_FROM = (By.CSS_SELECTOR, '[wized="unitPriceFromFilter"]')
    FILTER_PRICE_TO = (By.CSS_SELECTOR, '[wized="unitPriceToFilter"]')
    APPLY_FILTER_BUTTON = (By.XPATH, '//a[text()="Apply filter"]')

    CARDS_MIN_PRICE = (By.CSS_SELECTOR, '[wized="projectMinimumPrice"]')

    LIST_OF_PROJECTS = (By.CSS_SELECTOR,'[wized="cardOfProperty"]')
    TITLE_IN_EACH_CARD = (By.CSS_SELECTOR,"div.project-name")
    IMAGE_IN_EACH_CARD = (By.CSS_SELECTOR,"div.project-image")

    TOTAL_NUM_OF_PROJECTS = (By.CSS_SELECTOR, '[wized="totalPropertyCounter"]')

    NEXT_PAGE = (By.CSS_SELECTOR, '[wized="nextPageProperties"]')
    TOTAL_NUMBER_OF_PAGES = (By.CSS_SELECTOR, '[wized="totalPageProperties"]')
    CURRENT_PAGE_COUNT = (By.CSS_SELECTOR, '[wized="currentPageProperties"]')

    #Select the off plan menu option
    def click_on_off_plan(self):
        self.wait_for_element_to_appear(*self.OFF_PLAN_MENU)
        self.wait_to_be_clickable(*self.OFF_PLAN_MENU)

    #Verify that correct page is opened
    def verify_off_plan(self):
        self.wait_for_element_to_appear(*self.OFF_PLAN_TITLE)
        expected_title = "Total projects"
        self.verify_text(expected_title, *self.OFF_PLAN_TITLE)

    #Select out of stock option from the dropdown
    def select_status_out_of_stocks(self):
        sales_status_dropdown = Select(self.find_element(*self.SALES_STATUS))
        sales_status_dropdown.select_by_value('Out of stock')

    #Verify if sales status is displaying as expected for selected filter
    def verify_out_of_stocks(self):
        # Find all sales status elements
        self.wait(5)

        statuses = self.find_elements(*self.OUT_OF_STOCK_STATUS)
        #Expectd Status
        expected_text = "Out of stock"

        # Loop through each sales status and check if it has 'out of stock' text
        for status in statuses:
            # Find the text containing the 'out of stock' text within each sales
            actual_text = status.find_element(*self.OUT_OF_STOCK_STATUS).text
            assert expected_text == actual_text, f'Expected {expected_text} did not match actual {actual_text}'

    def filter_products_by_price(self):
        self.wait_for_element_to_appear(*self.FILTER_ICON)
        self.click(*self.FILTER_ICON)
        self.input_text(1200000,*self.FILTER_PRICE_FROM)
        self.input_text(2000000, *self.FILTER_PRICE_TO)
        self.click(*self.APPLY_FILTER_BUTTON)

    def verify_price_in_cards(self):
        # Find all card price elements
        self.wait_for_element_to_appear(*self.CARDS_MIN_PRICE)

        min_prices = self.find_elements(*self.CARDS_MIN_PRICE)

        # Loop through each card price
        for price in min_prices:
            # Find the price of each card and compare with expected
            actual_price = int(price.text.replace('AED','').replace(' ','').replace(',',''))
            assert  1200000 < actual_price < 2000000, f'Actual price {actual_price} did not fall between 1200000 and 2000000'

        #Return total number of products on this page
        return len(min_prices)

    def verify_product_title_image_in_cards(self):
        self.wait_for_element_to_appear(*self.LIST_OF_PROJECTS)
        all_projects = self.find_elements(*self.LIST_OF_PROJECTS)

        for project in all_projects:
            title = project.find_element(*self.TITLE_IN_EACH_CARD).text
            image = project.find_element(*self.IMAGE_IN_EACH_CARD).screenshot_as_png

            assert title is not None, f'Expected Title {title} is not present'
            assert image is not None, f'Expected Image {image} is not present'

        #Return total number of products on this page
        return len(all_projects)

    def verify_report_type(self, report_type):
        child_page_project_count = 0
        # assert the fist page before looping through rest all pages
        if report_type == "PRODUCT_TITLE":
            child_page_project_count = OffPlanPage.verify_product_title_image_in_cards(self)
        elif report_type == "PRICE_FILTER":
            child_page_project_count = OffPlanPage.verify_price_in_cards(self)

        return child_page_project_count

    def verify_each_off_plan_page(self,report_type):
        #Get total number of off plan projects
        self.wait_for_element_to_appear(*self.TOTAL_NUM_OF_PROJECTS)
        total_number_of_projects = self.find_element(*self.TOTAL_NUM_OF_PROJECTS).text

        #Get total number of pagination or child pages
        #We need to loop each page and assert all projects in each page
        self.wait_for_element_to_appear(*self.TOTAL_NUMBER_OF_PAGES)
        total_number_of_pages = int(self.find_element(*self.TOTAL_NUMBER_OF_PAGES).text)

        # To keep track of next page opening or not
        page_increment = 0
        # To keep track of how many projects are asserted, this should match
        # at the end with total number of projects
        project_increment = 0

        # Then Loop through each page
        while total_number_of_pages >= 1:
            # while page_increment <= 2:
            # Reduce the total number of pages so that loop will end after going through all pages
            total_number_of_pages = total_number_of_pages - 1

            # Keep track if clicking "Next" is actually taking to right page number
            page_increment = page_increment + 1

            try:
                # Find what is current page number
                current_page_num = int(self.find_element(*self.CURRENT_PAGE_COUNT).text)
                # Assert if that is the correct page number
                assert current_page_num == page_increment, f'Expected Page Number {current_page_num} is not matching with Actual Page Number {page_increment}'

                # Reuse method call to assert the actual ask
                project_increment = project_increment + OffPlanPage.verify_report_type(self, report_type)

                # Move to next page
                self.find_element(*self.NEXT_PAGE).click()
                self.wait_for_element_to_appear(*self.LIST_OF_PROJECTS)

            except NoSuchElementException:
                print(f'Next Page number {page_increment} not available or required element not present')
            else:
                print(f'Finished Page Number : {page_increment}')

        #Assert if total number of project asserted is same as
        #total number of projects displayed on main page
        assert project_increment == int(total_number_of_projects), f'Expected Product count {project_increment} is not matching with Actual Product count {total_number_of_projects}'
