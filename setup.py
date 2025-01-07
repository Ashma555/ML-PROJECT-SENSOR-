from setuptools import find_packages,setup
#from typing import list
from typing import List


setup(
    name="SENSOR",
    version="0.0.1",
    author="Ashma555",
    author_email="ashmasky786@gmail.com",
    packages = find_packages(),
    install_requires = ["pymongo"]
    
)