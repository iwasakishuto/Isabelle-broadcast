# coding: utf-8
import os
import setuptools

DESCRIPTION = "Make shell life fun by Isabelle's broadcasting."

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()
with open("requirements.txt", mode="r") as f:
    INSTALL_REQUIRES = [line.rstrip("\n") for line in f.readlines() if line[0]!=("#")]

def setup_package():
    metadata = dict(
        name="Isabelle-broadcast",
        version="0.0.0",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        author="Shuto Iwasaki",
        author_email="cabernet.rock@gmail.com",
        project_urls={
            "Bug Reports" : "https://github.com/iwasakishuto/Isabelle-broadcast/issues",
            "Source Code" : "https://github.com/iwasakishuto/Isabelle-broadcast",
            "Say Thanks!" : "https://twitter.com/cabernet_rock",
        },
        python_requires=">=3.7",
        install_requires=INSTALL_REQUIRES,
        entry_points = {
            "console_scripts": [
                "isacast=cli:isacast",
        ],
    },
    )
    setuptools.setup(**metadata)

if __name__ == "__main__":
    setup_package()