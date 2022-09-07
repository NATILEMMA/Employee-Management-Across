from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in employee/__init__.py
from employee import __version__ as version

setup(
	name="employee",
	version=version,
	description="Employee management ",
	author="Natnael.L",
	author_email="natilemma5@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
