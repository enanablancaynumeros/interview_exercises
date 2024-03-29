from setuptools import setup, find_packages
from codecs import open
from os import path

current_directory = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(current_directory, "DESCRIPTION.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="OpenWeatherForecast",
    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version="0.2.3",
    description=long_description,
    long_description=long_description,
    url="https://github.com/enanablancaynumeros/weather_forecast",
    author="Yeray Alvarez Romero",
    author_email="yeray.alvarez.romero@gmail.com",
    license="MIT",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Office/Business :: Financial",
        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    # What does your project relate to?
    keywords="forecast, weather, prediction",
    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=["requests"],
    tests_require=["nose", "coveralls"],
    test_suite="nose.collector",
)
