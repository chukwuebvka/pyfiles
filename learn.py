# #3.1 maths fxs
# import math
# import re #import math module to use the math fxs

# print("exp(1.0) =", math.exp(1))
# print("log(3.78) =", math.log(math.e))
# print("sqrt(4.0) =", math.sqrt(4.0))


# #3.4
# amount = eval(input("Enter an amount(e.g 11.56)"))

# remainingAmount = int(amount * 100)

# numberOfOneDOllars = remainingAmount // 100    
# remainingAmount = remainingAmount % 100

# numberOfQuarters = remainingAmount // 25
# remainingAmount = remainingAmount %  25

# numberOfDimes = remainingAmount // 10
# remainingAmount = remainingAmount % 10

# numberOfNickels = remainingAmount // 5
# remainingAmount = remainingAmount % 5

# numbersOfPennies = remainingAmount

# print("Your amount", amount, "consists of", numberOfOneDOllars, "dollars", numberOfQuarters, "quarters", numberOfDimes, "dimes", numberOfNickels, "nickels", numbersOfPennies, "pennies")


#3.6
# amount = 12618.98
# interestRate = 0.0013
# interest = amount * interestRate
# print("Interest is", format(interest, ".2f"))


#4 selections
# import random
# # generate random numbers
# number1 = random.randint(0, 9)
# number2 = random.randint(0, 9)
# # swap numbers
# if number1 < number2:
#     number1, number2 = number2, number1
# # prompt user to enter answer
# answer = eval(input("What is " + str(number1) + " - " + str(number2) + "? "))
# # display result
# if number1 - number2 == answer:
#     print("You are correct!")
# else:
#     print("Wrong answer.\n", number1, "-", number2, "is", number1 - number2,)


# #4.8
# number = eval(input("Enter an integer: "))

# if number % 2 == 0 and number % 3 == 0:
#     print(number, "is divisible by 2 and 3")
# if number % 2 or number % 3 == 0:
#     print(number, "is divisible by 2 or 3")
# if (number % 2 == 0 or number % 3 == 0) and \
#         not (number % 2 == 0 and number % 3 == 0):
#     print(number, "is divisible by 2 or 3, but not both")


# #4.10
# import random

# # Generate a lottery number
# lottery = random.randint(0, 99)

# # Prompt user to guess number

# guess = eval(input("Enter your lottery pick (two digits): "))

# # Get digits from lottery
# lotteryDigit1 = lottery // 10
# lotteryDigit2 = lottery % 10

# # Get digits from guess
# guessDigit1 = guess // 10
# guessDigit2 = guess % 10

# print("The lottery number is", lottery)

# # Check the guess
# if guess == lottery:
#     print("Exact match: you win $10,000")
# elif (guessDigit2 == lotteryDigit1 and guessDigit1 == lotteryDigit2):
#     print("Match all digits: you win $3,000")
# elif (guessDigit1 == lotteryDigit1 or guessDigit1 == lotteryDigit2 or guessDigit2 == lotteryDigit1 or guessDigit2 == lotteryDigit2):
#     print("Match one digit: you win $1,000")
# else:
#     print("Sorry, no match")


# number = eval(input("Enter number: "))
# print("number is even" if number % 2 == 0 else "number is odd")

# #5 Loops
# from re import I


# count = 0
# while count < 2:
#     print("Programming is fun!")
#     count += 1

# sum = 0
# i = 1
# while i < 10:
#     sum = sum + i # += i
#     i = i + 1
# print("sum is", sum) # sum is 45


# import random

# # Generate two random single-digit integers
# number1 = random.randint(0, 9)
# number2 = random.randint(0, 9)

# # Swap to highest number
# if number1 < number2:
#     number1, number2 = number2, number1

# # Prompt student to answer
# answer = eval(input("What is " + str(number1) + " - " + str(number2) + "? "))

