# -*- coding: utf8 -*-

from setuptools import setup

from algo import __version__

setup(
    name="algo",
    version=__version__,
    author="algo@gmail.com",
    description="algo.",
    packages=["algo"],
    install_requires=[
        "flask",
    ],
    entry_points={
        "console_scripts": [
            "api=algo.app:run"
        ]
    }
)
