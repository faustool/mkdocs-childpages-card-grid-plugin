from setuptools import setup, find_packages

setup(
    name='mkdocs-childpages-card-grid',
    version='0.1.0',
    description='Card grid generator for child pages',
    long_description='A MkDocs plugin to generate a responsive card grid with all child pages',
    keywords='mkdocs',
    url='',
    author='Fausto Oliveira',
    author_email='...',
    license='Apache License, Version 2.0',
    python_requires='>=3.4',
    install_requires=[
        'mkdocs>=1.4.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3+'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'childpages-card-grid = childpages_card_grid.plugin:ChildPagesCardGridPlugin'
        ]
    }
)