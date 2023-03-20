import os
import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from notion_autotest_web.model.pages import start_page
from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse=True)
def browser_management():
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

    browser.quit()
