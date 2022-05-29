import sys
class AdminRegister:
  import pyodbc
  def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.loggedIn = True
 
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
    print ("Welcome to Admin Area")
    print("1.Login,2.Previous Menu,3.exit")
    a = input("What would you like to do: ")
    if(a == "1" or a == "1"):
        Userlogin.adminlogin(Userlogin.uname,Userlogin.upwd)
    elif(a == "2" or a == "2"):
        import Banking
        Banking.home('')
        
    elif(a == "3" or a == "3"):
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
 def adminlogin(uname,upwd):
        Userlogin.uname = input("Username: ")
        Userlogin.upwd = input("Password: ")
        import pyodbc
        s = create_server_connection()
        cursor = s.cursor()
        cursor.execute('select UserPassword from Admin where [UserName]=?', Userlogin.uname)
        result = cursor.fetchone()
        a = (result[0])
        s.close()
   
        if(Userlogin.upwd == a):
         print("Welcome, " + Userlogin.uname)
         import AdminFunctions
        # bankaccount.Bank_Account.display(uname)
        else:
         print("Incorrect username or password")
         adminlogin.login(Userlogin.uname,Userlogin.upwd)
 uname = ""
 upwd = ""
home('')





