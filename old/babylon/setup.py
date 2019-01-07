from setuptools import setup, find_packages


setup(
    name="babylon",
    version="0.1.0",
    author="Yeray Alvarez Romero",
    include_package_data=True,
    packages=find_packages(exclude=["docs", "tests*"]),
)
