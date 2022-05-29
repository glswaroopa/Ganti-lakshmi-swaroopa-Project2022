import logging
import login
class Bank_Account():
 balance = "" # class variable filled at query show balance
 accounts = "" # class variable filled at query show balance
 def __init__(self):
            super().__init__()
            balance=self.balance
            print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
            self.loggedIn = True
def listbankaccounts(self):
        print ("listing all user accounts")
        s = login.create_server_connection()
        cursor = s.cursor()
        cursor.execute('SELECT AccountNumber,intialBalance FROM [customers] WHERE [Username] = ?',login.Userlogin.uname)
        result = cursor.fetchall()
        rows = len(result)
        print (rows)
        accounts = rows
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        print(field_names)
        for a in result:
         print(a)
        s.close()
        return()
def display(self):
           
            s = login.create_server_connection()
            cursor = s.cursor()
            cursor.execute('select AccountNumber from customers where [Username]=?',login.Userlogin.uname)
            result = cursor.fetchall()
            rows = len(result)
            if rows <= 1 :
                cursor.execute('select intialBalance from customers where [AccountNumber]=?',login.Userlogin.uname)
                result = cursor.fetchone()
                a = (result[0])
                s.close()
                balance=a
                Bank_Account.balance = balance
                print("\n Net Available Balance=",balance)
                return()
                

            else:
                print("You have mutiple Bank Accounts")
                listbankaccounts(self)
                accountnumber = input ("Enter the account Number from which you want to see the balance :")
                cursor.execute('select intialBalance from customers where [AccountNumber]=?',accountnumber)
                result = cursor.fetchone()
                a = (result[0])
                s.close()
                balance=a
                Bank_Account.balance = balance
                print("\n Net Available Balance=",balance)
                return()
def deposit(self):
            s = login.create_server_connection()
            cursor = s.cursor()
            cursor.execute('select AccountNumber from customers where [Username]=?',login.Userlogin.uname)
            result = cursor.fetchall()
            rows = len(result)
            if rows <= 1 :
                amount = float(input("Enter amount to be deposited: "))
                cursor.execute('select intialBalance from customers where [Username]=?',login.Userlogin.uname)
                result = cursor.fetchone()
                a = (result[0])
                balance=a
                print("\n Net Available Balance=",balance)
                balance += amount
                cursor.execute ("update customers set intialBalance = (?) where [Username] = (?)", balance,login.Userlogin.uname)
                cursor.commit()
                cursor.execute('select intialBalance from customers where [Username]=?',login.Userlogin.uname)
                result1 = cursor.fetchone()
                b = (result1[0])
                print("\n Amount Deposited:",b)
                logging.info (login.Userlogin.uname + "has deposited" + amount)
                s.close()
                home('')
  
            else:
                print("You have mutiple Bank Accounts")
                listbankaccounts(self)
                accountnumber = input ("Enter the account Number from which you want to deposit :")
                amount = float(input("Enter amount to be deposited: "))
                cursor.execute('select intialBalance from customers where [AccountNumber]=?',accountnumber)
                result = cursor.fetchone()
                a = (result[0])
                balance=a
                print("\n Net Available Balance=",balance)
                balance += amount
                cursor.execute ("update customers set intialBalance = (?) where [AccountNumber] = (?)", balance,accountnumber)
                cursor.commit()
                cursor.execute('select intialBalance from customers where [AccountNumber]=?',accountnumber)
                result1 = cursor.fetchone()
                b = (result1[0])
                print("\n Amount Deposited:",b)
                logging.info (login.Userlogin.uname + "has deposited" )
                s.close()
                home('')
def withdraw(self):
            s = login.create_server_connection()
            cursor = s.cursor()
            cursor.execute('select AccountNumber from customers where [Username]=?',login.Userlogin.uname)
            result = cursor.fetchall()
            rows = len(result)
            if rows <= 1 :
                amount = float(input("Enter amount to be withdrawn: "))
                cursor.execute('select intialBalance from customers where [Username]=?',login.Userlogin.uname)
                result = cursor.fetchone()
                a = (result[0])
                balance=a
                print("\n Net Available Balance=",balance)
                if balance>=amount:
                    balance -= amount
                    cursor.execute ("update customers set intialBalance = (?) where [Username] = (?)", balance,login.Userlogin.uname)
                    cursor.commit()
                    cursor.execute('select intialBalance from customers where [Username]=?',login.Userlogin.uname)
                    result1 = cursor.fetchone()
                    b = (result1[0])
                    print("\n Net Available Balance:",b)
                    logging.info (login.Userlogin.uname + "has withdrawn" )
                    s.close()
                else:
                    print("\n Insufficient balance  ")
                    home('')
            else:
                print("You have mutiple Bank Accounts")
                listbankaccounts(self)
                accountnumber = input ("Enter the account Number from which you want to Withdraw :")
                amount = float(input("Enter amount to be withdraw: "))
                cursor.execute('select intialBalance from customers where [AccountNumber]=?',accountnumber)
                result = cursor.fetchone()
                a = (result[0])
                balance=a
                print("\n Net Available Balance=",balance)
                if balance>=amount:
                    balance -= amount
                    cursor.execute ("update customers set intialBalance = (?) where [AccountNumber] = (?)", balance,accountnumber)
                    cursor.commit()
                    cursor.execute('select intialBalance from customers where [AccountNumber]=?',accountnumber)
                    result1 = cursor.fetchone()
                    b = (result1[0])
                    print("\n Net Available Balance:",b)
                    logging.info (login.Userlogin.uname + "has withdrawn" )
                    s.close()
                else:
                    print("\n Insufficient balance  ")
                    home('')

      
def createbankaccount(self):
      try:
            import random
            AccountNumber = random.randint(0,500)
            s = login.create_server_connection()
            cursor = s.cursor()
            cursor.execute('SELECT AccountNumber FROM [customers] WHERE [Username] = ?',login.Userlogin.uname)
            result = cursor.fetchone()
            a = (result[0])
            print (a)
            cursor.execute('SELECT * INTO Tempdb FROM [Banking].[dbo].[customers] WHERE [Username] = ? AND [AccountNumber]= ? ',login.Userlogin.uname,a)
            cursor.commit()
            cursor.execute('UPDATE Tempdb SET [AccountNumber] = ?',AccountNumber)
            cursor.commit()
            cursor.execute('INSERT INTO [Banking].[dbo].[customers] SELECT * FROM Tempdb')
            print(cursor.rowcount, "Successfully created New Bank Account")
            cursor.execute('DROP TABLE Tempdb')
            cursor.commit()
            logging.info (login.Userlogin.uname + "has created new account" + AccountNumber)
      except Error as error:
           print(error)
      finally:
        cursor.close()
        s.close()
def home(user):
        print("\n 1.BalanceInformation,\n 2.Deposit,\n 3.Withdrawl,\n 4.createbankaccount,\n 5.ListBankAccount")
        a = input("What would you like to do: ")
        if(a == "1" or a == "1"):
            display(user)
        elif(a == "2" or a == "2"):
            deposit(user)
        elif(a == "3" or a == "3"):
            withdraw(user)
        elif(a == "4" or a == "4"):
            createbankaccount(user)
        elif(a == "5" or a == "5"):
            listbankaccounts(user)
        else:
            print("Choose a valid option")
            home('')
home('')



 