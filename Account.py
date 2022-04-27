class Account:
    def __init__(self, id = 0, balance = 100, annualInterestRate = 0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def getId(self):
        return self.__id

    def getBalance(self):
        return self.__balance

    def getAnnuaInterestRate(self):
        return self.__annualInterestRate

    def setId(self, id):
        self.__id = id

    def setBalance(self, balance):
        self.__balance = balance

    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate

    def getMonthlyInterestRate(self):
        monthlyInterestRate = (self.__annualInterestRate / 100) / 12
        return monthlyInterestRate

    def getMonthlyInterest(self):
        monthlyInterest = self.__balance * self.getMonthlyInterestRate()
        return monthlyInterest

    # def withdraw(self):
    #     print

    # def deposit(self):
    #     print