# Q-1==================================================================================================
# Name = input("Enter you name=")
# for i in range(100):
#     print(Name)
# print("End of the Question 1")
# exit(0)
# =====================================================================================================

# Q-2| Write a program to fill the screen horizontally and vertically with your name.
# [Hint: add the option end='' into the print function to fill the screen horizontally.]

# Name = input("Enter your name=")
# for i in range(1000):
#     print(Name, end=" ")

# Q-3|==================================================================================================

# Name = input("Enter your name=")
# for i in range(1,101):
#     print(i, Name)

# Q-4|==================================================================================================

# for i in range(1,21):
#     print(i,"---",i*i)

# Q-5|==================================================================================================
# for i in range(8,90,3):
#     print(i, end=" ")

# Q-6|==================================================================================================
# for i in range(100,1,-2):
#     print(i, end=" ")

# Q-7|==================================================================================================

# for i in range(10):
#     print("A", end="")
# for i in range(7):
#     print("B", end="")
# for i in range(4):
#     print("C", end="")
#     print("D", end="")
# print("E", end="")
# for i in range(6):
#     print("F", end="")
# print("G")

# Q-8|==================================================================================================

# Name = str(input("Enter your name:"))
# iteration = eval(input("Enter number of times to print your name:"))
# for i in range(iteration):
#     print(i + 1, Name)

# Q-9|==================================================================================================

# f0 = 1
# f1 = 1
# num = eval(input("How many Fibonacci numbers to print (should be >2): "))
# if num > 2:
#     print(f0, f1, end=" ")
#     for i in range(2,num):
#         next_num = f1 + f0
#         print(next_num,end=" ")
#         f0 = f1
#         f1 = next_num
# else:
#     print("Number(n) should be greater than 2")

# Q-10|==================================================================================================

# hight_ = eval(input("Enter the hight of the box: "))
# width_ = eval(input("Enter the width of the box: "))
# for i in range(hight_):
#     print("*"*width_)

# Q-10|==================================================================================================

# hight_ = eval(input("Enter the hight of the box: "))
# width_ = eval(input("Enter the width of the box: "))
# for i in range(hight_):
#     if i ==0 or i==hight_-1:
#         print("*"*width_)
#     else:
#         print("*", " "*(width_-2),"*",sep="")

# Q-11|==================================================================================================

# hight_ = eval(input("Enter the hight of the box: "))
# symbol= input("Enter the symbol:")
# for i in range(hight_):
#     print(symbol*i)

# Q-12|==================================================================================================

# hight_ = eval(input("Enter the hight of the triangle: "))
# for i in range(hight_,0,-1):
#     print("*"*i)

# Q-13|==================================================================================================

# hight_ = eval(input("Enter the hight of the diamond: "))
# for i in range(hight_):
#     print(" "*(hight_-(i+1)),"* "*(i+1))
# for i in range(hight_-1):
#     print(" "*(i+1),"* "*(hight_-i-1))

# Q-14|==================================================================================================
# n = int(input("specify how large the \"A\" letter should be:"))
# for i in range(n):
#     print("  " * (n - i - 1) + "* ", end="")
#     if i >= 1:
#         if i == (n - 1) / 2:
#             print("* " * (2 * i - 1) + "*", end="")
#         else:
#             print("  " * (2 * i - 1) + "*", end="")
#     print()
