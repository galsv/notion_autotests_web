import time
import pyperclip
from selene.support.shared import browser
from selene import have, by, be, command, Element
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from notion_autotest_web.data.page import BlockContentType
from selenium.webdriver.common.action_chains import ActionChains
from notion_autotest_web.utils.path import to_resource


class ContentBlock:
    def __init__(self):
        self.wait_command_block = browser.element(by.text('Type \'/\' for commands'))
        self._last_element_in_block = browser.all('.notion-page-content .notion-selectable')[-1]

    def fill_text(self, value: str):
        self._last_element_in_block.type(value)
        time.sleep(0.5)
        return self

    def upload_picture_by_file(self, file_name: str):
        """
        Not recommend use if didn't block file upload window
        """
        browser.element(by.text('Upload file')).click()
        browser.element('input').send_keys(to_resource(file_name))
        time.sleep(5)
        return self

    def upload_file_by_link(self, link: str):
        browser.element('input[type="url"]').send_keys(link)
        browser.all(by.text('Embed link'))[-1].click()
        time.sleep(5)
        return self

    def select_type_by_name(self, name: BlockContentType):
        self._last_element_in_block.type(f'/{name.value}')
        browser.all('.notion-scroller.vertical')[-1].all('[role="button"]').first.click()
        return self

    def press_enter(self):
        self._last_element_in_block.press_enter()
        if self._last_element_in_block.matching(have.css_class('notion-to_do-block')):
            self._last_element_in_block.press(Keys.BACKSPACE)
        if self._last_element_in_block.matching(have.css_class('notion-embed-block')):
            self.click_plus()
        return self

    def click_button_left(self, button='plus', element=None):
        element_block = self._last_element_in_block if element is None else element
        action = ActionChains(browser.driver)
        plus = browser.element(f'.notion-frame .{button}')

        action.move_to_element(element_block()).perform()
        plus.should(be.visible).click()
        return self

    def change_text_color(self, block: Element, color: str):
        self.click_button_left('dragHandle', block)
        browser.element('input[placeholder="Search actions…"]').send_keys(color)
        time.sleep(0.5)
        browser.all('.notion-scroller.vertical')[-1].all('[role="button"]').first.click()
        return self

    def should_text_color(self, block: Element, rgb: str):
        block.element('div[style]').should(have.attribute('style').value_containing(rgb))
        return self

    def delete(self, block_number: int):
        browser.all('.notion-page-content > .notion-selectable')[block_number-1]\
               .click().clear().press(Keys.BACKSPACE)
        return self
