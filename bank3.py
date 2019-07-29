#!/usr/bin/env python

#uml classes
#assuming bank as database
class Bank:
    firstName = "group"
    lastName = "02"
    code = "PSW2019GRP02"
    address = "AITILAB03"
    accountNo = "GRP0002"
    accountPin = 1234

    def manages(self):
        print("this is method manages under bank class")

    def maintains(self):
        print("this is the maintains method under the Bank class")

class ATM:
    location = None
    managedBy = None
    logIn_confirmation = None

    def __init__(self, accountNo, accountPin):
        self.accountNo = accountNo
        self.accountPin = accountPin

    def logIn(self):
        tries = 0
        while tries < 4:
            self.accountNo = str(input("ACCOUNT ID: "))
            self.accountPin = int(input("PIN: "))

            if (self.accountNo == Bank.accountNo) and (self.accountPin == Bank.accountPin):
                print("LOGIN SUCCESS")
                ATM.logIn_confirmation = True
                return ATM.logIn_confirmation
            else:
                print("INCORRECT LOGIN INFO, TRY AGAIN")
                tries += 1

                ATM.logIn_confirmation = False
                return ATM.logIn_confirmation

    def logOut(self):
        exit()

    def identifies(self):
        print("identifies method under ATM class")

    def transactions(self):
        print("transaction method under ATM class")

    def mainMenu(self):
        menuChoice = None

        if ATM.logIn_confirmation == True:
            while 1:
                print("WELCOME TO PSW2019 GROUP02 BANK ATM.")
                print("ENTER 1 TO CHECK ACCOUNT BALANCE, 2 TO DEPOSIT AND 3 TO WITHDRAW, 4 TO LOG OUT")
                menuChoice = input()

                if (menuChoice == 1):
                    testAccount = Account("savings", "group02")
                    testAccount.checkBalance()
                    break
                elif (menuChoice == 2):
                    testAccount = transfer_Transaction()
                    testAccount.deposit()
                    break
                elif (menuChoice == 3):
                    testAccount = withdrawal_transaction()
                    testAccount.withdrawal()
                    break
                elif (menuChoice == 4):
                    ATM.logIn()
        if ATM.logIn_confirmation == False:
            exit()

#under atm class
class atmTransaction:
    transactionID = None
    date = None
    type = None
    def update(self):
        print("this is the atm transaction class")

class withdrawal_transaction(atmTransaction):
    # pin = 1234
    def __init__(self, amount):
        self.amount = amount

    def withdrawal(self, amount):
        self.amount = input("AMOUNT: ")
        if self.amount <= Account.balance:
            new_balance = Account.balance - amount
            print(new_balance)
        else:
            print("INSUFFICIENT BALANCE")

class transfer_Transaction(atmTransaction):
    def __init__(self, amount,accountNo):
        self.amount = amount
        self.accountNo = accountNo

    def deposit(self):
        self.amount = float(input("AMOUNT: "))
        Account.balance = Account.balance + amount
        print("BALANCE: ", Account.balance)


#in association with Bank class
class debitCard:
    cardNo = None
    ownedBy = None

    def access(self):
        print("this is the debit Card class")

class Customer:
    name = Bank.firstName + " " + Bank.lastName
    address = Bank.address
    dob = "15-07-19"

    def owns(self):
        print("this is the customer class")

class Account:
    balance  = 00.0

    def __init__(self, types,owner):
        self.types = "savings"
        self.owner = "group02"

    def checkBalance(self):
        print("BALANCE: ", Account.balance)


#in direct association debit card class and customer class and the ATM transaction class.
class savingAccounts(Account):
    accountNo = Bank.accountNo

    def debit(self):
        print("print this is the savings account class")

    def credit(self):
        print("this is the checkingAccount class")

class checkingAccount(Account):
    accountNo = Bank.accountNo

    def debit(self):
        print("this is the checkingAccount class")

    def credit(self):
        print("this is the checkingAccount class")

group02ATM = ATM("GRP0002", 1234)
group02ATM.logIn()
group02ATM.mainMenu()
