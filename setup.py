from setuptools import find_packages
from typing import List


def get_requirements(file_path: str) -> List[str]:
    '''
    this function returns the requirements list
    '''


setup(
    name="ML Project",
    version="0.0.1",
    author="Pavan Sai",
    author_name="pavansai24716@gmail.com",
    packages=find_packages("requriments.txt")
)