# # Repeatedly ask the question until the answer is correct
# while number1 - number2 != answer:
#     answer = eval(input("Wrong answer. Try again. What is " + str(number1) + " - " + str(number2) + "? "))

# print("You got it!")


# import random

# # Generate random number
# number = random.randint(0, 100)

# print("Guess a number between 0 and 100")

# guess = -1
# while guess != number:
#     # Prompt the use rto guess the number
#     guess = eval(input("Enter your guess: "))

#     if guess == number:
#         print("Yes, the number is", number)
#     elif guess > number:
#         print("Your guess is too high")
#     else:
#         print("Your guess is too low ")


# 5.4
# import random
# import time

# correctCount = 0
# count = 0
# NUMBER_OF_QUESTIONS = 5

# startTime = time.time()

# #while count < NUMBER_OF_QUESTIONS:
# continueLoop = "Y" #**
# while continueLoop == "Y": #**
#     # Generate two random single-digit integers
#     number1 = random.randint(0, 9)
#     number2 = random.randint(0, 9)

#     # Swap highest
#     if number1 < number2:
#         number1, number2 = number2, number1

#     # Prompt user's answer
#     answer = eval(input("What is " + str(number1) + " - " + str(number2) + "? "))

#     # Grade the answer and display result
#     if number1 - number2 == answer:
#         print("You're correct!")
#         correctCount += 1
#     else:
#         print("Your answer is wrong", number1, "-", number2, "is", number1 - number2)

#     # Increase count
#     count += 1

#     # Prompt the user for confirmation **
#     continueLoop = input("Enter Y to continue and N to quit: ")

# endTime = time.time()
# testTime = int(endTime - startTime)
# print("You got", correctCount, "out of", NUMBER_OF_QUESTIONS, "\nTest time is", testTime, "seconds")


#5.5
# data = eval(input("Enter an integer (the input ends if it is 0): "))

# # Keep reading data until the input is 0
# sum = 0
# while data != 0:
#     sum += data

#     data = eval(input("Enter an integer (the input ends if it is 0): "))

# print("The sum is", sum)

#5.3
# for i in range(10):
#     print(i)

#5.4
# print("         Multiplication Table")
# # Display the number title
# print("  |", end = '')
# for j in range(1, 10):
#     print(" ", j, end = '')
# print() # Jump to new line
# print("=======================================")

# # Display table body
# for i in range(1, 10):
#     print(i, "|", end = '')
#     for j in range(1, 10):
#         # Display the product and align properly
#         print(format(i * j, "4d"), end = '')
#     print() # Jump to new line


# i = 5
# while i >= 1: 
#     num = 1
#     for j in range(1, i + 1): 
#         print(num, end = "xxx")
#         num *= 2
#     print()
#     i -= 1


# for i in range(1, 5): 
#     j = 0
#     while j < i: 
#         print(j, end = " ")
#         j += 1


# Prompt user to enter two integers
# n1 = eval(input("Enter first integer: "))
# n2 = eval(input("Enter second integer: "))

# gcd = 1
# k = 2
# while k <= n1 and k <= n2:
#     if n1 % k == 0 and n2 % k == 0:
#         gcd = k
#     k += 1

# print("The greatest common divisor for", n1, "and", n2, "is", gcd)


# year = 0
# fees = 42000

# while fees < 84000:
#     year += 1
#     fees = fees * 1.07

# print("Fees will be doubled in", year, "years")
# print("Fees will be #" + format(fees, ".2f"), "in", year, "years")


# sum = 0
# number = 0

# while number < 40:
#     number += 1
#     sum += number
#     if sum >= 200:
#         break

# print("The number is", number)
# print("The sum is", sum)


# sum = 0
# number = 0

# while number < 20:
#     number += 1
#     if number == 9 or number == 11:
#         continue
#     sum += number

# print("The number is", number)
# print("The sum is", sum)



# 6 - fuctions
# def sum(i1, i2):
#     result = 0
#     for i in range(i1, i2 + 1):
#         result += i

