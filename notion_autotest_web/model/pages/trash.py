import time
import allure
from notion_autotest_web.model.controls import sidebar
from selene.support.shared import browser
from selene import be, have, by


class Trash:
    def __init__(self, page_name: str):
        self.pages = browser.all('.notion-sidebar-trash-menu > .notion-scroller.vertical .notranslate')
        self.open = browser.element('.notion-sidebar-trash-menu')
        self.page_name = page_name

    def open_menu(self):
        with allure.step('Open trash menu'):
            if self.open.matching(be.not_.in_dom):
                sidebar.click_by_name('Trash')
        return self

    def close_menu(self):
        with allure.step('Close trash menu'):
            if self.open.matching(be.in_dom):
                browser.element('.notion-sidebar').element(by.text('Trash')).double_click()
        return self

    def page_by_name(self):
        for page in self.pages:
            if page.matching(have.text(self.page_name)):
                return page
        return None

    def restore_page(self):
        with allure.step('Restore page'):
            self.page_by_name().element('svg.undo').click()
        return self

    def delete_page_permanently(self):
        with allure.step('Delete page permanently'):
            self.page_by_name().element('svg.trash').click()
            browser.element(by.text('Yes. Delete this page')).click()
        return self

    def should_page_in_trash(self, should=True):
        with allure.step('Should page in trash'):
            self.pages.wait_until(have.size_greater_than(0))

            text_should = self.page_by_name()

            if should:
                assert text_should
            else:
                assert not text_should
        return self

    def wait_page_in_trash(self):
        for _ in range(4):
            browser.driver.refresh()
            self.open_menu()
            self.pages.wait_until(have.size_greater_than(0))

            if self.page_by_name():
                break
            time.sleep(10)
        return self
