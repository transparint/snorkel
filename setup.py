from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name="snorkelicious",
    version="0.6.2",
    description="a system for rapidly creating, modeling, and managing training data",
    long_description=long_description,
    url='https://github.com/transparint/snorkel',
    author="Nom de Plume",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Machine Learning',
        'License :: Apache 2.0',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        # ??? python 3 ???
        ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        'bs4',
        'future',
        'futures',
        'ipywidgets>=7.0',
        'jupyter',
        'lxml>=3.6.4',
        'matplotlib',
        'nltk',
        'numba',
        'git://github.com/transparint/numbskull@master',
        'numpy>=1.11',
        'pandas',
        'requests',
        'scipy>=0.18',
        'six',
        'sqlalchemy>=1.0.14',
        'tensorflow>=1.0',
        'tika',
        'spacy==1.10.0',
        'psycopg2',
        'py4j',
        'treedlib',
        ],
)