#     return result

# def main():
#     print("Sum from 1 to 10 is", sum(1, 10))
#     print("Sum from 20 to 37 is", sum(20, 37))
#     print("Sum from 35 to 49 is", sum(35, 49))

# main()


#6.1
# def max(num1, num2):
#     if num1 > num2:
#         result = num1
#     else:
#         result = num2
    
#     return result

# def main():
#     i = 10
#     j = 7
#     k = max(i, j) # Call the max function
#     print("The larger number of", i, "and", j, 'is', k)

# main() # Call the main function


# Print grade for the score
# def printGrade(score):
#     if score >= 70:
#         print('A')
#     elif score >= 60:
#         print('B')
#     elif score >= 50:
#         print('C')
#     elif score >= 45:
#         print('D')
#     else:
#         print('F')

# def main():
#     score = eval(input("Enter a score: "))
#     print("The grade is ", end = "")
#     printGrade(score)

# main() # Call the main function


# def getGrade(score):
#     if score >= 70:
#         return 'A'
#     elif score >= 60:
#         return 'B'
#     elif score >= 50:
#         return 'C'
#     elif score >= 45:
#         return 'D'
#     else:
#         return 'F'
# def main():
#     score = eval(input("Enter a score: "))
#     print("The grade is ", getGrade(score))

# main() # Call the main function


# Print grade for the score
# def printGrade(score):
#     if score < 0 or score > 100:
#         print("Invalid score")
#         return # Same as return None
        
#     if score >= 90.0:
#         print('A')
#     elif score >= 80.0:
#         print('B')
#     elif score >= 70.0:
#         print('C')
#     elif score >= 60.0:
#         print('D')
#     else:
#         print('F')

# def main():
#     score = eval(input("Enter a score: "))
#     print("The grade is ", printGrade(score))

# main() # Call the main function


# def main():
#     print(min(5, 6))

# def min(n1, n2):
#     smallest = n1
#     if n2 < smallest:
#         smallest = n2

# main() # Call the main function


# def main():
#     print((min(5, 6), min(51, 6)))

# def min(n1, n2):
#     smallest = n1
#     if n2 < smallest:
#         smallest = n2

# main() # Call the main function


# def function1(n, m):
#     function2(3.4)

# def function2(n):
#     if n > 0:
#         return 1
#     elif n == 0:
#         return 0
#     elif n < 0:
#         return -1
#     function1(2, 3)


# def nPrintln(message, n):
#     for i in range(n):
#         print(message)


# def main():
#     max = 0
#     getMax(1, 2, max)
#     print(max)

# def getMax(value1, value2, max):
#     if value1 > value2:
#         max = value1
#     else:
#         max = value2

# main()


# def main():
#     i = 1
#     while i <= 6:
#         print(function1(i, 2))
#         i += 1

# def function1(i, num):
#     line = ""
#     for j in range(1, i):
#         line += str(num) + " "
#         num *= 2
#     return line

# main()


# def main():
#     i = 0
#     while i <= 4:
#         function1(i)
#         i += 1
        
#         print("i is", i)

# def function1(i):
#     line = " "
#     while i >= 1:
#         if i % 3 != 0:
#             line += str(i) + " "
#             i -= 1
        
#     print(line)

# main()


# def main():
#     # Initialize times
#     times = 3
#     print("Before the call, variable", "times is", times)
    
#     # Invoke nPrintln and display times 
#     nPrint("Welcome to CS!", times)
#     print("After the call, variable", "times is", times)

# # Print the message n times
# def nPrint(message, n):
#     while n > 0:
#         print("n = ", n)
#         print(message)
#         n -= 1

# main()


#6.5
# from GCDFunction import gcd # Import the gcd function

# # Prompt the user to enter two integers
# n1 = eval(input("Enter the first integer: "))
# n2 = eval(input("Enter the second integer: "))

