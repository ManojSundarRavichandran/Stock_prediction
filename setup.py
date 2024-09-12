import setuptools
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirments 
    '''
    requirements=[]
    with open(file_path) as file:
        requirements=file.readlines()
        requirements=[req.replace('\n','')for req in requirements] 
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
setup(
 name='Stock_prediction_deustchebank',
 version='0.0.1',
 author='manoj_sundar_ravichandran',
 author_email='manojsundar187@gmail.com',
 packages=find_packages(),   # check how many files have __init__.py file 
 install_requires=get_requirements('requirement.txt')
)
   
