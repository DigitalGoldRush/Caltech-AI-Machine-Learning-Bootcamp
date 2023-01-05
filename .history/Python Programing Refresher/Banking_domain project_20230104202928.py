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

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.balance)
        return self.balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(self.balance)
        return self.balance

    def getBalance(self):
        print(self.balance)
        return self.balance

  
#Create a SavingsAccount class that inherits from the account with the following
#  attributes (Use Super () to pass valued to the base class):
#MinBalance

class SavingsAccount(Account):
    def __init__(self, MinBalance, AccountID, Cust, balance, IFSC_Code, Bank_Name, Branch_Name, Location):
        super().__init__(AccountID, Cust, balance, IFSC_Code, Bank_Name, Branch_Name, Location)
        self.MinBalance = MinBalance



#Add the following methods to get account information, withdraw, and deposit:
#getsavingAccountInfo()
#deposit(2000,'true')
#withdraw(500)
#getBalance()

    def getsavingAccountInfo(self):
        print(self.AccountID, self.Cust, self.balance, self.MinBalance)
        return self.AccountID, self.Cust, self.balance, self.MinBalance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.balance)
        return self.balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(self.balance)
        return self.balance

    def getBalance(self):
        print(self.balance)
        return self.balance

#Validate MinBalance before allowing withdrawals.
#Create a class that runs the program and accepts input from the end user to create
#respective class objects and print details. Add a method to perform deposit and 
#withdrawal transaction based on the end user input.

class Run:
    def __init__(self):
        self.IFSC_Code = input("Enter the IFSC_Code: ")
        self.Bank_Name = input("Enter the Bank_Name: ")
        self.Branch_Name = input("Enter the Branch_Name: ")
        self.Location = input("Enter the Location: ")
        self.customerID = input("Enter the customerID: ")
        self.custname = input("Enter the custname: ")
        self.address = input("Enter the address: ")
        self.contactdetails = input("Enter the contactdetails: ")
        self.AccountID = input("Enter the AccountID: ")
        self.Cust = input("Enter the Cust: ")
        self.balance = int(input("Enter the balance: "))
        self.MinBalance = int(input("Enter the MinBalance: "))

    def GetAccountInfo(self):
        print(self.AccountID, self.Cust, self.balance)
        return self.AccountID, self.Cust, self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.balance)
        return self.balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(self.balance)
        return self.balance

    def getBalance(self):
        print(self.balance)
        return self.balance

    def getsavingAccountInfo(self):
        print(self.AccountID, self.Cust, self.balance, self.MinBalance)
        return self.AccountID, self.Cust, self.balance, self.MinBalance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.balance)
        return self.balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(self.balance)
        return self.balance

    def getBalance(self):
        print(self.balance)
        return self.balance

    def RunBank(self):
        bank = Bank(self.IFSC_Code, self.Bank_Name, self.Branch_Name, self.Location)
        customer = Customer(self.customerID, self.custname, self.address, self.contactdetails)
        account = Account(self.AccountID, self.Cust, self.balance, self.IFSC_Code, self.Bank_Name, self.Branch_Name, self.Location)
        savingaccount = SavingsAccount(self.MinBalance, self.AccountID, self.Cust, self.balance, self.IFSC_Code, self.Bank_Name, self.Branch_Name, self.Location)

        while True:

            print("1. GetAccountInfo")
            print("2. deposit")
            print("3. withdraw")
            print("4. getBalance")
            print("5. getsavingAccountInfo")
            print("6. Exit")
            print("Enter your choice: ")

            choice = int(input())
            if choice == 1:
                print("Enter the customer ID: ")
                customerID = input()
                if customerID == self.customerID:
                    print("Enter the AccountID: ")
                    AccountID = input()
                    if AccountID == self.AccountID:
                        account.GetAccountInfo()
                    else:
                        print("Invalid AccountID")
                else:
                    print("Invalid customer ID")
                    exit()
            elif choice == 2:
                print("Enter the customer ID: ")
                customerID = input()
                if customerID == self.customerID:
                    print("Enter the AccountID: ")
                    AccountID = input()
                    if AccountID == self.AccountID:
                        print("Enter the amount: ")
                        amount = int(input())
                        account.deposit(amount)
                    else:
                        print("Invalid AccountID")
                else:
                    print("Invalid customer ID")
                    exit()
            elif choice == 3:
                print("Enter the customer ID: ")
                customerID = input()
                if customerID == self.customerID:
                    print("Enter the AccountID: ")
                    AccountID = input()
                    if AccountID == self.AccountID:
                        print("Enter the amount: ")
                        amount = int(input())
                        account.withdraw(amount)
                    else:
                        print("Invalid AccountID")
                else:
                    print("Invalid customer ID")
                    exit()
            elif choice == 4:
                print("Enter the customer ID: ")
                customerID = input()
                if customerID == self.customerID:
                    print("Enter the AccountID: ")
                    AccountID = input()
                    if AccountID == self.AccountID:
                        account.getBalance()
                    else:
                        print("Invalid AccountID")
                else:
                    print("Invalid customer ID")
                    exit()
            elif choice == 5:
                print("Enter the customer ID: ")
                customerID = input()
                if customerID == self.customerID:
                    print("Enter the AccountID: ")
                    AccountID = input()
                    if AccountID == self.AccountID:
                        savingaccount.getsavingAccountInfo()
                    else:
                        print("Invalid AccountID")
                else:
                    print("Invalid customer ID")
                    exit()
            elif choice == 6:
                exit()
            else:
                print("Invalid choice")
                exit()


if __name__ == "__main__":
    run = Run()
    run.RunBank()
    print("Thank you for using the bank!")
    exit()





