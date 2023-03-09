"""Berglyd.net Theme
"""
import sphinx.application

from pathlib import Path

__version__ = "0.0.1"


def setup(app: sphinx.application.Sphinx):
    """Main theme setup.
    """
    themeRoot = Path(__file__).parent.resolve()
    print(themeRoot)
    app.add_html_theme("berglyd_theme", str(themeRoot))

    return {"version": __version__, "parallel_read_safe": True}
