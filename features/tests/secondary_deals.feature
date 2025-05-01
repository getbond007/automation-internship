#####Follow below Instructions to run this test
# Set below environment variable under Run/Debug Configuration of this test feature
#1. REELLY_USER_ID : This is the user id to log in to REELLY website
#2. REELLY_PASSWORD : This is the user password to log in to REELLY website
#3. RUN_WITH_DRIVER : One of the values "CHROME" or "FIREFOX"
#4. RUN_WITH_HEADLESS : One of the values 'HEADLESS CHROME' or 'HEADLESS FIREFOX' or NONE

Feature: Test Scenarios for secondary deals

  Scenario: User can filter the Secondary deals by “want to buy” option
    Given Open Reelly home page
    When Log in to the main page
    Then Click on “Secondary” option at the left side menu
    And Verify the Secondary deals page opens
    And Click on filter option
    And Filter the products by “want to buy” and Click on Apply Filter
    And Verify all cards have “Want to buy” tag

  Scenario: User can filter the Secondary deals by Unit price range
    Given Open Reelly home page
    When Log in to the main page
    Then Click on “Secondary” option at the left side menu
    And Verify the Secondary deals page opens
    And Click on filter option
    And Filter the listings by price range from 1200000 to 2000000 AED
    And Verify the price in all listings is inside the range (1200000 - 2000000)