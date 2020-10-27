import sqlite3
import random

from Backend.employee import Employee
from Backend.employee_address import EmployeeAddress
from Backend.employee_permissions import EmployeePermissions
from Backend.employee_pto import EmployeePTO
from Backend.employee_credentials import EmployeeCredentials
from Backend.employee_timecard import EmployeeTimecard
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

    for command in database_commands:
        cursor.execute(command)
    
    cursor.execute(database_triggers)
    database.commit()

    # Make some qualifiers to only execute if there is no data in the database
    generate_employees()

def generate_employees():
    with open('Database/employees.csv') as employeeFile:
        lineCount = 0
        for emp in employeeFile:
            if(lineCount > 0):
                emp = emp.rstrip().split(',')
                newEmpAddress = EmployeeAddress(emp[3], emp[4], emp[5], int(emp[6]))
                newEmpPermissions = EmployeePermissions(False, False, False, False)
                newEmpPTO = EmployeePTO(50, 0, 75)
                newEmpCredentials = EmployeeCredentials(None, None)
                phoneNum = generate_phone_dashes(random.randint(2000000000, 9999999999))
                payType = random.randint(1, 2)
                payMethod = random.randint(1, 3)
                newEmp = Employee(emp[1], emp[2], phoneNum, float(emp[8]), float(emp[10]), float(emp[9]), payType, payMethod, False, newEmpAddress, newEmpPermissions, newEmpPTO, newEmpCredentials)
                newEmp.save()

                for timecard in generate_timecards():
                    newEmp.add_timecard(timecard)
                    
            lineCount += 1
    
def generate_phone_dashes(phoneNum : int):
    phoneStr = str(phoneNum)
    phoneStr = phoneStr[:3] + '-' + phoneStr[3:6] + '-' + phoneStr[6:10]
    return phoneStr

def generate_timecards():
    timecards = []
    numOfTimecards = random.randint(0, 12)
    while(numOfTimecards != 0):
        hours = round(random.uniform(4, 10), 2)
        timecard = EmployeeTimecard(hours)
        timecards.append(timecard)
        numOfTimecards = numOfTimecards - 1
    return timecards

database = sqlite3.connect('Database/empdata.db')
cursor = database.cursor()

initialize_employee_database(database, cursor)