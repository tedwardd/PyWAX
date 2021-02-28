import pathlib
from setuptools import setup, find_packages


HERE = pathlib.Path(__file__).parent
PACKAGE_NAME = "PyWAX"
AUTHOR = "Ted Wood"
URL = "https://github.com/tedwardd/PyWAX"
LICENSE = "Apache 2.0"
DESCRIPTION = "Python library for interacting with the WAX blockchain"
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"
INSTALL_REQUIRES = [
    "datetime",
    "inspect",
    "json",
    "requests",
]
setup(
    name=PACKAGE_NAME,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    license=LICENSE,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
)
