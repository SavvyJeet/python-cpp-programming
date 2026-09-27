class BankAccount():
  def __init__(self,holder,balance):
    if not holder.strip():
      raise ValueError("Account holder name cannot be empty.")
    if balance < 0:
      raise ValueError("Initial balance cannot be negative.")
    self.holder = holder.strip()      #holder.strip() removes the extra spaces from the starting and ending of the name given by the user
    self.balance = balance
    
  def deposit(self,amount):
    try:
      amount = float(amount)
      if amount <= 0:
        print("Deposit amount must be greater than 0.")
      else:
        self.balance+=amount
        print("Amount deposited successfully.")
    except ValueError:
      print("Please enter a correct amount to be deposited.")
    
  def withdraw(self,amount):
    try:
      amount = float(amount)
      if amount <= 0:
        print("You may only withdraw the amount greater than 0.")
      elif amount > self.balance:
        print("Insufficient Balance")
      else:
        self.balance-=amount
        print("Amount withdrawn successfully.")
    except ValueError:
      print("enter the correct withdrawal amount.")
      
  def show_balance(self):
    print("Your current account balance is",self.balance)
