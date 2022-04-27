class QuadraticEquation:
    #
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def getDiscriminant(self):
        discriminant = (self.__b ** 2) - (4 * self.__a * self.__c)
        return discriminant

    def getRoot1(self):
        root1 = (-(self.__b) + (self.getDiscriminant() ** 0.5)) / (2 * self.__a)
        return root1

    def getRoot2(self):
        root2 = (-(self.__b) - (self.getDiscriminant() ** 0.5)) / (2 * self.__a)
        return root2

    def getResult(self):
        disc = self.getDiscriminant()
        if disc > 0:
            print("The roots of the equation are", self.getRoot1(), self.getRoot2())
        
        elif disc == 0:
            print("The root of the equation is", self.getRoot1())
        
        else:
            print("The equation has no roots")