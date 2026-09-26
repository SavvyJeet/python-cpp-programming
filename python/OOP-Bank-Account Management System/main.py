class BankAccount():
  def __init__(self,holder,balance):
    self.holder = holder
    self.balance = balance
    
  def deposit(self,amount):
    self.balance+=amount
    
  def withdraw(self,amount):
    if amount > self.balance:
      print("Insufficient Balance")
    else:
      self.balance-=amount
      
  def show_balance(self):
    print("Your current account balance is"self.balance)
