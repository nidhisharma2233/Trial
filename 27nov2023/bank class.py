class BankAccount:
  def __init__(self,an,name,balance):
    self.__account_n=an
    self.__name=name
    self.__balance=balance
  def deposit(self,amount):
    self.dep_balance=self.__balance+amount

  def withdraw(self,amount):
    self.balance=self.dep_balance-amount

  def display(self):
    print("Account Number :",self.__account_n)
    print("Account Name :",self.__name)
    print("Account Balance :", self.balance)


newAccount = BankAccount(2178514584, "Mandy" , 2000)

newAccount.deposit(1000)

newAccount.withdraw(700)




newAccount.display()