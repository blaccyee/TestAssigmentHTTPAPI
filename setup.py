"""
This is a setup file for HTTP API application
"""

from setuptools import setup

setup(
    name='test-app',
    version='0.0.1',
    author='K K',
    description='HTTP app created wit FastApi',
    install_requires=[
        'fastapi~=0.85.1',
        'pydantic~=1.10.2',
        'starlette~=0.20.4',
        'SQLAlchemy~=1.4.42',
        'uvicorn~=0.19.0',
        'setuptools~=57.0.0',
        'pytest~=7.2.0'
    ],
    scripts=['app/main.py', 'scripts/create_db.py']
)
