from notion_autotest_web.model import app
from notion_autotest_web.data.page import PageContent
from notion_autotest_web.data.page import empty_page, empty_page_another_title
import os
import allure


@allure.title('Create new page')
def test_create_page():
    (
        app.page.create_new()

        .fill_title(empty_page.title)
        .save_url()
        .select_type_content(PageContent.EmptyPage)

        .should_title(empty_page.title)
    )


@allure.title('Change title on page')
def test_change_tittle():
    (
        app.page.open_by_url(os.getenv('NOTION_PAGE_URL'))
        .change_title(empty_page_another_title.title)
        .should_title(empty_page_another_title.title)

        .change_title(empty_page.title)
        .should_title(empty_page.title)
    )


@allure.title('Delete page')
def test_delete_page():
    app.page.delete_by_name(empty_page.title)\
       .should_page_exist(os.getenv('NOTION_PAGE_URL'), False)

