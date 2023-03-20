from pathlib import Path
from notion_autotest_web import resources


def to_resource(relative_path):
    return str(Path(resources.__file__).parent.joinpath(relative_path).absolute())
