import os
from setuptools import find_packages, setup

# --------------------
# Setup
# --------------------

def read_file(fname):
    "Read a local file"
    return open(file=os.path.join(os.path.dirname(__file__), fname), encoding="utf-8").read()

setup(
    name='mkdocs-childpages-card-grid-plugin',
    version=read_file('VERSION').strip(),
    description='Create card grids with links to child pages on your MkDocs site',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    keywords=["mkdocs", "plugin", "python", "child-pages", "card-grid"],
    url='https://github.com/faustool/mkdocs-childpages-card-grid-plugin',
    author='Fausto Oliveira',
    license='Apache License, Version 2.0',
    python_requires='>=3.7',
    install_requires=[
        'mkdocs>=1.4.0',
        "mkdocs-material>=8.5.0"
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3'
    ],
    include_package_data=True,
    packages=find_packages(exclude=['test']),
    entry_points={
        'mkdocs.plugins': [
            'childpages-card-grid = childpages_card_grid.plugin:ChildPagesCardGridPlugin'
        ]
    }
)
