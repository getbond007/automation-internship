# Careerist Test Automation repository
written in
### Python 3, Behave
https://www.careerist.com/automation

##### Follow below Instructions to run this test in browser with optional headless 
# Set below environment variables under Run/Debug Configuration of offplan_sales_status_filter.feature
# 1. REELLY_USER_ID : This is the user id to log in to REELLY website
# 2. REELLY_PASSWORD : This is the user password to log in to REELLY website
# 3. RUN_WITH_DRIVER : One of the values "CHROME" or "FIREFOX"
# 4. RUN_WITH_HEADLESS : One of the values 'HEADLESS CHROME' or 'HEADLESS FIREFOX' or NONE

##### Follow below Instructions to run this test in browser stack
# Set below environment variables under Run/Debug Configuration of offplan_sales_status_filter.feature
# 1. RUN_WITH_DRIVER : set it as BROWSERSTACK
# 2. RUN_WITH_HEADLESS : set it as NONE
# 3. BROWSER_STACK_USER : set it as your User Name from browser stack ACCESS KEY drop down
# 4. BROWSER_STACK_KEY : set it as your Access Key from browser stack ACCESS KEY drop down
# 5. BROWSER_OS : set it as your OS example Windows
# 6. BROWSER_OS_VERSION : set it to your OS version example 11 for Windows
# 7. BROWSER_NAME : set it to your browser name example edge for Windows
# So it will look like something as below for Windows:
# BROWSER_NAME=edge;BROWSER_OS=Windows;BROWSER_OS_VERSION=11;BROWSER_STACK_KEY=<Your actual user name>;BROWSER_STACK_USER=<your actual key>;RUN_WITH_DRIVER=BROWSERSTACK;RUN_WITH_HEADLESS=NONE
# And it will look like something as below for MacOS:
# BROWSER_NAME=Chrome;BROWSER_OS=OS X;BROWSER_OS_VERSION=Sonoma;BROWSER_STACK_KEY=<Your actual user name>;BROWSER_STACK_USER=<your actual key>;RUN_WITH_DRIVER=BROWSERSTACK;RUN_WITH_HEADLESS=NONE

#### If wanted to test in Mobile device, set following environment variables
# 1. RUN_WITH_DRIVER : set it as BROWSERSTACK_MOBILE
# 2. RUN_WITH_HEADLESS : set it as NONE
# 3. BROWSER_STACK_USER : set it as your User Name from browser stack ACCESS KEY drop down
# 4. BROWSER_STACK_KEY : set it as your Access Key from browser stack ACCESS KEY drop down
# 5. BROWSER_DEVICE_NAME : set it as your Mobile device name
# 6. BROWSER_OS_VERSION : set it to your OS version example 16 for iPhone
# 7. BROWSER_NAME : set it to your browser name example chromium for iPhone
# So it will look like something as below for iPhone:
# BROWSER_DEVICE_NAME=iPhone 14 Pro Max;BROWSER_NAME=chromium;BROWSER_OS_VERSION=16;BROWSER_STACK_KEY=<Your actual user name>;BROWSER_STACK_USER=<your actual user>;RUN_WITH_DRIVER=BROWSERSTACK_MOBILE
# Refer to this link to know what is supported by Browser stack
# https://www.browserstack.com/docs/automate/capabilities

# For Reference https://www.jetbrains.com/help/pycharm/run-debug-configuration.html


#### If wanted to emulate Mobile
# 1. RUN_WITH_DRIVER : set it as MOBILE

#### To Generate report in Allure
# run below command
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ .\features\tests\offplan_sales_status_filter.feature
# allure serve test_results/