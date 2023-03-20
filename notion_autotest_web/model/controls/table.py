from selene import Element
from selene import by, have
from selene.support.shared import browser


class Cell:
    def __init__(self, element: Element):
        self.element = element
        self.input = self.element.element('input')

    def start_editing(self):
        self.element.double_click()
        return self

    def set(self, value):
        self.input.set_value(value)
        return self

    def save(self):
        self.input.press_enter()
        return self


class Row:
    def __init__(self, container: Element):
        self.container = container
        self.cells = container.all('td')

    def cell(self, number):
        index = number - 1
        return Cell(self.cells[index])

    def remove_member(self):
        self.container.element(by.text('Workspace owner')).click()
        browser.element(by.text('Remove from workspace')).click()
        browser.element(by.text('Remove')).click()
        return self


class Table:
    def __init__(self, container: Element):
        self.container = container
        self.rows = self.container.all('tr')

    def row(self, number):
        index = number - 1
        return Row(self.rows[index])

    def row_by_name(self, name):
        return Row(self.rows.element_by(have.text(name)))

    def add(self):
        self.container.element('.table-add').click()
        return Row(self.rows[-1])
