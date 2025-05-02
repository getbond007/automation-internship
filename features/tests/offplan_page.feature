#####Follow below Instructions to run this test
# Set below environment variable under Run/Debug Configuration of this test feature
#1. REELLY_USER_ID : This is the user id to log in to REELLY website
#2. REELLY_PASSWORD : This is the user password to log in to REELLY website
#3. RUN_WITH_DRIVER : One of the values "CHROME" or "FIREFOX"
#4. RUN_WITH_HEADLESS : One of the values 'HEADLESS CHROME' or 'HEADLESS FIREFOX' or NONE

Feature: Test Scenarios for off-plan page

   Scenario: User can open the off plan page and go through the pagination
    Given Open Reelly home page
    When Log in to the main page
    Then Click on off plan at the left side menu
    And Verify the right page opens
    And Go to the final page using the pagination button and Go back to the first page using the pagination button