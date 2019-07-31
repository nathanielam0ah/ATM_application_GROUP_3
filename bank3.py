#!/usr/bin/env python

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
        logIn_tries = 0
        while logIn_tries != 4:
            try:
                self.accountNo = str(input("ACCOUNT ID: "))
                self.accountPin = int(input("PIN: "))
            except ValueError:
                print("INVALID INPUT")

            if (self.accountNo == Bank.accountNo) and (self.accountPin == Bank.accountPin):
                print("LOGIN SUCCESS")
                ATM.logIn_confirmation = True
                return ATM.logIn_confirmation
            else:
                print("INCORRECT LOGIN INFO, TRY AGAIN")
                logIn_tries += 1

            if logIn_tries == 4:
                print("MAXIMUM LOGIN ATTEMPS. EJECTING CARD ... ")
                ATM.logIn_confirmation = False
                return ATM.logIn_confirmation
                exit()

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
                print("PSW2019 GROUP02 BANK ATM.")
                print("ENTER 1 TO CHECK ACCOUNT BALANCE, 2 FOR TRANSACTIONS AND 3 TO LOG OUT")
                try:
                    menuChoice = int(input(": " ))
                except ValueError:
                    print("INVALID INPUT")

                if (menuChoice == 1):
                    testAccount = Account("savings", "group02")
                    testAccount.checkBalance()

                elif (menuChoice == 2):
                    print("ENTER 1 FOR WITHDRAWAL AND 2 FOR TRANSFER.")
                    try:
                        confirm_transaction = int(input(": "))
                    except ValueError:
                        print("INVALID INPUT")
                    if (confirm_transaction == 1):
                        testAccount = Withdrawal_transaction()
                        testAccount.withdrawal()
                    elif (confirm_transaction == 2):
                        testAccount = Transfer_Transaction()
                        testAccount.deposit()

                elif (menuChoice == 3):
                    break
        if ATM.logIn_confirmation == False:
            exit()

class AtmTransaction:
    transactionID = None
    date = None
    type = None
    def update(self):
        print("this is the atm transaction class")

class Withdrawal_transaction(AtmTransaction):
    amount = None
    accountPin = None
    def withdrawal(self):
        try:
            amount = float(input("AMOUNT: "))
        except ValueError:
            print("INVALID INPUT")
        if  amount <= Account.balance:
            print("CONFIRM WITHDRAWAL")
            try:
                accountPin = int(input(": "))
            except ValueError:
                print("INVALID INPUT")
            if (accountPin == Bank.accountPin):
                Account.balance = Account.balance - amount
                print("WITHDRAWAL SUCCESSFUL\nCURRENT BALANCE: ",Account.balance)
            else:
                print("WITHDRAWAL FAILED, INCORRECT PIN")
        else:
            print("INSUFFICIENT BALANCE")

class Transfer_Transaction(AtmTransaction):
    accountNo = None
    amount = None
    accountPin = None
    def transferToOther(self):
        print()

    def deposit(self):
        try:
            amount = float(input("AMOUNT: "))
        except ValueError:
            print("INVALID INPUT")
        print("CONFIRM DEPOSIT")
        try:
            accountPin = int(input(": "))
        except ValueError:
            print("INVALID INPUT")
        if (accountPin == Bank.accountPin):
            Account.balance = Account.balance + amount
            print(amount," DEPOSITED\nCURRENT BALANCE: ", Account.balance)
        else:
            print("DEPOSIT FAILED, INCORRECT PIN")


class DebitCard:
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
    balance  = 3000.0

    def __init__(self, types,owner):
        self.types = "savings"
        self.owner = "group02"

    def checkBalance(self):
        print("BALANCE: ", Account.balance)


class SavingAccounts(Account):
    accountNo = Bank.accountNo

    def debit(self):
        print("print this is the savings account class")

    def credit(self):
        print("this is the checkingAccount class")

class CheckingAccount(Account):
    accountNo = Bank.accountNo

    def debit(self):
        print("this is the checkingAccount class")

    def credit(self):
        print("this is the checkingAccount class")

group02ATM = ATM("GRP0002", 1234)
group02ATM.logIn()
group02ATM.mainMenu()
