import os
from setuptools import setup, find_packages

# --------------------
# Initialization
# --------------------

VERSION_NUMBER = '0.7.0'

# --------------------
# Setup
# --------------------

def read_file(fname):
    "Read a local file"
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='mkdocs-childpages-card-grid-plugin',
    version=VERSION_NUMBER,
    description='Create card grids with links to child pages on your MkDocs site.',
    long_description=read_file('README.md'),
    keywords=["mkdocs", "plugin", "python", "child-pages", "card-grid"],
    url='https://github.com/faustool/mkdocs-childpages-card-grid-plugin',
    author='Fausto Oliveira',
    license='Apache License, Version 2.0',
    python_requires='>=3.5',
    install_requires=[
        'mkdocs>=1.4.0',
        "mkdocs-material>=8.5.0"
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3+'
    ],
    include_package_data=True,
    packages=find_packages(exclude=['test']),
    entry_points={
        'mkdocs.plugins': [
            'childpages-card-grid = childpages_card_grid.plugin:ChildPagesCardGridPlugin'
        ]
    }
)
