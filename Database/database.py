import sqlite3
import random
import string
import hashlib
import pandas
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

def initialize_employee_database():
    database = sqlite3.connect('Database/EmpData.db')
    cursor = database.cursor()

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
    
    database.close()

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

                socialSecurity = str(random.randint(100000000, 900000000))
                newEmp.set_social_security(socialSecurity)
                    
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
        LEFT JOIN EMPLOYEE_PTO ON EMPLOYEE_PTO.emp_id = EMPLOYEES.emp_id
        LEFT JOIN EMPLOYEE_CREDENTIALS ON EMPLOYEE_CREDENTIALS.emp_id = EMPLOYEES.emp_id
        WHERE EMPLOYEES.emp_id=?
    '''
    
    empData = cursor.execute(query, (empId,)).fetchone()
    empAddress = EmployeeAddress(empData[11], empData[12], empData[13], empData[14])
    empPermissions = EmployeePermissions(bool(empData[16]), bool(empData[17]), bool(empData[18]), bool(empData[19]))
    empPto = EmployeePTO(empData[21], empData[22], empData[23])
    empCredentials = EmployeeCredentials(empData[25], empData[29])
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
            WHERE EMPLOYEES.first_name = ? OR EMPLOYEES.last_name = ?
        '''

        for emp in cursor.execute(query, (searchParam, searchParam)):
            employee = Employee(emp[1], emp[2], emp[3], emp[4], emp[5], emp[6], emp[7], emp[8], emp[9], None, None, None, None)
            employee.EmpId = emp[0]
            employeeList.append(employee)

    currentDataContext.close()
    
    return employeeList

def generate_employee_report(includeArchived : bool):
    # May need to check and see if the user has that filename open?
    # Should user be able to name file?
    currentDataContext = sqlite3.connect('Database/empdata.db')
    cursor = currentDataContext.cursor()
    empList = []

    query = '''SELECT EMPLOYEES.*, EMPLOYEE_PERMISSIONS.reporting_permissions, EMPLOYEE_PERMISSIONS.accounting_permissions, 
        EMPLOYEE_PERMISSIONS.editing_permissions, EMPLOYEE_PERMISSIONS.manager_permissions, 
        EMPLOYEE_PTO.current_pto, EMPLOYEE_PTO.used_pto, EMPLOYEE_PTO.pto_limit,
        EMPLOYEE_CREDENTIALS.emp_social_last FROM EMPLOYEES LEFT JOIN EMPLOYEE_ADDRESS ON EMPLOYEE_ADDRESS.emp_id = EMPLOYEES.emp_id 
        LEFT JOIN EMPLOYEE_PERMISSIONS ON EMPLOYEE_PERMISSIONS.emp_id = EMPLOYEES.emp_id
        LEFT JOIN EMPLOYEE_PTO ON EMPLOYEE_PTO.emp_id = EMPLOYEES.emp_id
        LEFT JOIN EMPLOYEE_CREDENTIALS ON EMPLOYEE_CREDENTIALS.emp_id = EMPLOYEES.emp_id'''

    for emp in cursor.execute(query):
        empList.append(emp)

    currentDataContext.close()

    columnNames = ['Id', 'First Name', 'Last Name', 'Phone Number', 'Salary', 'Hourly', 'Commission', 'Pay Type', 'Pay Method', 'Is Archived', 'Can Report', 'Can Account', 'Can Edit', 'Manager', 'Current PTO', 'PTO Used', 'PTO Limit', 'SSN Last 4']
    dataframe =pandas.DataFrame(empList, columns=columnNames)
    writer = pandas.ExcelWriter('new.xlsx')
    dataframe.to_excel(writer, sheet_name='Employee Records')
    writer.save()


initialize_employee_database()