# print("The greatest common divisor for", n1, "and", n2, "is", gcd(n1, n2))


#6.7
# # Check whether number is prime
# def isPrime(number):
#     divisor = 2
#     while divisor <= number / 2:
#         if number % divisor == 0:
#             # If true, number is not a prime
#             return False # number is not a prime
#         divisor += 1

#     return True # number is prime

# def printPrimeNumbers(numberOfPrimes):
#     NUMBER_OF_PRIMES = 50 # Number of primes to display
#     NUMBER_OF_PRIMES_PER_LINE = 10 # Display 10 per line
#     count = 0 # Count the number of prime numbers
#     number = 2 # A number to be tested for primeness

#     # Repeatedly find prime numbers
#     while count < numberOfPrimes:
#         # Print the prime number and increase the count
#         if isPrime(number):
#             count += 1 # Increase count

#             print(number, end = " ")
#             if count % NUMBER_OF_PRIMES_PER_LINE == 0:
#                 # Print the number and advance to the new line
#                 print()

#         # Check if the next number is prime
#         number += 1

# def main():
#     print("The first 50 prime numbers are")
#     printPrimeNumbers(50)

# main() # Call the main function


# 6.8
# # Convert a decimal to a hex as a string
# def decimalToHex(decimalValue):
#     hex = " "

#     while decimalValue != 0:
#         hexValue = decimalValue % 16
#         hex = toHexChar(hexValue) + hex
#         decimalValue = decimalValue // 16

#     return hex

# # Convert an integer into a single hex digit as a character
# def toHexChar(hexValue):
#     if 0 <= hexValue <= 9:
#         return chr(hexValue + ord('0'))
#     else:
#         return chr(hexValue - 10 + ord('A'))

# def main():
#     # Prompt the user to enter a decimal integer
#     decimalValue = eval(input("Enter a decimal number: "))

#     print("The hex number for decimal", decimalValue, "is", decimalToHex(decimalValue))

# main() # Call the main function


# 6.9
# def printArea(width = 1, height = 2):
#     area = width * height
#     print("width:", width, "\theight:", height, "\tarea:", area)

# printArea()
# printArea(3, 5)
# printArea(width = 3.4)
# printArea(height = 7.3)
# printArea(width = 4, height = 6)


# def f(w = 1, h =2):
#     print(w, h)

# f()
# f(w = 5)
# f(h = 24)
# f(4, 5)


# def main():
#     nPrintln(5)

# def nPrintln(n, message = "Welcome to Python!"):
#     for i in range(n):
#         print(message)

# main() # Call the main function


# 6.10
# def sort(number1, number2):
#     if number1 < number2:
#         return number1, number2
#     else:
#         return number2, number1

# n1, n2 = sort(3, 2)
# print("n1 is", n1)
# print("n2 is", n2)


# def f(x, y):
#     return x + y, x - y, x * y, x / y

# t1, t2, t3, t4 = f(9, 5)
# print(t1, t2, t3, t4)


# 6.11
# import RandomCharacter

# NUMBER_OF_CHARS = 175 # Number of character to generate
# CHARS_PER_LINE = 25 # Number of character to display per line

# # Print random characters between 'a' and 'z', 25 chars per line
# for i in range(NUMBER_OF_CHARS):
#     print(RandomCharacter.getRandomLowerCaseLetter(), end = " ")
#     if (i + 1) % CHARS_PER_LINE == 0:
#         print() # Jump to the new line


# 6.13
# # Print the calendar for a month in a year
# def printMonth(year, month):
#     # Print the headings of the calendar
#     printMonthTitle(year, month)

#     # Print the body of the calendar
#     printMonthBody(year, month)

# # Print the month title, e.g., May 1999
# def printMonthTitle(year, month):
#     print("         ", getMonthName(month), " ", year)
#     print("=============================")
#     print(" Sun Mon Tue Wed Thu Fri Sat")

