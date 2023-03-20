from notion_autotest_web.model import app
from notion_autotest_web.data.page import PageContent
from notion_autotest_web.data.page import trash_page
import os


def test_page_in_trash_after_delete():
    (
        app.page.create_new()
        .save_url()
        .fill_title(trash_page.title)
        .select_type_content(PageContent.EmptyPage)
        .fill_content_block(trash_page.content_block)
        .delete_by_name(trash_page.title)
        .should_page_exist(os.getenv('NOTION_PAGE_URL'), False)
    )

    app.trash.wait_page_in_trash().should_page_in_trash()


def test_restore_page():
    (
        app.trash.open_menu()
        .should_page_in_trash()
        .restore_page()
        .open_menu()
        .should_page_in_trash(should=False)
        .close_menu()
    )

    app.page.should_page_exist(os.getenv('NOTION_PAGE_URL'), True)


def test_delete_page_permanently():
    app.page.delete_by_name(trash_page.title)

    app.trash.wait_page_in_trash().should_page_in_trash()
    app.trash.delete_page_permanently()
    app.trash.should_page_in_trash(should=False)
    app.trash.close_menu()
