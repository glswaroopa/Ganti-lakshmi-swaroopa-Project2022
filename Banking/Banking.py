# Banking Project Landing Page
import sys
import logging
#Prerequisites before you run this application
# you need to have a msssql server with atleast express edition
# install the python driver for mssql https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/python-sql-driver-pyodbc?view=sql-server-ver16
# restore the sql database "Banking"
# Create a login on the MSSQL Server with the user banking,password User@123, can be of anychoice, need to chang in the connection string.


print("Welcome to Banking Application")


def __init__(self,):
        self.loggedIn = True
def home(user):
    log() #function to log the records
    logging.info('Started') 
    print("\n 1. Customer, \n 2. Admin, \n 3. Exit ")
    a = input("What would you like to do: ")
    if(a == "1" or a == "1"):
        login(user) # Calling the loginclass for customer
    elif(a == "2" or a == "2"):
        Adminlogin(user)  #Calling the loginclass for Administration
    elif(a == "3" or a == "3"):
         sys.exit(0) #exiting the applicazion
        
    else:
        print("Choose a valid option")
        home('')
def login(user):
    import login 
    login.home    # Calling the loginclass for customer (from login.py)
def Adminlogin(user):
    import AdminUser
    AdminUser.Userlogin  #Calling the userlogin class from Admin (from AdminUser.py)
def log():
    logging.basicConfig(filename='.\myapp.log', level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

home('')
