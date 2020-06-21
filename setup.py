# -*- coding: utf8 -*-

from setuptools import setup, find_packages

from src import __version__

setup(
    name="src",
    version=__version__,
    author="src@gmail.com",
    description="src.python.hd_tensorflow",
    packages=find_packages(),
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.json', '*.xml'],
    },
    # include_package_data=True,
    install_requires=[
        "flask==1.1.2",
        "tensorflow==2.1.0",
        "numpy==1.18.2",
        "pandas==1.0.3",
        "scikit-learn==0.22.2",
        "joblib==0.14.1",
        "zc.recipe.egg==2.0.7",
        "zc.zdaemonrecipe==1.0.0",
        "pyignite==0.3.4",
        "ortools == 7.6.7691",
        'py_eureka_client==0.7.4'

    ],
    entry_points={
        "console_scripts": [
            "api=src.app:run"
        ]
    }
)
