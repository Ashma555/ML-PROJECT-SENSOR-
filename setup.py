from setuptools import find_packages,setup
#from typing import list
from typing import List


def get_requirements()->List[str]:

    requirements_list : List[str] =[]

    return requirements_list


setup(
    name="SENSOR",
    version="0.0.1",
    author="Ashma555",
    author_email="ashmasky786@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(),


)