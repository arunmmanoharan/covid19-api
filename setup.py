from setuptools import setup, find_packages

setup(
    name='covid_19_api',
    version='1.0.0',

    packages=find_packages(),

    install_requires=['flask-restx==0.5.1', 'Flask-SQLAlchemy==2.4.1'],
)