from notion_autotest_web.data.page import trash_page
from .pages.page import Page
from .pages.trash import Trash
from .pages.settings_and_members import Members

page = Page()
member = Members()
trash = Trash(trash_page.title)
