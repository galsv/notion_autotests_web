from selene.support.shared import browser
from selene import by, be
import time


def login(user_login: str, user_password: str):
    browser.open('/')
    browser.element(by.text('Log in')).click()

    browser.element('[placeholder="Enter your email address..."]').type(user_login)
    browser.element('form > div[role="button"]').click()

    browser.element('[autocomplete="current-password"]').type(user_password)
    browser.element(by.text('Continue with password')).click()


def should_success_login(user_login: str):
    sidebar_switcher = browser.element('.notion-sidebar-switcher')
    sidebar_switcher.click()

    browser.element(by.text(user_login)).should(be.visible)
    sidebar_switcher.double_click()
    time.sleep(1)


def close_window_about_ai():
    if browser.element(by.text('Notion AI')).matching(be.in_dom):
        browser.element('svg.close').click()
