# working_dir/setup.py  -----------------------------------------------------------------------------------------------
from setuptools import setup


setup(name="text_analyzer", 
      version="0.0.1", 
      description="An example package for DataCamp", 
      author="John HHU", 
      author_email="john.hhu2020@gmail.com", 
      packages=["text_analyzer"], 
      install_requires=["matplotlib", 
                        "numpy==1.15.4", 
                        "pycodestyle>=2.4.0", 
                        "token_utils"])
