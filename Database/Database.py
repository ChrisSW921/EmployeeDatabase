import sqlite3

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

    for command in database_commands:
        cursor.execute(command)

    database.commit()
    
database = sqlite3.connect('Database/empdata.db')
cursor = database.cursor()

initialize_employee_database(database, cursor)