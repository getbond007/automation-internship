#####Instruction on how to set user id and passowrd########
#######Set 2 environment variables REELLY_USER_ID and REELLY_PASSWORD
#######under Run/Debug Configuration of this test feature
Feature: Test Scenarios for filter functionality of off-plan page

  Scenario: User can filter by sale status Out of Stocks
    Given Open Reelly main page
    When Log in to the page
    Then Click on off plan at the left side menu
    And Verify the right page opens
    And Click on Sales status dropdown menu and Select sales status of “Out of Stocks"
    And Verify each product contains the Out of Stocks tag