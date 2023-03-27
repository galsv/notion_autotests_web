import os
import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from notion_autotest_web.model.pages import start_page
from dotenv import load_dotenv
from notion_autotest_web.utils import attach


DEFAULT_BROWSER_VERSION = "100.0"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def browser_management(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser.config.driver = driver

    browser.config.timeout = 6
    browser.config.base_url = 'https://www.notion.so'
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    load_dotenv()

    user_login = os.getenv('NOTION_LOGIN')
    user_password = os.getenv('NOTION_PASSWORD')
    start_page.login(user_login, user_password)
    start_page.should_success_login(user_login)

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()
