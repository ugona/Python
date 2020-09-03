# Q-1|
# from random import randint
# for i in range(50):
#     print(randint(3, 6))

# Q-2|

# from random import randint
# x = randint(1,50)
# y = randint(2,5)
# result = x**y
# print("The value of x=",x)
# print("The value of y=",y)
# print("The computed value of x**y is:",result)

# Q-3|

# from random import randint
# rand_num=randint(1,10)
# print("Printing your name {0} time(s)".format(rand_num))
# for i in range(rand_num):
#     print("Umamaheswararao")

# Q-4|

# import random
# count = eval(input("Enter the number of values to print: "))
# for i in range(count):
#     print(round(random.uniform(1,10),2))

# Q-5|

# from random import randint
#
# for i in range(1, 51):
#     print(i, "| random integer between (1,{0}) is ".format(i + 1), randint(1, (i + 1)))

# Q-6|

# x = eval(input("x="))
# y = eval(input("y="))
# print("result=",abs(x-y)/(x+y))

# Q-7|
# value = eval(input("Enter a value between -180 and +180 degree: "))
# if (-180) <= value <= 180:
#     print("The equivalent angle is: {} degree".format(value + 180))
# else:
#     print("Wrong input. Please try again")

# Q-8|

# seconds = eval(input("Enter seconds:"))
# print("Output : {0} minutes {1} seconds".format(seconds//60,seconds%60))

# Q-9|

# hour = eval(input("Enter hour: "))
# ahead = eval(input("How many hours ahead? "))
# print("New hour: {} o' clock".format((hour+ahead)%12))

# Q-10.a|

# power = eval(input("Enter a power: "))
# result = 2**power
# last_dig = result % 10
# print("The last digit of 2 raised to that power: ",last_dig)

# Q-10.b|

# power = eval(input("Enter a power: "))
# result = 2**power
# last_dig = result % 100
# print("The last two digits of 2 raised to that power: ",last_dig)

# Q-10.c|

# power = eval(input("Enter a power: "))
# digits = eval(input("how many last digits you want: "))
# result = 2**power
# last_dig = result % (10**digits)
# print("The last {} digit(s) of 2 raised to that power: ".format(digits),last_dig)

# Q-11|

# weight_kg = eval(input("enter a weight in kilograms: "))
# weight_lb = round(weight_kg * 2.204623, 1)
# print("Weight in pounds: ",weight_lb)

# Q-11|

# weight_kg = eval(input("enter a weight in kilograms: "))
# weight_lb = round(weight_kg * 2.204623, None)
# last_digit = weight_lb%10
# if last_digit > 5:
#     weight_lb +=(10-last_digit)
# else:
#     weight_lb -= last_digit
# print("Weight in pounds: ", weight_lb)

# Q-12|

# import math
# num = eval(input("Please enter the number:"))
# print("The factorial of the number: ",math.factorial(num))

# Q-12..|
# num = int(input("Enter a number: "))
# factorial = 1
# if num < 0:
#     print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#     print("The factorial of 0 is 1")
# else:
#     for i in range(1, num + 1):
#         factorial = factorial * i
#     print("The factorial of", num, "is", factorial)

# Q-13|
# import math
# num = eval(input("Enter a num: "))
# print("sin({}) in radians= ".format(num),math.sin(num))
# print("cos({}) in radians= ".format(num),math.cos(num))
# print("tan({}) in radians= ".format(num),math.tan(num))

# Q-14|
# import math
#
# degrees = eval(input("enter an angle in degrees: "))
# radians = degrees * math.pi / 180
# print(math.sin(radians))

# Q-15|
# import math
# for degrees in range(0,360,15):
#     radians = degrees * math.pi / 180
#     print(degrees," --- ",round(math.sin(radians),4),round(math.cos(radians),4))

# Q-16|
# import math
#
# Y = eval(input("Please enter the year: "))
# C = Y // 100
# m = (15 + C - math.floor(C / 4) - math.floor(((8 * C) + 13) / 25)) % 30
# n = (4 + C - math.floor(C / 4)) % 7
# a = Y % 4
# b = Y % 7
# c = Y % 19
# d = ((19 * c) + m) % 30
# e = ((2 * a) + (4 * b) + (6 * d) + n) % 7
# bit = 0
# list1 = [2, 5, 10, 13, 16, 21, 24, 39]
# for i in list1:
#     if i == m:
#         bit += 1
# if d == 29 and e == 6:
#     print("easter will be on April 19")
# elif d == 28 and e == 6 and bit == 1:
#     print("The easter will be on April 18")
# else:
#     print("The easter will be on either April {0}".format(d + e - 9))

# Q-17|

# year = eval(input("Please enter a year: "))
# leap_years_count = 0
# for i in range(1600, year):
#     if i % 100 == 0:
#         if i % 400 == 0:
#             leap_years_count += 1
#     elif i % 4 == 0:
#         leap_years_count += 1
# print("The number of leap years between 1600 and {}: ".format(year), leap_years_count)

# Q-17|

# change=eval(input("Enter an amount of change less than $1.00 in cents: "))
# dimes = change//10
# nickels = (change % 10) // 5
# pennies = (change % 10) % 5
# print("You will get:\ndimes={0}\nNickels={1}\nPennies={2}".format(dimes, nickels, pennies))

# Q-18|
# hight1 = eval(input("Please enter the hight1 of the rectangle: "))
# width = eval(input("Please enter the width of the rectangle: "))
# i=0
# for k in range(hight1):
#     for j in range(width):
#         print(i, end="  ")
#         i = (i+1)%10
#     print("")
