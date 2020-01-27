""" CMGTest """
import setuptools

setuptools.setup(
    name='cmgtest',
    version='0.0.1',
    description=__doc__,
    install_requires=[
        'Flask',
        'Click',
        'Flask-WTF',
        'WTForms'
    ],
    packages=setuptools.find_packages())
