import sys
import os
sys.path.insert(0,os.getcwd())
from Gui.login import LoginScreen
from Database import database

database.initialize_employee_database()
LoginScreen()