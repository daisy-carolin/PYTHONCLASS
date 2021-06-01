from datetime import datetime
class Account:
    def __init__(self,name,phone_number):
        self.name=name
        self.phone_number=phone_number

        self.balance=0
        self.statement=[]

    def show_balance(self):
      return f"Hello {self.name} your balance {self.balance} "

    def deposit(self,amount):
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




                        

