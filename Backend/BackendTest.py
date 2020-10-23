from Backend.Employee import Employee
from Backend.EmployeeAddress import EmployeeAddress
from Backend.EmployeePermissions import EmployeePermissions
from Backend.EmployeePTO import EmployeePTO
from Backend.EmployeeCredentials import EmployeeCredentials

newEmployeeAddress = EmployeeAddress('1234 W 123 S', 'Test', 'YT', 83133)
newEmployeePermissions = EmployeePermissions(False, False, False, False)
newEmployeePTO = EmployeePTO(50, 10, 100)
newEmployeeCrednetials = (None, None)
newEmployee = Employee('Carson', 'Stromberg', '801-554-4967', 80450.40, 00.00, 00.00, 1, False, newEmployeeAddress, newEmployeePermissions, newEmployeePTO, newEmployeeCrednetials)

