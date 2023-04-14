class Atm:
    def _init__(self,total):
        self.total = total

class Machine:
    def __init__(self):
        self.__balance = 0
    
    def addAmount(self,money):
        self.__balance += money

    def takeAmount(self, money):
      if self.__balance < money:
        print('Insufficient Funds')
      else:
        self.__balance -= money
        

    def displayAmount(self):
        print(self.__balance)

p1 = Machine()
# p1.addAmount(20)
# p1.displayAmount()
print("Welcome to our Bank!")
while True:
  print("Press Q to add money to your balance!")
  print("Press W to check your current balance!")
  print("Press E to withdraw money from your balance!") 
  print("Press X to exit.")
  userInput = input("\n")
  if userInput == "x":
    break
    print('Goodbye, have a nice day!')   
  elif userInput == "q":
    kaching = int(input("Enter the amount you want to enter: \n"))
    p1.addAmount(kaching)
  elif userInput == "w":
    p1.displayAmount()
  elif userInput == "e":
    withdraw = int(input("Enter the amount you want to withdraw" ))
    p1.takeAmount(withdraw)
  else:
    print('Invalid response.\n')
      
        

