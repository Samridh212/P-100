class Atm(object):
  """
    blueprint for car
  """

  def __init__(self,AcNumber):
   self.AcNumber = AcNumber

  def CheckBalance(self):
    
    print("You Have a balance of 10000")

  def CashWithdrwal(self,amount):
      new_amount = 10000- amount
      print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))

  def CashDeposit(self,amount):
      new_amount = 10000 + amount
      print("you have deposited amount "+str(amount) +". Your remaining balance is "+ str(new_amount))

def main():
    Ac_Number = input("Enter your account number:- ")
    print("Choose your activity ")
    print("1.Balance Enquriy   2.Withdrawl  3.Deposit")
    activity = int(input("Enter Activity Number :- "))

    user = Atm(Ac_Number)

    if (activity == 1):
        user.CheckBalance()

    elif (activity == 2):
        amount = int(input("Enter the amount:- "))
        user.CashWithdrwal(amount)

    elif (activity == 3):
        amount =int(input("Enter The amount:- "))
        user.CashDeposit(amount)
        
    else:
        print("enter a valid number")



if __name__ == "__main__":
    main()

     

