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
import sqlite3
from Backend.employee_address import EmployeeAddress
from Backend.employee_pto import EmployeePTO
from Backend.employee_permissions import EmployeePermissions
from Backend.employee_credentials import EmployeeCredentials

class Employee:
    def __init__(self, firstName : str, lastName : str, phoneNumber : str, salary : float, hourly : float, commission : float, payType : int, payMethod : int, archived : bool, address : EmployeeAddress, permissions : EmployeePermissions, pto : EmployeePTO, credentials : EmployeeCredentials):
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
        currentDataContext = sqlite3.connect('Database/empdata.db')
        cursor = currentDataContext.cursor()

        cursor.execute('INSERT INTO EMPLOYEES (first_name, last_name, phone_number, pay_method, salary, hourly, commission, archived) VALUES (?,?,?,?,?,?,?,?)', (self.First_Name, self.Last_Name, self.Phone_Number, self.Pay_Type, self.Salary, self.Hourly, self.Commission, self.Archived))
        currentEmpId = int(cursor.lastrowid)
        
        cursor.execute('UPDATE EMPLOYEE_ADDRESS SET street_address = ?, address_city = ?, address_state = ?, address_zip = ? WHERE emp_id = ?', (self.Address.Street_Address, self.Address.City, self.Address.State, self.Address.Zip_Code, currentEmpId))
        cursor.execute('UPDATE EMPLOYEE_PERMISSIONS SET reporting_permissions = ?, accounting_permissions = ?, editing_permissions = ?, manager_permissions = ? WHERE emp_id = ?', (self.Permissions.Reporting_Permission, self.Permissions.Accounting_Permission, self.Permissions.Editing_Permission, self.Permissions.Manager_Permission, currentEmpId))
        cursor.execute('UPDATE EMPLOYEE_PTO SET current_pto = ?, used_pto = ?, pto_remaining = ? WHERE emp_id = ?', (self.PTO.Current_PTO, self.PTO.Used_PTO, self.PTO.PTO_Limit, currentEmpId))

        currentDataContext.commit()
        currentDataContext.close()