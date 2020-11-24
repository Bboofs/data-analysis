from setuptools import setup, find_packages

setup(
    name='twitter-data-analysis',
    version='0.0.1',
    url='https://github.com/Bboofs/twitter-data-analysis',
    license='BSD',
    author='loogs',
    packages=find_packages(),
    install_requires=['PyQt5', 'pandas', 'sqlalchemy', 'nltk', 'numpy', 'jupyter', 'python-twitter'],
    entry_point={},
    extras_require={'dev': ['flake8']}
)
