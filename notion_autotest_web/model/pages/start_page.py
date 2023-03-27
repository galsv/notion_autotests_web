from selene.support.shared import browser
from selene import by, be
import time
import allure


def login(user_login: str, user_password: str):
    with allure.step('Open notion and click Login button'):
        browser.open('/')
        browser.element(by.text('Log in')).click()

    with allure.step('Fill email and click next button'):
        browser.element('[placeholder="Enter your email address..."]').type(user_login)
        browser.element('form > div[role="button"]').click()

    with allure.step('Fill password and click continue'):
        browser.element('[autocomplete="current-password"]').type(user_password)
        browser.element(by.text('Continue with password')).click()


def should_success_login(user_login: str):
    sidebar_switcher = browser.element('.notion-sidebar-switcher')
    sidebar_switcher.click()

    with allure.step('Should main page after login'):
        browser.element(by.text(user_login)).should(be.visible)
        sidebar_switcher.double_click()
        time.sleep(1)


def close_window_about_ai():
    if browser.element(by.text('Notion AI')).matching(be.in_dom):
        browser.element('svg.close').click()
