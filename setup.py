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
        '': ['*.json', '*.xml', '*.ini'],
    },
    # include_package_data=True,
    install_requires=[
        "flask==1.1.2",
        "tensorflow==2.1.2",
        "numpy==1.18.2",
        "pandas==1.0.3",
        "scikit-learn==0.22.2",
        "joblib==0.14.1",
        "zc.recipe.egg==2.0.7",
        "zc.zdaemonrecipe==1.0.0",
        "pyignite==0.3.4",
        "ortools == 7.6.7691",
        'py_eureka_client==0.7.4',
        'python-logstash-async==1.6.6',
        'loguru==0.5.1',
        'flask-admin==1.5.6',
        'flask-SQLAlchemy==2.4.3',
        'Flask-Migrate==2.5.3',
        'Flask-script==2.0.6',
        'flask-babelex==0.9.4',
        'pylint==2.5.3',
        'plotly==4.8.2',

    ],
    entry_points={
        "console_scripts": [
            "api=src.app:run"
        ]
    }
)
