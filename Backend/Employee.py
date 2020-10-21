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
from EmployeeAddress import EmployeeAddress
from EmployeePermissions import EmployeePermissions
from EmployeePTO import EmployeePTO

class Employee:
    def __init__(self, firstName : str, lastName : str, phoneNumber : int, salary : float, hourly : float, commission : float, payType : int, address : EmployeeAddress, permissions : EmployeePermissions, pto : EmployeePTO):
        self.First_Name = firstName
        self.Last_Name = lastName
        self.Full_Name = self.get_full_name()
        self.Phone_Number = phoneNumber
        self.Salary = salary
        self.Hourly = hourly
        self.Commission = commission
        self.Pay_Type = payType
        self.Address = address
        self.Permissions = permissions
        self.PTO = pto
    
    def get_full_name(self):
        return self.First_Name + " " + self.Last_Name
