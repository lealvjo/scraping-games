from os.path import abspath, dirname, join

from setuptools import find_packages, setup

ROOT = dirname(abspath(__file__))


def get_extra_requires(path):
    extra_deps = []
    with open(path) as fp:
        for p in fp.readlines():
            extra_deps.append(p.replace("\n", ""))
    return extra_deps


setup(
    name='games_store',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/lealvjo/scraping_games',
    license='',
    author='lealvjo',
    author_email='leonardo.jose.barros@hotmail.com',
    description='Application Programming Interface (API) - web scraping on playstationstore promotions and returns a new json object for testing',
    platforms='any',
    install_requires=get_extra_requires(join(ROOT, "requirements.txt")),
    entry_points={
        "console_scripts": [
            "games_store_run=src.main:main"
        ]},
    package_data={'': [join(ROOT, 'src/scraping/controller/schema/game_data_schema.json')]}
)
