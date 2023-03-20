import os
from selene import have
from notion_autotest_web.model import app
from notion_autotest_web.data.page import content_page, PageContent, Color


def test_create_page():
    (
        app.page.create_new()
        .fill_title(content_page.title)
        .save_url()
        .select_type_content(PageContent.EmptyPage)
        .should_title(content_page.title)
    )


def test_fill_content():
    app.page.fill_content_block(content_page.content_block)\
        .should_content_blocks(content_page.content_block)


def test_change_color_test():
    app.page.change_colour_in_text_block(1, Color.Yellow, True)
    app.page.change_colour_in_text_block(1, Color.Yellow, False)


def test_delete_content():
    len_before = len(app.page.all_block)
    app.page.content_block.delete(2)
    app.page.all_block.wait_until(have.size_less_than(len_before))


def test_delete_page():
    app.page.delete_by_name(content_page.title)\
        .should_page_exist(os.getenv('NOTION_PAGE_URL'), False)
