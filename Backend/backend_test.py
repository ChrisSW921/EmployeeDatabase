from Backend.employee import Employee
from Backend.employee_address import EmployeeAddress
from Backend.employee_permissions import EmployeePermissions
from Backend.employee_pto import EmployeePTO
from Backend.employee_credentials import EmployeeCredentials
from Database import database

newEmployeeAddress = EmployeeAddress('1234 W 123 S', 'Test', 'YT', 83133)
newEmployeePermissions = EmployeePermissions(False, False, False, False)
newEmployeePTO = EmployeePTO(50, 10, 100)
newEmployeeCrednetials = (None, None)
newEmployee = Employee('Carson', 'Stromberg', '801-554-4967', 80450.40, 00.00, 00.00, 1, 2, False, newEmployeeAddress, newEmployeePermissions, newEmployeePTO, newEmployeeCrednetials)

newEmployee.save()
newEmployee.set_password('test')

result = database.verify_credentials(newEmployee.EmpId, 'false')
print(result)