class LinearEquation:
    #
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def getD(self):
        return self.__d

    def getE(self):
        return self.__e

    def getF(self):
        return self.__f

    def isSolvable(self):
        isSolvable = (self.__a * self.__d) - (self.__b * self.__c)
        return isSolvable

    def getX(self):
        x = ((self.__e * self.__d) - (self.__b * self.__f)) / self.isSolvable()
        return x

    def getY(self):
        y = ((self.__a * self.__f) - (self.__e * self.__c)) / self.isSolvable()
        return y

    def getResult(self):
        solve = self.isSolvable()
        if solve == 0:
            print("The equation has no solution")

        else:
            print("The solution to the equation is x = ", self.getX(), "and y = ", self.getY())