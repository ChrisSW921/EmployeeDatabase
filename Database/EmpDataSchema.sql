CREATE TABLE IF NOT EXISTS EMPLOYEES ( 
    emp_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    first_name TEXT, last_name TEXT, 
    phone_number TEXT, 
    salary REAL, 
    hourly REAL, 
    commission REAL,
    pay_type INTEGER,
    pay_method INTEGER,
    archived BOOLEAN 
);

CREATE TABLE IF NOT EXISTS EMPLOYEE_CREDENTIALS ( 
    emp_id INTEGER NOT NULL, 
    emp_password TEXT,
    emp_password_salt TEXT,
    emp_social_inital TEXT,
    emp_social_salt TEXT, 
    emp_social_last TEXT, 
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
    pto_limit INTEGER, 
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

CREATE TABLE IF NOT EXISTS EMPLOYEE_TIMECARDS (
    emp_id INTEGER NOT NULL,
    timecard_hours REAL,
    FOREIGN KEY(emp_id) REFERENCES EMPLOYEES(emp_id)
);

DROP TRIGGER IF EXISTS TRG_CREATE_EMP_DETAILS;