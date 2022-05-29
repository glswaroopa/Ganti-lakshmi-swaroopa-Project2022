import sys
import logging
# Customer registration is done in the class UserRegister
# it uses the method "create_server_connection" under Class User .
# method create_server_connection is hardcoded with connection variables for this project, but in general should be handled in the configuration files.
# Class userlogin,checks for Customer login against the password saved in the database.

class UserRegister:
  import pyodbc
  def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.loggedIn = True
  def register():
    Name = input("Name: ")
    Adress = input("Address: ")
    PhoneNumber = input("PhoneNumber: ")
    username = input("username: ")
    password = input("password: ")
    IntialBalance = input("intialbalance: ")
    import random
    AccountNumber = random.randint(0,50)
    s = create_server_connection()
    cursor = s.cursor()
    cursor.execute("INSERT INTO dbo.customers(Name,Address,PhoneNumber,Username,Password,intialBalance,AccountNumber) VALUES ('%s','%s','%s','%s','%s','%s','%s');"%(Name,Adress,PhoneNumber,username,password,IntialBalance,AccountNumber))
    cursor.commit()
    print("Welcome, " + username)
    logging.info("created" + username)
    home('')

class User():
 import pyodbc

 def __init__(self, name, username, password):
        User.uname
        User.upwd
        self.name = name
        self.username = username
        self.password = password
        self.loggedIn = True
def home(user):
    print ("Welcome to Custome Area")
    logging.info('Entered customer Area')
    print("\n 1.Login, \n 2.Signup,\n 3.Previous Menu,\n 4.exit")
    a = input("What would you like to do: ")
    if(a == "1" or a == "1"):
        Userlogin.login(Userlogin.uname,Userlogin.upwd)

    elif(a == "2" or a == "2"):
        UserRegister.register()
    elif(a == "3" or a == "3"):
        import Banking
        Banking.home('')
    elif(a == "4" or a == "4"):
         sys.exit(0)
    else:
        print("Choose a valid option")
        home('')
def create_server_connection():
     import pyodbc 
     connection = pyodbc.connect('Driver={SQL Server};''Server=INCDE01D011G01;''Database=Banking;''Trusted_Connection=yes;'"UID=banking;""PWD=User@123;")
     return connection

class Userlogin:
 def __init__(self,name):
        self.name = name
        self.loggedIn = True
 def login(uname,upwd):
        print ("username and password are case sensitive")
        Userlogin.uname = input("Username: ")
        Userlogin.upwd = input("Password: ")
        import pyodbc
        s = create_server_connection()
        cursor = s.cursor()
        cursor.execute('select Password from customers where [Username]=?', Userlogin.uname)
        result = cursor.fetchone()
        if result is not None:
          a = (result[0])
          if(Userlogin.upwd == a):
            print("Welcome, " + Userlogin.uname)
            logging.info(Userlogin.uname + 'logged in')
            import bankaccount
        else:
                print("Entered username or password incorrect")
                #Userlogin.login(Userlogin.uname,Userlogin.upwd)
                home('')
               
 uname = ""
 upwd = ""
home('')





