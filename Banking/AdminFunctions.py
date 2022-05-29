#Admin Functions Class has three functions
# create_server_connection is a hard coded connection variable to MSSQL
# functon custinfo is a function used to retrvie all customer information inside the table dbo.customers, except customerid
# function deletecust is a function used to delete customer from the dbo.customers table.
# function updatecust is a function used for updating customer information ,like name,telephone number,address,intialbalance,password.

import logging
import AdminUser
class AdminFunctions():
 customer = ""
def home(user):
        logging.info('Ended')
        print("\n 1.CustomerInformation,\n 2.Delete Customer,\n 3.UpdateCustomer")
        a = input("What would you like to do: ")
        if(a == "1" or a == "1"):
            custinfo(user)
        elif(a == "2" or a == "2"):
            deletecust(user)
        elif(a == "3" or a == "3"):
            updatecust(user)
        else:
            print("Choose a valid option")
            home('')
def create_server_connection():
     import pyodbc 
     connection = pyodbc.connect('Driver={SQL Server};''Server=INCDE01D011G01;''Database=Banking;''Trusted_Connection=yes;'"UID=banking;""PWD=User@123;")
     return connection
def custinfo(self):
    print ("customerinformation")
    logging.info (AdminUser.Userlogin.uname + " has accessed customer information") #Userlogin.uname
       
    s = create_server_connection()
    cursor = s.cursor()
    cursor.execute('select Name,Address,PhoneNumber,Username,Password,AccountNumber from customers')
    result = cursor.fetchall()
    num_fields = len(cursor.description)
    field_names = [i[0] for i in cursor.description]
    print(field_names)
    for a in result:
     print(a)
    logging.info (AdminUser.Userlogin.uname + " has exited customer information") #Userlogin.uname
    cursor.close()
    s.close()
    print("Returing to previous Menu")
    home('')
    


def deletecust(self):
    print("deletecustomer")
    print("Enter the customer Name to delete")
    customerName = input("EnterCustomerName:")
    s = create_server_connection()
    cursor = s.cursor()
    cursor.execute('delete from customers where Name =?',customerName)
    cursor.commit()
    logging.info (AdminUser.Userlogin.uname + " has deleted the customer information" + customerName ) #Userlogin.uname
    s.close()
    print("Returing to previous Menu")
    home('')
def updatecust(self):
    print("Update Customer Information")
    customerName = input("Enter CustomerName: ")
    AccountNumber = input("Enter CustomerAccountNumber: ")
    logging.info (AdminUser.Userlogin.uname + " has entered the customer update Section :" + customerName ) #Userlogin.uname
    print ("")
    s = create_server_connection()
    cursor = s.cursor()
    cursor.execute ('select Password from customers where [Name]=? and [AccountNumber] =?', customerName,AccountNumber)
    result = cursor.fetchone()
    if result is not None:
        print("Please select from below which information of you would like to update ")
        datachange = input("\n 1.Name \n 2.PhoneNumber \n 3.Address \n 4.intialBalance \n 5.password \n 6.AccountNumber : ")
        s = create_server_connection()
        cursor = s.cursor()
        if(datachange == "1"):
           Name = input("Enter New CustomerName: ")
           cursor.execute ("update customers set Name = (?) where [Name]= (?) and [AccountNumber] = (?)", Name,customerName,AccountNumber)
           cursor.commit()
           print("Customer Name Updated")
           logging.info (AdminUser.Userlogin.uname + " has updated the customer Name of customer :" + customerName + " to " + Name)
           cursor.close()
           s.close()
           
           
        elif(datachange == "2"):
            PhoneNumber = input("Enter New PhoneNumber: ")
            cursor.execute ("update customers set PhoneNumber = (?) where [Name]= (?) and [AccountNumber] = (?)", PhoneNumber,customerName,AccountNumber)
            cursor.commit()
            print ("New Phone Number Updated for" + customerName )
            logging.info (AdminUser.Userlogin.uname + " has updated the PhoneNumber of customer :" + customerName )
            
            cursor.close()
            s.close()
            print("Returing to previous Menu")
            home('')
            
        elif(datachange == "3"):
            Address = input("Enter New Address: ")
            cursor.execute ("update customers set Address = (?) where [Name]= (?) and [AccountNumber] = (?)", Address,customerName,AccountNumber)
            cursor.commit()
            print ("New Address Updated for" + customerName )
            logging.info (AdminUser.Userlogin.uname + " has updated the address of customer :" + customerName )
            
            cursor.close()
            s.close()
            print("Returing to previous Menu")
            home('')
           
        elif(datachange == "4"):
           intialBalance = input("Enter New Balance: ")
           cursor.execute ("update customers set intialBalance = (?) where [Name]= (?) and [AccountNumber] = (?)", intialBalance,customerName,AccountNumber)
           cursor.commit()
           print ("New Balance Updated for" + customerName )
           logging.info (AdminUser.Userlogin.uname + " has updated the intialbalance of customer :" + customerName )
           
           cursor.close()
           s.close()
           print("Returing to previous Menu")
           home('')
           
        elif(datachange == "5"):
           password = input("Enter New password: ")
           cursor.execute ("update customers set password = (?)  where [Name]= (?) and [AccountNumber] = (?)", password,customerName,AccountNumber)
           cursor.commit()
           print ("New password Updated for" + customerName )
           logging.info (AdminUser.Userlogin.uname + " has updated the password of customer :" + customerName )
           cursor.close()
           s.close()
           print("Returing to previous Menu")
           home('')
           
        elif(datachange == "6"):
           newaccountnumber = input("Enter New AccountNumber: ")
           cursor.execute ("update customers set AccountNumber = (?) where [Name]= (?) and [AccountNumber] = (?)", newaccountnumber,customerName,AccountNumber)
           cursor.commit()
           print ("New AccountNumber Updated for" + customerName )
           logging.info (AdminUser.Userlogin.uname + " has updated the accountnumber of customer :" + customerName )
           
           cursor.close()
           s.close()
           print("Returing to previous Menu")
           home('')
           

        else:
              print("Choose a valid option")
              home('')
    else:
         print("\n Entered Wrong Customer Name or Account Number \n go to previous menu and fetch customerinformation to select the name")
         home('')


home('')