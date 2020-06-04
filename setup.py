from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='PyGAMP',
    packages=['PyGAMP'],
    version='0.11',
    license='MIT',
    description='PyGAMP is a Python package for Google Analytics Measurement Protocol',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Matt Clarke',
    author_email='matt@flyandlure.org',
    url='https://github.com/flyandlure/pygamp',
    download_url='https://github.com/flyandlure/pygamp/archive/master.zip',
    keywords=['python', 'google analytics', 'ga', 'measurement protocol', 'universal analytics'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
)
