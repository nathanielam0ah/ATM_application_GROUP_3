#!/usr/bin/env python
main_code = 1234
#uml classes
print("welcome to Python Sandwich Bank ATM")
while True:
    code  = int(input("please enter your code: "))
    if code == main_code:
        input("select your transaction")
        input1 = input("Press 1 for Balance: ")
        input2 = input("Press 2 for withdraw: ")
        input3 = input("Press 3 for Deposit: ")
        input4 = input("press 4 for Transfer Transaction: ")
        
        list = [input1, input2, input3]
        
        switch (list)
            case list[0]:
                balance = Account("saving", "customer")
                balance.checkbalance()
                break
            case list[1]:
                withdraw = withdrawal_transaction(904)
                withdraw.withdraw()
                break
            case list[3]:
                transfer = Transfer_Transaction()
                transfer.amount = 56
                transfer.accountNo = 40110495837262
                print(transfer.amount)
                print(transfer.accountNo)
                break
            
        
        
        


#parent classes
class Bank:
    code = None
    address = None
    def manages(self):
        print("this is method manages under bank class")
    def maintains(self):
        print("this is the maintains method under the Bank class")

class ATM:
    location = None
    managedBy = None
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
    
    def withdrawal(self, amount, balance ):
         if self.amount <=  balance:
            new_balance = balance - amount
            print(new_balance)
        else:
            print("sorry! insufficient balance")
            
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
        self.types
        self.owner
    
    def checkBalance(self):
        print(Balance)
        
    
    

#in association debit card class and customer class and the ATM transaction class.
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
