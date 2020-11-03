import sys
import os
sys.path.insert(0,os.getcwd())

from Backend.employee import Employee
from Backend.employee_address import EmployeeAddress
from Backend.employee_permissions import EmployeePermissions
from Backend.employee_pto import EmployeePTO
from Backend.employee_credentials import EmployeeCredentials
from Database import database

emp = database.get_employee(2)
# Tests we should build
# -- Adding new Employee works
# -- Setting new Passwords works
# -- Verification of Passwords works
# -- Saving a new Employee works