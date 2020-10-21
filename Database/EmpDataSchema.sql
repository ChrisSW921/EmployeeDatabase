CREATE TABLE IF NOT EXISTS EMPLOYEES ( 
    emp_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    first_name TEXT, last_name TEXT, 
    phone_number INTEGER, 
    pay_method INTEGER, 
    salary REAL, 
    hourly REAL, 
    commission REAL 
);

CREATE TABLE IF NOT EXISTS EMPLOYEE_CREDENTIALS ( 
    emp_id INTEGER NOT NULL, 
    emp_password TEXT, 
    social_security TEXT, 
    FOREIGN KEY(emp_id) REFERENCES EMPLOYEES(emp_id) 
);

CREATE TABLE IF NOT EXISTS EMPLOYEE_ADDRESS ( 
    emp_id INTEGER NOT NULL, 
    street_address TEXT, 
    address_city TEXT, 
    address_state TEXT, 
    address_zip INTEGER, 
    FOREIGN KEY(emp_id) REFERENCES EMPLOYEES(emp_id) 
);

CREATE TABLE IF NOT EXISTS EMPLOYEE_PTO ( 
    emp_id INTEGER NOT NULL, 
    current_pto INTEGER, 
    used_pto INTEGER, 
    pto_remaining INTEGER, 
    FOREIGN KEY(emp_id) REFERENCES EMPLOYEES(emp_id)
);

CREATE TABLE IF NOT EXISTS EMPLOYEE_PERMISSIONS ( 
    emp_id INTEGER NOT NULL, 
    reporting_permissions BOOLEAN, 
    accounting_permissions BOOLEAN, 
    editing_permissions BOOLEAN, 
    manager_permissions BOOLEAN, 
    FOREIGN KEY(emp_id) REFERENCES EMPLOYEES(emp_id) 
);