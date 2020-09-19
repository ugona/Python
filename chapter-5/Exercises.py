# count = 0
# for i in range(1, 101):
#     if ((i * i) % 10) == 1:
#         count += 1
# print(count)

# Q-2|
# count1 = 0
# count2 = 0
# for i in range(1, 101):
#     if ((i * i) % 10) == 4:
#         count1 += 1
#     if ((i * i) % 10) == 9:
#         count2 += 1
# print(count1,count2)

# Q-3|
# from math import log
#
# su = 0
# num = eval(input("Enter a value of n:"))
# for i in range(1, num + 1):
#     su = su + (1 / num)
# output = su - log(num, 2)
# print("The output= ",output)

# Q-4|
# sam = 0
# num = eval(input("Enter a value of n: "))
# for i in range(1, num + 1):
#     if i % 2 == 0:
#         sam = sam - i
#     else:
#         sam = sam + i
# print("The sum= ", sam)

# Q-5|
# Total=0
# num=eval(input("enter a number: "))
# for i in range(1,num):
#     if num%i==0:
#         Total=Total+i
# print("The sum of the divisors: ", Total)

# Q-6|

# num = eval(input("enter a number: "))
# print("The perfect numbers are: ", end="")
# for i in range(1, num + 1):
#     Total = 0
#     for j in range(1, i):
#         if i % j == 0:
#             Total = Total + j
#     if Total == i:
#         print(i, end=" ")

# Q-7|
# import math

# Total = 0
# num = eval(input("enter a number: "))
# for i in range(1, num):
#     if num % i == 0:
#         # print(i, end=" ")
#         root = math.sqrt(i)
#         if int(root + 0.5) ** 2 == i:
#             Total += 1
# if Total > 1:
#     print("The given Number is not square free")
# else:
#     print("The given Number is square free")

# Q-8|

# x,y,z=0,1,2
# x,y,z=y,z,x
# print(x,y,z)

# Q-9|
# import math
#
# count = 0
# n = 1000
# for i in range(1,n+1):
#     # sq_root=math.sqrt(i)
#     sq_root=i**(1/2)
#     qube_root=i**(1/3)
#     fifth_root = i ** (1 / 5)
#     if int(sq_root + 0.5) ** 2 == i:
#         count = count + 1
#     elif int(qube_root) ** 3 == i:
#         count = count + 1
#     elif int(fifth_root) ** 5 == i:
#         count = count + 1
# print(n-count)

# Q-10|
# import math
#
# list1 = []
# sort11_list = []
# summm = 0
# num = eval(input("Enter how many numbers you want to enter:"))
# for i in range(1, num + 1):
#     list1.append(eval(input("Please enter test-{} score:".format(i))))
# for i in range(1, num + 1):
#     if list1[i - 1] > 100:
#         print("\n" * 3)
#         print("Warning: value over 100 has been entered")
#         print("\n")
# list1.sort()
# print("The lowest and highest scores are:", list1[0], ",", list1[num - 1])
# print("The average of the scores:", math.fsum(list1) / num)
# print("second largest score is :", list1[num - 2])
# for i in range(2, num):
#     summm += list1[i]
# print("The avg of the test scores(omitted 2 lowest scores)", summm / (num - 2))

# Q-11|

# import math
# fact = math.factorial(3)
# print(fact)

# # Q-11| another way
# globals(total)
# def fact(n, total=0):
#     total = total + fact(n - 1)
#     return total
#
#
# fact(3)

# Q-12|
import random

# total_points = 0
#
# for i in range(1,6):
#     rand_num=eval(input("guess a random number between 1 and 10: "))
#     a = random.randint(1,10)
#     if a == rand_num:
#         total_points += 10
#     else:
#         total_points +=-1
# if total_points>0:
#     print("Total points = ",total_points)
# else:
#     print("\nYou lost the game.Total points = 0")

# Q-13 |
# right_ans=0
# wrong_ans=0
# print("----------------------")
# print(" Multipilcation Game")
# print("----------------------")
# print("")
# from random import randint
#
# for i in range(10):
#     a = randint(1, 10)
#     b = randint(1, 10)
#     print("Question {} :".format(i+1), end="")
#     x = eval(input("{0} X {1} = ".format(a,b)))
#     if x == a*b:
#         right_ans += 1
#         print("Right!")
#     else:
#         wrong_ans += 1
#         print("Wrong. The answer is {}".format(a*b))
# print("\nTotal count:\nRight Answers = {0}\nWrong Answers={1}".format(right_ans,wrong_ans))

#Q-14|

# import random
# a=random.randint(1,3)
# print(a)
# b=eval(input("Choose your number between 1 to 3:"))
# print("You have choosen ",b)
# for i in range(1,4):
#     if i == a:
#         print(i)
#     else:

        # Monty Hall Problem
        # Various comments are used to improve readability of code
# import random  # To choose and guess the probability of winning.
#
# doors = ["GOAT"] * 3  # Initializing each door with door
# goat_door = []
# switch_win = 0  # No. of times player wins by switching
# stick_win = 0  # No. of times player wins by sticking to initial choice
# j = 0
# while j < 100000:
#     x = random.randint(0, 2)  # xth door comprise of the prize
#     doors = ["GOAT"] * 3  # switching xth door with car
#     doors[x] = "CAR"
#     for i in range(3):
#         if doors[i] != "CAR":
#             goat_door.append(i)  # Appending all goat_door index to list
#         ch = random.randint(0, 2)
#             host_door = random.choice(goat_door)
#             while host_door == ch:
#                 host_door = random.choice(goat_door)
#             swap = random.randint(0, 1)  # To know whether player swaps or not
#             if (swap == 1):
#                 if doors[ch] == "GOAT":
#                     switch_win = switch_win + 1
#             else:
#                 if doors[ch] != "GOAT":
#                     stick_win = stick_win + 1
#             j = j + 1
#             doors.clear()
#             goat_door.clear()
#         print(switch_win, stick_win)


# x, y = 25, 50
# big = x if x < y else y
# print(big)

import re

# x="umamaheswararao"
# y=re.split()
# print(y)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'xznlwebgjhqdyvtkfuompciasr'
secret_message = input('Enter your message: ')
secret_message = secret_message.lower()
for c in secret_message:
    if c.isalpha():
        print(key[alphabet.index(c)],end='')
    else:
        print(c, end='')