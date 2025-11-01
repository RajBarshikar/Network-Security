'''
The setup.py file is an essential part of packaging and distributing
python projects. It is used by setuptools (or disutils in older Python
versions) to define the configuration of your project, such as its 
metadata, dependencies and more.
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return the list of packages to be installed
    """
    requirement_lst:List[str] = [] 
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines = file.readlines()
            #Process each line
            for line in lines:
                requirement = line.strip()
                #ignore empty lines and -e.
                if requirement and requirement != '-e.':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirement_lst


setup(
    name="MLops_project",
    version="0.0.1",
    author="Raj Barshikar",
    author_email="rajlkbarshikar@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
    python_requires='>=3.7',
)



    
