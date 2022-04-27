# 7.1
# from Rectangle import Rectangle

# def main():
#     # Create a rectangle with width = 1 and height = 2
#     rectangle1 = Rectangle()
#     print("The rectangle with width", rectangle1.width, "and height", rectangle1.height, "has the area", rectangle1.getArea(), "and perimeter", rectangle1.getPerimeter())

#     # Create a rectangle with width = 4 and height = 40
#     rectangle2 = Rectangle(4, 40)
#     print("The rectangle with width", rectangle2.width, "and height", rectangle2.height, "has the area", rectangle2.getArea(), "and perimeter", rectangle2.getPerimeter())

#     # Create a rectangle with width = 3.5 amd height = 35.7
#     rectangle3 = Rectangle(3.5, 35.7)
#     print("The rectangle with width", rectangle3.width, "and height", rectangle3.height, "has the area", rectangle3.getArea(), "and perimeter", rectangle3.getPerimeter())

# main() # Call the main function



# 7.6
# from QuadraticEquation import QuadraticEquation

# def main():
#     # Prompt user to enter values
#     a = eval(input("Enter the value of a: "))
#     b = eval(input("Enter the value of b: "))
#     c = eval(input("Enter the value of c: "))

#     res = QuadraticEquation(a, b, c)
#     res.getResult()
    
# main() # Call the main function


# 7.7
# from LinearEquation import LinearEquation

# def main():
#     # Prompt user to enter values
#     a = eval(input("Enter the value of a: "))
#     b = eval(input("Enter the value of b: "))
#     c = eval(input("Enter the value of c: "))
#     d = eval(input("Enter the value of d: "))
#     e = eval(input("Enter the value of e: "))
#     f = eval(input("Enter the value of f: "))

#     res = LinearEquation(a, b, c, d, e, f)
#     res.getResult()

# main() # Call the main function


# 7.2
# from Stock import Stock

# def main():
#     stock = Stock("INTC", "Intel Corporation", 20.5, 20.35)
#     print("The previous closing price is", stock.getPreviousClosingPrice(), "the new current price is", stock.getCurrentPrice(), "and the price change percentage is", stock.getChangePercent())

# main() # Call the main function


# 7.3
from Account import Account

def main():
    account = Account(1122, 20000, 4.5)
    print("Account id: ", account.getId(), "\n")
    print("Account balance: ", account.getBalance(), "\n")
    print("Monthly interest rate: ", account.getMonthlyInterestRate(), "\n")
    print("Monthly interest: ", account.getMonthlyInterest(), "\n")

main() # Call the main function