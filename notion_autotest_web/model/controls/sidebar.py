from selene.support.shared import browser
from selene import be, by, have, command
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import sys
import time


def open_if_hidden():
    btn = browser.element('.notion-open-sidebar')
    if btn.matching(be.in_dom):
        btn.hover().click()


def press_buttons_for_close():
    modifier_key = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL
    browser.element('.notion-sidebar-switcher').send_keys(modifier_key + '\\')
    browser.element('.notion-topbar').click()


def click_by_name(name: str):
    browser.element(by.text(name)).click()


def click_hide_button_by_name(name: str, hide_btn: str = 'dots' or 'plus'):
    data_block = browser.all('.notion-outliner-private .notion-selectable').element_by(have.text(name))
    action = ActionChains(browser.driver)
    btn = '.dots' if hide_btn == 'dots' else '.plusThick'
    dots = browser.element(f'.notion-outliner-private .notion-selectable {btn}')

    action.move_to_element(data_block()).perform()
    dots.should(be.visible).click()


def call_context_by_name(name: str):
    browser.all('.notion-outliner-private .notion-selectable').element_by(have.text(name)).context_click()
