# Q-20|
# import datetime

# time = input("Please enter the time: ")
# timezones=["Eastern","Central","Mountain","Pacific"]
# timezone_diff=[]
# st_zone = input("Starting zone: ")
# datetime_eastren= datetime.now(time)
#
# end_zone = input("Ending zone: ")

# Q-21|
# message = input("Please enter the text: ")
# message_even=""
# message_odd=""
# for i in range(len(message)):
#     if i%2 == 0:
#         message_even = message_even+message[i]
#     else:
#         message_odd = message_odd+message[i]
# print(message_even+message_odd)

# message=input("Enter a message to decrypt: ")
# second_half_len=len(message)//2
# first_half_len=len(message)-second_half_len
# first_half_message=message[0:first_half_len]
# second_half_message=message[first_half_len:]
#
# for i in range(first_half_len):
#     print(first_half_message[i], end='')
#     if i<second_half_len:
#         print(second_half_message[i],end="")