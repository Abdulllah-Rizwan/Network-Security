from setuptools import find_packages,setup
from typing import List


def get_requirements() -> List[str]:

    requirements_list: List[str] = []

    try:
        with open('requirements.txt','r') as f:
            lines = f.readlines()

            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirements_list.append(requirement)
        
        return requirements_list

    except FileNotFoundError:
        print('requirements.txt file is not found')


setup(
    name='Network Security',
    author='Abdullah Rizwan',
    version='0.0.1',
    author_email='abdullahrizwan354@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()

)