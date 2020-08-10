import html.parser
import json
import re
import sys

from SzDjango import SzObject


class Route(SzObject):
    __slats__ = ()

    def __init__(self):
        super().__init__()
        self._paths = []

    def url(self, paths: list = []) -> any:
        if type(paths) == list:
            for _path in paths:
                __path = re.match('^$', _path)
                self._paths.append(__path)
        return self._paths

    def _parse_path(self, _path: str = ''):
        return html.parser.HTMLParser(_path)
