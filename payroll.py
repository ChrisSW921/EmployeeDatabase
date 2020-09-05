"""Employee data file"""

from abc import ABC, abstractmethod
import os, os.path, shutil
employees = []
PAY_LOGFILE = 'payroll.txt'


class Employee:
    """Class to create employee and interact with it"""
    def __init__(self, emp_id, name, address, city, state, zipcode, classification):
        self.emp_id = emp_id
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.classification = classification
        
    def make_hourly(self, Hourly_pay):
        """Change employees classification to hourly"""
        self.classification = Hourly(Hourly_pay)
        
    def make_salaried(self, salary):
        """Change employees classification to salaried"""
        self.classification = Salaried(salary)
        
    def make_commissioned(self, salary, comm_rate):
        """Change employees classification to commissioned"""
        self.classification = Commissioned(salary, comm_rate)
        
    def issue_payment(self):
        """Compute the payment for the employee and write to the txt file"""
        try:
            if len(self.classification.time_cards) == 0:
                pass
            else:
                with open(PAY_LOGFILE, 'a') as file1:
                    file1.write(f'Mailing {round(self.classification.issue_payment(),2)} to {self.name} at {self.address} {self.city} {self.state} {self.zipcode}\n')           
        except:
            with open(PAY_LOGFILE, 'a') as file1:
                file1.write(f'Mailing {round(self.classification.issue_payment(),2)} to {self.name} at {self.address} {self.city} {self.state} {self.zipcode}\n')



class Classification(ABC):
    """Abstract class to organize classification"""
    def __init__(self):
        pass
    @abstractmethod
    def issue_payment(self):
        pass
    

class Hourly(Classification):
    def __init__(self, Hourly_pay):
        self.Hourly_pay = Hourly_pay
        self.time_cards = []
    def add_timecard(self,time_card):
        """Add a timecard to the list of timecards"""
        self.time_cards.append(time_card)
    def issue_payment(self):
        """Compute and return the payment for the pay period"""
        total = 0
        for entry in self.time_cards:
            total += self.Hourly_pay * entry
        self.time_cards = []
        return total
        


class Salaried(Classification):
    def __init__(self, salary):
        self.salary = salary
    def issue_payment(self):
        """Compute and return the payment for the pay period"""
        return self.salary / 24

class Commissioned(Salaried):
    def __init__(self, salary, comm_rate):
        self.commission_rate = comm_rate
        self.salary = salary
        self.receipts = []
    def add_receipt(self,receipt):
        """Add a receipt to the list of receipts"""
        self.receipts.append(receipt)
    def issue_payment(self):
        """Compute and return the payment for the pay period"""
        self.total = (self.salary / 24)
        for entry in self.receipts:
            self.total += (entry * (self.commission_rate/100))
        self.receipts = []
        return self.total
        

def load_employees():
    """Parce CSV file and load list of employees with given attributes"""
    emps_raw_list = []
    with open('employees.csv') as emps:
        for line in emps:
            emps_raw_list.append(line.strip().split(','))
    for emp in emps_raw_list[1:]:
        if emp[7] == '3':
            new_emp = Employee(emp[0],f'{emp[1]} {emp[2]}',emp[3],emp[4],emp[5],emp[6],Hourly(float(emp[10])))
            employees.append(new_emp)
        elif emp[7] == '2':
            new_emp = Employee(emp[0],f'{emp[1]} {emp[2]}',emp[3],emp[4],emp[5],emp[6],Commissioned(float(emp[8]),float(emp[9])))
            employees.append(new_emp)
        elif emp[7] == '1':
            new_emp = Employee(emp[0],f'{emp[1]} {emp[2]}',emp[3],emp[4],emp[5],emp[6],Salaried(float(emp[8])))
            employees.append(new_emp)

        
def find_employee_by_id(id):
    """Return employee object with given id"""
    for emp in employees:
        if emp.emp_id == id:
            return emp  
  
def process_timecards():
    """Parse CSV file and add the timecards to the appropriate employees classification"""
    timecard_raw_list = []
    with open('timecards.csv') as timecards:
        for timec in timecards:
            timecard_raw_list.append(timec.strip().split(','))
    for item in timecard_raw_list:
        emp = find_employee_by_id(item[0])
        for entry in item[1:]:
            emp.classification.time_cards.append(float(entry))
        
         
def process_receipts():
    """Parse CSV file and add the receipts to the appropriate employees classification"""
    raw_receipts = []
    with open('receipts.csv') as receipts:
        for receipt in receipts:
            raw_receipts.append(receipt.strip().split(','))
    for item in raw_receipts:
        emp = find_employee_by_id(item[0])
        for rec in item[1:]:
            emp.classification.receipts.append(float(rec))

        
def run_payroll():
    """Delete old file and write all the payments to the employees to the file"""
    if os.path.exists(PAY_LOGFILE):
        os.remove(PAY_LOGFILE)
    for emp in employees:
        emp.issue_payment()
       

   
     