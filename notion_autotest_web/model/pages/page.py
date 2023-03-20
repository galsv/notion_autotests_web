import time
import sys
import os
from selene.support.shared import browser
from selene import have, be, by, query
from selenium.webdriver import Keys

from notion_autotest_web.model.controls import sidebar
from notion_autotest_web.data.page import PageContent, BlockContentType, Color
from notion_autotest_web.model.controls.content_block import ContentBlock


class Page:
    def __init__(self):
        self._title_element = browser.element('[placeholder="Untitled"]')
        self.pages = browser.all('.notion-outliner-private [data-block-id]')
        self.all_block = browser.all('.notion-page-content > .notion-selectable')
        self.content_block = ContentBlock()

    def open_by_url(self, relative_url: str):
        browser.open(relative_url)
        return self

    def create_new(self):
        sidebar.click_by_name('New page')
        browser.element('svg.openAsPageThick').click()
        return self

    def fill_title(self, value: str):
        self._title_element.type(value)
        return self

    def change_title(self, value: str):
        self._title_element.click().clear().type(value)
        return self

    def save_url(self):
        os.environ['NOTION_PAGE_URL'] = browser.get(query.url).split(browser.config.base_url)[-1]
        return self

    def select_type_content(self, content_type: PageContent):
        if content_type in PageContent:
            browser.element('.notion-page-content').element(by.text(content_type.value)).click()
        else:
            raise TypeError('content_type must be an instance of PageContent Enum')
        return self

    def fill_content_block(self, contents: list):
        time.sleep(1)
        for content in contents:
            self.content_block.click_button_left()
            self.content_block.select_type_by_name(content[0])
            if content[0] in [BlockContentType.Text, BlockContentType.TODO]:
                self.content_block.fill_text(content[1])
            if content[0] is BlockContentType.Image:
                self.content_block.upload_picture_by_file(content[1])
            if content[0] is BlockContentType.Embed:
                self.content_block.upload_file_by_link(content[1])
        return self

    def change_colour_in_text_block(self, block_number: int, color: Color, background=False):
        text_block = self.all_block[block_number-1]
        text_color = f'background{color.name}' if background else color.name
        text_style = color.value[1] if background else color.value[0]

        self.content_block.change_text_color(text_block, text_color)\
            .should_text_color(text_block, text_style)

        return self

    def delete_text_block(self, block_number: int):
        self.content_block.delete(block_number)

    def should_title(self, value):
        self._title_element.should(have.text(value))
        return self

    def should_content_blocks(self, data):
        self.all_block.wait_until(have.size_greater_than_or_equal(len(data)))

        content = self.all_block
        for count, block in enumerate(content):
            block.should(have.attribute('class').value_containing(data[count][0].block_class))
        return self

    def should_page_exist(self, page_url: str, exist: bool):
        result = any([page.element('a')
                     .matching(have.attribute('href')
                     .value_containing(page_url.lstrip('/')))
                     for page in self.pages])
        if exist:
            assert result
        else:
            assert not result
        return self

    def delete_by_name(self, name):
        sidebar.click_hide_button_by_name(name, 'dots')
        browser.all('.notion-scroller.vertical')[-1].element(by.text('Delete')).click()
        time.sleep(1)
        return self
