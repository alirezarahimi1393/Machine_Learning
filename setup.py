from setuptools import find_packages,setup
from typing import List

hyphn_e_dot ='-e .'
def get_requirments(file_path:str)->list[str]:
    '''
    this function will return the list of requirments
    '''
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readline()
        [req.replace("\n","") for req  in requirments ]
        if hyphn_e_dot in requirments:
            requirments.remove(hyphn_e_dot)
    return requirments

setup(
 name='mlproject',
 version='0.0.1',
 author='Ali Reza',
 author_email= 'alirezarahimi1393@gmail.com',
 packages=find_packages(),
 install_requires=get_requirments['requirments.txt']
)