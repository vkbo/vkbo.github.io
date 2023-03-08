"""
Website Builder :: Init
"""

import shutil

from pathlib import Path

from .content import SiteContent


def makeClean():
    """Delete old site files.
    """
    print("")
    print("Running: Make Clean")
    print("===================")
    print("")

    outDir = Path("_html")
    bldDir = Path("_build")
    if outDir.is_dir():
        print(f"Deleting: {outDir}")
        shutil.rmtree(outDir)
    if bldDir.is_dir():
        print(f"Deleting: {bldDir}")
        shutil.rmtree(bldDir)

    print("Done!")
    print("")

    return


def makeHTML():
    """Build the website project
    """
    print("")
    print("Running: Make Build")
    print("===================")
    print("")

    outDir = Path("_html")
    bldDir = Path("_build")
    outDir.mkdir(exist_ok=True)
    bldDir.mkdir(exist_ok=True)

    content = SiteContent(Path("content"))
    content.build()

    print("Done!")
    print("")

    return


def main(sysArgs):
    """The main entry script for the site builder.
    """
    if "clean" in sysArgs:
        makeClean()
    if "html" in sysArgs:
        makeHTML()
    return 0
