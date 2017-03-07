class EquityBank():
  def deposit(): 
    pass
  
class Mbanking(coop_bank):
  def __init__(self):
    self.bankbalance = bankbalance
    
  
  def deposit(self,deposit):
    if type(deposit) == int and deposit !="":
      if deposit >= 0:
        self.bankbalance += deposit
        return self.bankbalance

      else:
        return 'Failed. Invalid Amount!'

    else:
      raise ValueError("Transaction cannot complete!Follow the instructions")

  def withdraw(self,amount):
    if type(amount) == int and amount != "":
      if amount > 0:
        if (self.bankbalance-amount) > 0:
          if (self.bankbalance -amount) > 200:
            self.bankbalance-=amount
            return self.bankbalance
          else:
            return 'You do not have sufficient funds in your account. Try Again!'
        else:
          return 'Enter Amount below Actual balance'
      else:
        return 'Invalid Amount'
    else:
      raise ValueError("Incomplete transaction!Follow the instructions")
      
class ChamaAccount(coop_bank):
  def __init__(self):
    self.bankbalance = bankbalance
    
  
  def deposit(self,deposit):
    if type(deposit) == int and deposit !="":
      if deposit >= 0:
        self.bankbalance += deposit
        return self.bankbalance

      else:
        return 'Invalid deposit amount'

    else:
      raise ValueError("Incomplete transaction!Follow the instructions")

  def withdraw(self,amount):
    if type(amount) ==  int and amount != "":
      if amount > 0:
        if (self.bankbalance-amount) > 0:

          self.bankbalance-=amount
          return self.bankbalance

        else:
          return 'Enter Amount below Actual balance'
      else:
        return 'Invalid withdraw amount'
    else:
      raise ValueError("Incomplete transaction!Follow the instructions")
jane=Mpesa()
jane.bankbalance=500
jane.deposit=600