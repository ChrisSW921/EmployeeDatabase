import sqlite3
from random import randint

from Backend.Employee import Employee
from Backend.EmployeeAddress import EmployeeAddress
from Backend.EmployeePermissions import EmployeePermissions
from Backend.EmployeePTO import EmployeePTO
from Backend.EmployeeCredentials import EmployeeCredentials
'''
    Database Class

    - This class will also initialize the database when first loading the application 

    Public Methods
        CurrentDataContext - Returns cursor for executing commands
        SaveChanges - Saves changes with try-catch (could handle with logs)
        Close - Void - Closes execution on current stream

'''

def initialize_employee_database(database : sqlite3.Connection, cursor : sqlite3.Cursor):
    with open('Database/EmpDataSchema.sql') as databaseFile:
        database_commands = databaseFile.read().replace('\n', ' ').split(';')

    with open('Database/EmpDataTriggers.sql') as databaseTriggers:
        database_triggers = databaseTriggers.read().replace('\n', ' ')
        print(database_triggers)

    for command in database_commands:
        cursor.execute(command)
    
    cursor.execute(database_triggers)

    database.commit()

    # Make some qualifiers to only execute if there is no data in the database
    generate_employees()

def generate_employees():
    with open('Database/employees.csv') as employeeFile:
        lineCount = 0
        for employee in employeeFile:
            if(lineCount > 0):
                employee = employee.rstrip().split(',')
                newEmpAddress = EmployeeAddress(employee[3], employee[4], employee[5], int(employee[6]))
                newEmpPermissions = EmployeePermissions(False, False, False, False)
                newEmpPTO = EmployeePTO(50, 0, 75)
                newEmpCredentials = EmployeeCredentials(None, None)
                phoneNum = generate_phone_dashes(randint(2000000000, 9999999999))
                payType = randint(1, 2)
                newEmp = Employee(employee[1], employee[2], phoneNum, float(employee[8]), float(employee[10]), float(employee[9]), payType, False, newEmpAddress, newEmpPermissions, newEmpPTO, newEmpCredentials)
                newEmp.save()

            lineCount += 1
    
def generate_phone_dashes(phoneNum : int):
    phoneStr = str(phoneNum)
    phoneStr = phoneStr[:3] + '-' + phoneStr[3:6] + '-' + phoneStr[6:10]
    return phoneStr

database = sqlite3.connect('Database/empdata.db')
cursor = database.cursor()

initialize_employee_database(database, cursor)

