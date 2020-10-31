import sqlite3
import random
import string
import hashlib
import sys
import os
sys.path.insert(0,os.getcwd())

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

    numOfRows = cursor.execute('SELECT COUNT(*) FROM EMPLOYEES').fetchone()[0]
    if(numOfRows <= 0):
        generate_employees()

def generate_employees():
    adminAddress = EmployeeAddress(None, None, None, None)
    adminPermissions = EmployeePermissions(True, True, True, True)
    adminPTO = EmployeePTO(50, 0, 100)
    adminCredentials = EmployeeCredentials(None, None)
    admin = Employee("System", "Admin", None, None, None, None, None, None, False, adminAddress, adminPermissions, adminPTO, adminCredentials)
    admin.save()
    admin.set_password('admin')

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
                payMethod = int(emp[7])
                newEmp = Employee(emp[1], emp[2], phoneNum, float(emp[8]), float(emp[10]), float(emp[9]), payType, payMethod, False, newEmpAddress, newEmpPermissions, newEmpPTO, newEmpCredentials)
                newEmp.save()

                for timecard in generate_timecards():
                    newEmp.add_timecard(timecard)

                tempPassword = ''.join(random.choice(string.ascii_letters) for i in range(8))
                newEmp.set_password(tempPassword)
                    
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

def verify_credentials(empId : int, password : str):
    currentDataContext = sqlite3.connect('Database/empdata.db')
    cursor = currentDataContext.cursor()

    currentEmpPassword = cursor.execute('SELECT emp_password, emp_password_salt FROM EMPLOYEE_CREDENTIALS WHERE emp_id=?', (empId,)).fetchone()
    comparedPassword = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), currentEmpPassword[1], 1000)

    currentDataContext.close()

    return currentEmpPassword[0] == comparedPassword

def get_employee(empId : int):
    currentDataContext = sqlite3.connect('Database/empdata.db')
    cursor = currentDataContext.cursor()
    query = '''
        SELECT * FROM EMPLOYEES LEFT JOIN EMPLOYEE_ADDRESS ON EMPLOYEE_ADDRESS.emp_id = EMPLOYEES.emp_id 
        LEFT JOIN EMPLOYEE_PERMISSIONS ON EMPLOYEE_PERMISSIONS.emp_id = EMPLOYEES.emp_id
        LEFT JOIN EMPLOYEE_PTO ON EMPLOYEE_PTO.emp_id = EMPLOYEE_PTO.emp_id
        LEFT JOIN EMPLOYEE_CREDENTIALS ON EMPLOYEE_CREDENTIALS.emp_id = EMPLOYEES.emp_id
        WHERE EMPLOYEES.emp_id=?
    '''
    
    empData = cursor.execute(query, (empId,)).fetchone()
    empAddress = EmployeeAddress(empData[10], empData[11], empData[12], empData[13])
    empPermissions = EmployeePermissions(empData[15], empData[16], empData[17], empData[18])
    empPto = EmployeePTO(empData[20], empData[21], empData[22])
    empCredentials = EmployeeCredentials(empData[24], empData[26])
    employee = Employee(empData[1], empData[2], empData[3], empData[4], empData[5], empData[6], empData[7], empData[8], False, empAddress, empPermissions, empPto, empCredentials)
    employee.EmpId = empData[0]

    currentDataContext.close()

    return employee

def search_employees(searchParam : str):
    currentDataContext = sqlite3.connect('Database/empdata.db')
    cursor = currentDataContext.cursor()
    employeeList = []

    if (searchParam.isdigit()):
        empId = int(searchParam)
        employee = get_employee(empId)
        employeeList.append(employee)

    else:
        query = '''
            SELECT DISTINCT * FROM EMPLOYEES 
            WHERE EMPLOYEES.first_name = ?
        '''

        for emp in cursor.execute(query, (searchParam,)):
            employeeList.append(emp)

    currentDataContext.close()
    
    return employeeList

database = sqlite3.connect('Database/empdata.db')
cursor = database.cursor()

initialize_employee_database(database, cursor)

cursor.close()
