from Employee import Employee
from EmployeeAddress import EmployeeAddress
from EmployeePermissions import EmployeePermissions
from EmployeePTO import EmployeePTO

newEmployeeAddress = EmployeeAddress('1234 W 123 S', 'Test', 'YT', 83133)
newEmployeePermissions = EmployeePermissions(False, False, False, False)
newEmployeePTO = EmployeePTO(50, 10, 100)
newEmployee = Employee('Carson', 'Stromberg', 8015544967, 80450.40, 00.00, 00.00, 1, newEmployeeAddress, newEmployeePermissions, newEmployeePTO)

print(newEmployee)

