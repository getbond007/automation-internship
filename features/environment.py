from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
import os

def browser_init(context):

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
    browser_init(context)

def before_step(context, step):
    print('\nStarted step: ', step)

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)

def after_scenario(context, feature):
    context.driver.quit()