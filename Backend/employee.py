''' 
    Employee Class

    Properties
        private string First_Name
        private string Last_Name
        private string Full_Name
        private int Phone_Number
        private int Salary
        private int Pay_Type
        private int Pay

        private EmployeeAddress Employee_Address
        private EmployeePTO Employee_PTO
        private EmployeePermissions Employee_Permissions

    Public Methods 
        - Properties will have getter and setter methods public
'''
import sys
import os
sys.path.insert(0,os.getcwd())

import hashlib
import sqlite3

from Backend.employee_address import EmployeeAddress
from Backend.employee_pto import EmployeePTO
from Backend.employee_permissions import EmployeePermissions
from Backend.employee_credentials import EmployeeCredentials
from Backend.employee_timecard import EmployeeTimecard
from Backend.employee_receipt import EmployeeReceipt

class Employee:
    def __init__(self, firstName : str, lastName : str, phoneNumber : str, salary : float, hourly : float, commission : float, payType : int, payMethod : int, archived : bool, address : EmployeeAddress, permissions : EmployeePermissions, pto : EmployeePTO, credentials : EmployeeCredentials):
        self.EmpId = None
        self.First_Name = firstName
        self.Last_Name = lastName
        self.Full_Name = self.get_full_name()
        self.Phone_Number = phoneNumber
        self.Salary = salary
        self.Hourly = hourly
        self.Commission = commission
        self.Pay_Type = payType
        self.Pay_Method = payMethod
        self.Address = address
        self.Archived = archived
        self.Permissions = permissions
        self.PTO = pto
        self.Credentials = credentials
    
    def get_full_name(self):
        return self.First_Name + " " + self.Last_Name

    def save(self):
        currentDataContext = sqlite3.connect(database_file_path())
        cursor = currentDataContext.cursor()

        if (self.EmpId != None):
            cursor.execute('UPDATE EMPLOYEES SET first_name = ?, last_name = ?, phone_number = ?, salary = ?, hourly = ?, commission = ?, pay_type = ?, pay_method = ?, archived = ? WHERE emp_id = ?', (self.First_Name, self.Last_Name, self.Phone_Number, self.Salary, self.Hourly, self.Commission, self.Pay_Type, self.Pay_Method, self.Archived, self.EmpId))

            cursor.execute('UPDATE EMPLOYEE_ADDRESS SET street_address = ?, address_city = ?, address_state = ?, address_zip = ? WHERE emp_id = ?', (self.Address.Street_Address, self.Address.City, self.Address.State, self.Address.Zip_Code, self.EmpId))
            cursor.execute('UPDATE EMPLOYEE_PERMISSIONS SET reporting_permissions = ?, accounting_permissions = ?, editing_permissions = ?, manager_permissions = ? WHERE emp_id = ?', (self.Permissions.Reporting_Permission, self.Permissions.Accounting_Permission, self.Permissions.Editing_Permission, self.Permissions.Manager_Permission, self.EmpId))
            cursor.execute('UPDATE EMPLOYEE_PTO SET current_pto = ?, used_pto = ?, pto_limit = ? WHERE emp_id = ?', (self.PTO.Current_PTO, self.PTO.Used_PTO, self.PTO.PTO_Limit, self.EmpId))
        else:
            cursor.execute('INSERT INTO EMPLOYEES (first_name, last_name, phone_number, salary, hourly, commission, pay_type, pay_method, archived) VALUES (?,?,?,?,?,?,?,?,?)', (self.First_Name, self.Last_Name, self.Phone_Number, self.Salary, self.Hourly, self.Commission, self.Pay_Type, self.Pay_Method, self.Archived))
            self.EmpId = int(cursor.lastrowid)
            
            cursor.execute('UPDATE EMPLOYEE_ADDRESS SET street_address = ?, address_city = ?, address_state = ?, address_zip = ? WHERE emp_id = ?', (self.Address.Street_Address, self.Address.City, self.Address.State, self.Address.Zip_Code, self.EmpId))
            cursor.execute('UPDATE EMPLOYEE_PERMISSIONS SET reporting_permissions = ?, accounting_permissions = ?, editing_permissions = ?, manager_permissions = ? WHERE emp_id = ?', (self.Permissions.Reporting_Permission, self.Permissions.Accounting_Permission, self.Permissions.Editing_Permission, self.Permissions.Manager_Permission, self.EmpId))
            cursor.execute('UPDATE EMPLOYEE_PTO SET current_pto = ?, used_pto = ?, pto_limit = ? WHERE emp_id = ?', (self.PTO.Current_PTO, self.PTO.Used_PTO, self.PTO.PTO_Limit, self.EmpId))

        currentDataContext.commit()
        currentDataContext.close()

    def add_timecard(self, timecard : EmployeeTimecard):
        currentDataContext = sqlite3.connect(database_file_path())
        cursor = currentDataContext.cursor()

        cursor.execute('INSERT INTO EMPLOYEE_TIMECARDS VALUES (?,?)', (self.EmpId, timecard.Hours))

        currentDataContext.commit()
        currentDataContext.close()

    def add_receipt(self, receipt : EmployeeReceipt):
        currentDataContext = sqlite3.connect(database_file_path())
        cursor = currentDataContext.cursor()

        cursor.execute('INSERT INTO EMPLOYEE_RECEIPTS VALUES (?,?)', (self.EmpId, receipt.Receipt))

        currentDataContext.commit()
        currentDataContext.close()

    def set_password(self, password : str):
        currentDataContext = sqlite3.connect(database_file_path())
        cursor = currentDataContext.cursor()

        salt = os.urandom(32)
        hashedPassword = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 1000)

        cursor.execute('UPDATE EMPLOYEE_CREDENTIALS SET emp_password = ?, emp_password_salt = ? WHERE emp_id = ?', (hashedPassword, salt, self.EmpId))

        currentDataContext.commit()
        currentDataContext.close()

    def set_social_security(self, social : str):
        # The number passed into this function needs to be a 9-digit integer casted to a string... We should do parsing on the front end
        currentDataContext = sqlite3.connect(database_file_path())
        cursor = currentDataContext.cursor()
        initialSocial = social[:5]
        lastSocial = social[5:9]
        salt = os.urandom(32)
        hashedSocial = hashlib.pbkdf2_hmac('sha256', initialSocial.encode('utf-8'), salt, 1000)

        cursor.execute('UPDATE EMPLOYEE_CREDENTIALS SET emp_social_inital = ?, emp_social_salt = ?, emp_social_last = ? WHERE emp_id = ?', (hashedSocial, salt, lastSocial, self.EmpId))
        
        currentDataContext.commit()
        currentDataContext.close()

def database_file_path():
    filePath = os.path.dirname(os.path.realpath(__file__))
    parentDir = os.path.abspath(os.path.join(filePath, '..'))
    if sys.platform == 'win32':
        return parentDir + '\Database\empdata.db'
    else:
        return parentDir + '/Database/empdata.db'
