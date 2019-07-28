#!/usr/bin/env python

#uml classes
#parent classes
class Bank:
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

    def __init__(self, accountNo, accountPin):
        self.accountNo = accountNo
        self.accountPin = accountPin

    def logIn(self):
        tries = 0
        while tries < 4:
            self.accountNo = str(input("ACCOUNT ID: "))
            self.accountPin = int(input("PIN: "))

            if (self.accountNo == Bank.accountNo) and (self.accountPin == Bank.accountPin):
                print("SUCCESS")
                return True
            else:
                print("INCORRECT LOGIN INFO, TRY AGAIN")
                tries += 1

            return False

    def identifies(self):
        print("identifies method under ATM class")

    def transactions(self):
        print("transaction method under ATM class")

#under atm class
class atmTransaction:
    transactionId = None
    date = None
    type = None
    def update(self):
        print("this is the atm transaction class")

class withdrawal_transaction(atmTransaction):
    # pin = 1234
    def __init__(self, amount):
        self.amount = amount

    def withdrawal(self, amount, balance):
        if self.amount <= balance:
            new_balance = balance - amount
            print(new_balance)
        else:
            print("INSUFFICIENT BALANCE")

class Transfer_Transaction(atmTransaction):
    def __init__(self, amount,accountNo):
        self.amount = amount
        self.accountNo = accountNo


#in association with Bank class
class debitCard:
    cardNo = None
    ownedBy = None

    def access(self):
        print("this is the debit Card class")

class Customer:
    name = None
    address = None
    dob = None

    def owns(self):
        print("this is the customer class")

class Account:
    balance  = 2000

    def __init__(self, types,owner):
        self.types = "savings"
        self.owner = "group02"

    def checkBalance(self):
        print(Balance)


#in direct association debit card class and customer class and the ATM transaction class.
class savingAccounts:
    accountNo = None

    def debit(self):
        print("print this is the savings account class")

    def credit(self):
        print("this is the checkingAccount class")

class checkingAccount:
    accountNo = None

    def debit(self):
        print("this is the checkingAccount class")

    def credit(self):
        print("this is the checkingAccount class")

group02ATM = ATM("GRP0002", 1234)
group02ATM.logIn()
