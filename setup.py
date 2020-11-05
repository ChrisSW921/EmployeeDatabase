import sys
import os
sys.path.insert(0,os.getcwd())

from setuptools import setup
from Database import database

setup(name='EmpDatabase',
      version='0.1',
      description='Employee Database',
      url='https://github.com/ChrisSW921/EmployeeDatabase',
      packages=['Backend', 'Database', 'Gui'],
      install_requires=['pandas'],
      zip_safe=False)

database.initialize_employee_database()