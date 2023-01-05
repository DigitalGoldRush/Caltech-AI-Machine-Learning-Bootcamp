#Use parameterized constructors in all classes to initialize default values
#Create a bank class with the following attributes:
#IFSC_Code
#Bank_Name
#Branch_Name
#Location

class Bank:
    def __init__(self, IFSC_Code, Bank_Name, Branch_Name, Location):
        self.IFSC_Code = IFSC_Code
        self.Bank_Name = Bank_Name
        self.Branch_Name = Branch_Name
        self.Location = Location


#Create a customer class with the following attributes:
#customerID
#custname
#address
#contactdetails

class Customer:
    def __init__(self, customerID, custname, address, contactdetails):
        self.customerID = customerID
        self.custname = custname
        self.address = address
        self.contactdetails = contactdetails


#Create an account class that inherits from the bank class 
# the following attributes (use Super() to pass value to the base class):
#AccountID
#Cust Object of Customer
#balance

class Account(Bank):
    def __init__(self, AccountID, Cust, balance, IFSC_Code, Bank_Name, Branch_Name, Location):
        super().__init__(IFSC_Code, Bank_Name, Branch_Name, Location)
        self.AccountID = AccountID
        self.Cust = Cust
        self.balance = balance
    


#Add the following methods to get account information, withdraw, and deposit:
#GetAccountInfo()
#deposit(2000,'true')
#withdraw(500)
#getBalance()

    def GetAccountInfo(self):
        print(self.AccountID, self.Cust, self.balance)
        return self.AccountID, self.Cust, self.balance

    def deposit(self, amount, isCash):
        if isCash == 'true':
            self.balance += amount
            print('Your balance is', self.balance)
        else:
            print('Your balance is', self.balance)
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print('You have insufficient balance')
        else:
            self.balance -= amount
            print('Your balance is', self.balance)
        return self.balance

#Create a SavingsAccount class that inherits from the account with the following
#  attributes (Use Super () to pass valued to the base class):
#MinBalance

#Add the following methods to get account information, withdraw, and deposit:
#getsavingAccountInfo()
#deposit(2000,'true')
#withdraw(500)
#getBalance()

#Validate MinBalance before allowing withdrawals.
#Create a class that runs the program and accepts input from the end user to create
#respective class objects and print details. Add a method to perform deposit and 
#withdrawal transaction based on the end user input.