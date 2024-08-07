from setuptools import setup, find_packages
import pathlib

def get_Requirements(reqFile):
        requirements=[]
        with open(reqFile) as file_obj:
            requirements=file_obj.readlines()
            requirements=[req.replace("\n","") for req in requirements]

            if "" in requirements:
                requirements.remove("")
        
        return requirements

setup(
    name="BMIPROJECT",
    version="0.3",
    author="Siddharth Sehgal",
    packages=find_packages(),
    install_requires=get_Requirements('requirements.txt')
) 



