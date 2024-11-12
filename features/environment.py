from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
import os

#def browser_init(context):
def browser_init(context, scenario_name):

    # Set below environment variables
    RUN_WITH_DRIVER = os.getenv("RUN_WITH_DRIVER")
    RUN_WITH_HEADLESS = os.getenv("RUN_WITH_HEADLESS")

    if RUN_WITH_DRIVER == 'CHROME' :
        driver_path = ChromeDriverManager().install()
        service = Service(driver_path)
        context.driver = webdriver.Chrome(service=service)
    elif RUN_WITH_DRIVER == 'FIREFOX' :
        driver_path = GeckoDriverManager().install()
        service = Service(driver_path)
        context.driver = webdriver.Firefox(service=service)
    elif RUN_WITH_DRIVER == 'BROWSERSTACK':
        ### BROWSERSTACK ###
        # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
        bs_user = os.getenv("BROWSER_STACK_USER")
        bs_key = os.getenv("BROWSER_STACK_KEY")
        bs_os = os.getenv("BROWSER_OS")
        bs_os_version = os.getenv("BROWSER_OS_VERSION")
        bs_browser_name = os.getenv("BROWSER_NAME")

        url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
        # Set Options
        options = Options()
        bstack_options = {
            "os": bs_os,
            "osVersion": bs_os_version,
            "browserName": bs_browser_name,
            "sessionName": scenario_name,
        }
        options.set_capability('bstack:options', bstack_options)
        context.driver = webdriver.Remote(command_executor=url, options=options)
    else:
        raise Exception("Please set environment variable 'RUN_WITH_DRIVER' to either 'CHROME' or 'FIREFOX' " +
                        'refer to instructions in feature file or README file for more details.')
    

    ### HEADLESS MODE ####
    if RUN_WITH_HEADLESS == 'HEADLESS CHROME' :
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        service = Service(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(
            options=options,
            service=service
        )
    elif RUN_WITH_HEADLESS == 'HEADLESS FIREFOX':
        options = webdriver.FirefoxOptions()
        options.add_argument('headless')
        service = Service(GeckoDriverManager().install())
        context.driver = webdriver.Firefox(
            options=options,
            service=service
        )
    else:
        print('Running program without Headless as no option provided, ' +
              'if you want to run with headless refer to instruction in test feature or README file.')

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=15)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    #browser_init(context)
    browser_init(context, scenario.name)

def before_step(context, step):
    print('\nStarted step: ', step)

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)

def after_scenario(context, feature):
    context.driver.quit()