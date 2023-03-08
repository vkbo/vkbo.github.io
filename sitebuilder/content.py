"""
Website Builder :: Content
"""

import docutils.core

from pathlib import Path


class SiteContent:

    def __init__(self, content: Path):

        self._content = content
        self._index = content / "index.rst"

        return

    def build(self):
        index = Page(self._index).parts
        print(index)
        return

# END Class SiteContent


class Page:

    def __init__(self, path: Path):

        self._path = path
        self._parts = self._parsePage()

        return

    @property
    def parts(self):
        return self._parts

    def _parsePage(self):
        """
        """
        with open(self._path, mode="r", encoding="utf-8") as inFile:
            parts = docutils.core.publish_parts(source=inFile.read(), writer_name="html")
        return parts

# END Class Page
