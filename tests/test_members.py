import time

from notion_autotest_web.model import app
from notion_autotest_web.data.members import user


def test_add_member():
    (
        app.member.open_window()

        .add_by_email(user.email)
        .should_exist(user.name, True)

        .close_window()
    )


def test_delete_member():
    (
        app.member.open_window()

        .delete(user.name)
        .should_exist(user.name, False)

        .close_window()
    )
