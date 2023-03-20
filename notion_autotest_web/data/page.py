from enum import Enum
from dataclasses import dataclass
from typing import List, Tuple


class PageContent(Enum):
    EmptyPage = 'Empty page'


class BlockContentType(Enum):
    Text = 'text'
    TODO = 'todo'
    Image = 'image'
    Embed = 'embed'

    @property
    def block_class(self):
        if self.value == 'todo':
            return 'notion-to_do-block'
        if self.value == 'text':
            return 'notion-text-block'
        if self.value == 'image':
            return 'notion-image-block'
        if self.value == 'embed':
            return 'notion-embed-block'


class Color(Enum):
    Yellow = ('color: rgb(203, 145, 47);', 'background: rgb(251, 243, 219);')


@dataclass
class Page:
    title: str
    content_block: List[Tuple[BlockContentType, str]]


trash_page = Page('Trash Page', [(BlockContentType.Text, 'test')])
empty_page = Page('Empty Page', [])
empty_page_another_title = Page('Another Tittle', [])
content_page = Page('Content Page',
                    [
                        (BlockContentType.Text, 'test1'),
                        (BlockContentType.Text, 'test2'),
                        (BlockContentType.TODO, 'test_todo5'),
                        (BlockContentType.Embed,
                         'https://fs-thb03.getcourse.ru/fileservice/file/thumbnail/h/b635b6cb9478bb87c77e9c070ee6e122.png/s/x50/a/159627/sc/207'),

                    ])
