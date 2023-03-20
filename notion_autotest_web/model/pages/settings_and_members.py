import time

from selene.support.shared import browser
from selene import by, have
from selenium.webdriver import ActionChains

from notion_autotest_web.model.controls import sidebar
from notion_autotest_web.model.controls.table import Table
from selenium.webdriver.common.keys import Keys


class Members:
    def __init__(self):
        self.table = Table(browser.element('tbody'))

    def open_window(self):
        sidebar.click_by_name('Settings & members')
        return self

    def add_by_email(self, email: str):
        browser.element(by.text('Add members')).click()
        browser.element('[placeholder="Search name or emails"]').type(email)
        browser.element(by.text('Invite')).click()
        return self

    def delete(self, name: str):
        self.table.row_by_name(name).remove_member()
        return self

    def should_exist(self, name: str, exist: bool):
        if exist:
            self.table.container.should(have.text(name))
        else:
            self.table.container.should(have.no.text(name))
        return self

    def close_window(self):
        time.sleep(1)
        ActionChains(browser.driver).send_keys(Keys.ESCAPE).perform()
