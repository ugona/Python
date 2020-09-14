# Q-1|

# length_cm = eval(input("Enter a length in centimeters: "))
# lenght_in = round(length_cm/2.54,2)
# if length_cm < 0:
#     print("The entry is invalid")
# else:
#     print("Length in inches: {}".format(lenght_in))

# Q-2|

# temperature = eval(input("Enter Temperature: "))
# units = input("Enter units (Celsius or Fahrenheit)")
# if units == "C" or units == "Celsius":
#     temp = (9/5*temperature)+32
#     print("The temperature is {0} Fahrenheit,".format(temp))
# elif units == "F" or units == "Fahrenheit":
#     temp= (5/9*(temperature-32))
#     print("The temperature is {0} Celsius   ,".format(temp))

# Q-3|

# temperature = eval(input("Enter a temperature in Celsius: "))
# if temperature< -273.15:
#     print("The temperature is invalid because it is below absolute zero")
# elif temperature == -273.15:
#     print("The temperature is absolute 0")
# elif 0<temperature<273.15:
#     print("The temperature is below freezing")
# elif temperature==0:
#     print("The temperature is at the freezing point")
# elif 0 < temperature < 100:
#     print("The temperature is in the normal range")
# elif temperature == 100:
#     print("The temperature is at the boiling point")
# elif temperature >100:
#     print("The temperature is above the boiling point")

# Q-4|

# credits =eval(input("How many credits they have taken: "))
# if credits <= 23:
#     print("Freshman")
# elif 24 <= credits <= 53:
#     print("sophomore")
# elif 54 <= credits <=83:
#     print("junior")
# elif credits >= 84:
#     print("Senior")

# Q-5|

# import random
# rand_num=random.randint(1,10)
# gue_num=eval(input("guess the number between 1 -10 : "))
# if rand_num == gue_num:
#     print("Hurrey.......You are right")
# else:
#     print("Wrong guess. The number is {}".format(rand_num))

# Q-6|
#
# items = eval(input("How many items you are buying: "))
# if items < 10:
#     print("The total cost is: $",items*12, sep="")
# elif 10 <= items <= 99:
#     print("The total cost is: $", items * 10, sep="")
# elif items >= 100:
#     print("The total cost is: $", items * 7, sep="")

# Q-7|
# num1,num2=eval(input("Enter the numbers seperated by comma: "))
# print(num1,num2)
# if abs(num1-num2)==0.001:
#     print("They are too close")
# else:print("Not close")

# Q-8|
# year = eval(input("Enter a year: "))
# if year%100 == 0:
#     if year%400 == 0:
#         print ("It's a leap year")
# elif year % 4 == 0:
#     print("Its a leap year")
# else:
#     print("Its not a leap year")

# Q-9|

# num=eval(input("Enter a number: "))
# for i in range(1,num):
#     if num%i == 0:
#         print(i)

# Q-10 |
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
#         print("Right!")
#     else:
#         print("Wrong. The answer is {}".format(a*b))

# Q-11|

# hour=eval(input("Enter hour: "))
# hour_ap=eval(input("am (1) or pm (2)?"))
# if not(hour_ap==1 or hour_ap==2):
#     print("Entered wrong input. Please try agian.....")
#     exit(15)
# hours_ahead=eval(input("How many hours ahead? "))
# new_hour=(hour+hours_ahead)%12
# new_hour_ap=((hour+hours_ahead)//12)+hour_ap
# if new_hour_ap%2==1:
#     print("New hour: {0} am".format(new_hour))
# else:
#     print("New hour: {0} pm".format(new_hour))

# Q-12|
from random import randint

# comp = 0
# human = 0
# x = randint(1, 3)
# for i in range(5):
#     y = eval(input("Rock (1)-Paper (2)-Scissors (3):"))
#     if x > y:
#         comp += 1
#     elif x < y:
#         human += 1
# if comp > human:
#     print("You lost the game")
# elif comp < human:
#     print("You won the match")
# else:
#     print("Match tie")

# import random
# r=["rock","paper", "scissors"]
# x=random.choice(r)
# print(x)
# input_human = input(print("PLease enter your choice Rock-Paper-Scissors: "))
# if r=="rock" and input_human=="Scissors":
    