# # Print month body
# def printMonthBody(year,month):
#     # Get start day of the week for the first date of the month
#     startDay = getStartDay(year, month)

#     # Get number of days in a month
#     numberOfDaysInMonth = getNumberOfDaysInMonth(year, month)

#     # Pad space before the first day of the month
#     i = 0
#     for i in range (0, startDay):
#         print("   ", end = " ")

#     for i in range(1, numberOfDaysInMonth + 1):
#         print(format(i, "4d"), end = "")

#         if (i + startDay) % 7 == 0:
#             print() # Jump to the new line

# # Get the English name for the month
# def getMonthName(month):
#     if month == 1:
#         monthName = "January"
#     elif month == 2:
#         monthName = "February"
#     elif month == 3:
#         monthName = "March"
#     elif month == 4:
#         monthName = "April"
#     elif month == 5:
#         monthName = "May"
#     elif month == 6:
#         monthName = "June"
#     elif month == 7:
#         monthName = "July"
#     elif month == 8:
#         monthName = "August"
#     elif month == 9:
#         monthName = "September"
#     elif month == 10:
#         monthName = "October"
#     elif month == 11:
#         monthName = "November"
#     else:
#         monthName = "December"

#     return monthName

# # Get the start day of month/1/year
# def getStartDay(year, month):
#     START_DAY_FOR_JAN_1_1800 = 3

#     # Get total number of days from 1/1/1800 to month/1/year
#     totalNumberOfDays = getTotalNumberOfDays(year, month)

#     # Return the start day fot month/1/year
#     return (totalNumberOfDays + START_DAY_FOR_JAN_1_1800) % 7

# # Get the total number of days since January 1, 1800
# def getTotalNumberOfDays(year, month):
#     total = 0

#     # Get the total days from 1800 to 1/1/year
#     for i in range(1800, year):
#         if isLeapYear(i):
#             total = total + 366
#         else:
#             total = total + 365

#     # Add days from Jan to the month prior to the calendar month
#     for i in range(1, month):
#         total = total + getNumberOfDaysInMonth(year, i)

#     return total

# # Get the number of days in a month
# def getNumberOfDaysInMonth(year, month):
#     if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
#         return 31
    
#     if month == 4 or month == 6 or month == 9 or month == 11:
#         return 30

#     if month == 2:
#         return 29 if isLeapYear(year) else 28

#     return 0 # If month is incorrect

# # Determine if it is a leap year
# def isLeapYear(year):
#     return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

# def main():
#     # Prompt the user to enter year and month
#     year = eval(input("Enter full year (e.g., 2001): "))
#     month = eval(input("Enter month (between 1 and 12): "))

#     # Print calendar for the month of the year
#     printMonth(year, month)

# main() # Call the main function



# 7 - Objects and Classes

# 7.1
# from Circle import Circle
# c = Circle(5)
# c.radius
# c.getPerimeter()
# c.getArea()
# print("Area is", Circle(5).getArea())
# print("Preimeter is", Circle(5).getPerimeter())


# 7.2
# from Circle import Circle

# def main():
#     # Create a circle with radius 1
#     circle1 = Circle()
#     print("The area of the circle of radius", circle1.radius, "is", circle1.getArea())

#     # Create a circle with radius 25
#     circle2 = Circle(25)
#     print("The area of the circle of radius", circle2.radius, "is", circle2.getArea())

#     # Create a circle with radius 125
#     circle3 = Circle(125)
#     print("The area of the circle of radius", circle3.radius, "is", circle3.getArea())

#     # Modify circle radius
#     circle2.radius = 100 # or circle2.setRadius(100)
#     print("The area of the circle of radius", circle2.radius, "is", circle2.getArea())

# main() # Call the main function


# 7.4
# from TV import TV

# def main():
#     tv1 = TV()
#     tv1.turnOn()
#     tv1.setChannel(30)
#     tv1.channelUp()
#     tv1.setVolume(3)
#     tv1.volumeUp()

