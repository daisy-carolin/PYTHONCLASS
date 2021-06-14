from datetime import datetime
from typing import Type
class Account:
    def __init__(self,name,phone_number):
        self.name=name
        self.phone_number=phone_number

        self.balance=0
        self.statement=[]


    def show_balance(self):
      return f"Hello {self.name} your balance {self.balance} "

    def deposit(self,amount):
      try:
        10*amount
      except TypeError:
         return f"amount must be in figures"
      if amount < 0:
         return f"Hello {self.name} your balance is {self.balance} "
      else:
         self.balance+=amount
         now = datetime.now()
         transaction={
           "amount": amount,
           "time": now,
           "narration":"you deposited"

         }
         self.statement.append(transaction)
         return self. show_balance()

    def withdraw(self,amount):
      try:
        10*amount
      except TypeError:
        return f"amount must be in figures"  

      if amount > 0:
        self.balance-=amount
        now=datetime.now()
        transaction={
           "amount": amount,
           "time": now,
           "narration":"you deposited"


        }
        self.statement.append(transaction)
        return self.show_balance()

    def borrow(self,amount):
      return f"Hello {self.name} you have borrowed a loan of {amount} "

    def repay_loan(self,amount):
      try:
        10*amount
      except TypeError:
        return f"amount must be in figures"  
      return f"Hello {self.name} you have repaid a loan of {amount} "

    def show_statement(self):
        return self.statement
    def show_statement(self):
        for transaction in self.statement:
                       amount=transaction["amount"]
                       narration=transaction["narration"]
                       time=transaction["time"]
                       date=time.strftime("%d/%m/%y")
                       print(f"{date} : {narration} {amount}")
                       return self.statement


    def borrow(self,amount):
      if amount >0:
         return f"you can borrow"

      elif self.loan>0:
        return f"you cannot borrow"

      elif amount<0.1* self.balance:
     
          return f"you cannnot borrow"

    
      else:
          loan=amount*0.15
          self.loan=loan
          self.balance +amount=amount
          now=datetime.now()
          transaction={
            "amount":amount,
            "time":now,
            "narration":"you deposited"
      }
      self.statement.append(transaction)
      return f"Dear {self.name} you have {self.loan} your balance is {self.balance}" 

     

    def repay_loan(self,amount):
      
      if amount<0:
        return f"you have repaid your loan"
      elif amount<=self.loan:
          return  f"you have decreased your loan by {amount}"

      elif amount>self.loan:
        return f"you have increased your loan by {amount}"
      
      else:
        difference=amount-self.loan
        self.loan=0
        self.deposit(difference)
        now=datetime.now()
        transaction={
            "amount":amount,
            "time":now,
            "narration":"you deposited"
      }
      self.statement.append(transaction)
      return f" you have repaid {self.loan} you have {self.loan} your balance is {self.balance}"

    # def transfer(self,Account,amount):
    #   fee=amount*0.05
    #   self.balance-=total
    #   Account.deposit(amount)
    #   total=amount+fee
    #   if total>self.balance:
    #     return f"your balance is {self.balance} and you need transfer at least {total} for this account"

    #   else:
        
    def transfer(self,account,amount):
        try:
            10+amount
        except TypeError:
            return f"The amount should be in figures"
        fee= amount*0.05
        total=amount + fee

        if amount<0:
            return f"You are not qualified to make a transfer"
        elif total>self.balance:
            return f"your balance is {self.balance} and you need atleast {total} for this transfer "
        else:
            account.deposit(200000)
            self.balance=total
            return f"The amount has been transferred to the account number"

class Mobile_money(Account):

      def __init__(self,name,Phone_number,service_provder):
        Account.__init__(name,Phone_number)
        self.service_provider=service_provder

      def buy_airtime(self,amount):
        try:
            10+amount
        except TypeError:
            return f"The anmount sghould be in figures"
        if amount<0:
            return f"You have insufficient funds"
        elif self.balance>amount:
            return f"Your balance is low to buy this amount of credit"
        else:
            self.balance-=amount
            return f"You have purchased airtime worth {amount} from {self.service_provider}. Your account balance is {self.balance}"        

