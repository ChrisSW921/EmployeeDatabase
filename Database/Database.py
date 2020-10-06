import sqlite3

'''
    Database Class

    - This class will also initialize the database when first loading the application 

    Public Methods
        CurrentDataContext - Returns cursor for executing commands
        SaveChanges - Saves changes with try-catch (could handle with logs)
        Close - Void - Closes execution on current stream

'''