#     tv2 = TV()
#     tv2.turnOn()
#     tv2.channelUp()
#     tv2.channelUp()
#     tv2.volumeUp()

#     print("tv1's channel is", tv1.getChannel(), "and volume level is", tv1.getVolumeLevel())
#     print("tv2's channel is", tv2.getChannel(), "and volume level is", tv2.getVolumeLevel())

# main() # Call the main function


# 7.5
# from Circle import Circle

# def main():
#     # Create a Circle object with radius 1
#     myCircle = Circle()

#     # Print areas for radius 1,2,3,4, and 5
#     n = 5
#     printAreas(myCircle, n)

#     # Display myCircle.radius and times
#     print("\nRadius is", myCircle.radius)
#     print("n is", n)

# # Print a table of areas for radius
# def printAreas(c, times):
#     print("Radius \t\tArea")
#     while times >= 1:
#         print(c.radius, "\t\t", c.getArea())
#         c.radius += 1
#         times -= 1

# main() # Call the main function


# class Count:
#     def __init__(self, count = 0):
#         self.count = count

# def main():
#     c = Count()
#     n = 1
#     m(c, n)
    
#     print("count is", c.count)
#     print("n is", n)

# def m(c, n):
#     c = Count(5) 
#     n = 3

# main() # Call the main function


# from Circle import Circle
# c = Circle(5)
# print(c.getRadius())


# class A:
#     def __init__(self, on):
#         self.on = not on


# def main():
#     a = A(False)
#     print(a.on)

# main() # Call the main function


# class A:
#     def __init__(self, i):
#         self.i = i

# def main():
#     a = A(5)
#     print(a.i)

# main() # Call the main function


# def main():
#     a = A()
#     a.print()

# class A:
#     def __init__(self, newS = "Welcome"):
#         self.__s = newS

#     def print(self):
#         print(self.__s)

# main() # Call the main function


# 7.6 Class Abstraction and Encapsulation

# 7.7
# from Loan import Loan

# def main():
#     # Enter yearly interest rate
#     annualInterestRate = eval(input("Enter yearly interest rate, for example, 7.25: "))

#     # Enter number of years
#     numberOfYears = eval(input("Enter number of years as an integer: "))

#     # Enter loan amount
#     loanAount = eval(input("Enter loan amount, for example, 120000.95: "))
    
#     # Enter a borrower
#     borrower = input("Enter a borrower's name: ")

#     # Create a loan object
#     loan = Loan(annualInterestRate, numberOfYears, loanAount, borrower)

#     # Display loan date, monthly payment, and total payment
#     print("The loan is for", loan.getBorrower())
#     print("The monthly payment is", format(loan.getMonthlyPayment(), ".2f"))
#     print("The total payment is", format(loan.getTotalPayment(), ".2f"))

# main() # Call the main function


# 7.9
# from BMI import BMI

# def main():
#     bmi1 = BMI("John Doe", 18, 145, 70)
#     print("The BMI for", bmi1.getName(), "is", bmi1.getBMI(), bmi1.getStatus())

#     bmi2 = BMI("Peter king", 50, 215, 70)
#     print("The BMI for", bmi2.getName(), "is", bmi2.getBMI(), bmi2.getStatus())

# main() # Call the main function


# from Circle import Circle

# c = Circle(5)

# print(c.getRadius())


# class Person:
#     def getInfo(self):
#         return "Person"
        
#     def printPerson(self):
#         print(self.getInfo())

# class Student(Person):
#     def getInfo(self):
#         return "Student"

# Person().printPerson()
# Student().printPerson()


# class Person:
#     def __getInfo(self):
#         return "Person"
        
#     def printPerson(self):
#         print(self.__getInfo())

# class Student(Person):
#     def __getInfo(self):
#         return "Student"

# Person().printPerson()
# Student().printPerson()



aTuple = (1, 'Jhon', 1+3j)
print(type(aTuple[2:3]))