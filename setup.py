import sys
import os
sys.path.insert(0,os.getcwd())

from setuptools import setup

setup(name='EmpDatabase',
      version='0.1',
      description='Employee Database',
      url='https://github.com/ChrisSW921/EmployeeDatabase',
      install_requires=['pandas', 'openpyxl'],
      zip_safe=False)