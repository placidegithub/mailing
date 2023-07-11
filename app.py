# print("Henry Placide")
# print('o----')
# print(' ||||')
# print('*' * 10)

# Variables
#----------------------------------------------------------------

# price = 10
# price = 20
# name = "Placide"
# pipo = 4.5
# is_published = False
# print(pipo)
# name = 'John Smith'
# age = 20
# is_new = True

# how to get input form a user
#------------------------------------------------------------------

# name = input("What is your name? ")
# print("Hi " + name)

# name = input("What is your name? ")
# color = input("What is your favorite color do like? ")
# print(name + " likes " + color)

# birth_year = input("Birth year: ")
# age = 2023 - int(birth_year)
# print(age)

# weight_lbs = input("weight in (lbs) : ")
# weight_kg = int(weight_lbs) * 0.45
# print(weight_kg)

# multiple line of string
#---------------------------------------------------------------------

# course = '''
# hi ma best friend !,
# I wanna to great you .
# you have made wonders last time too much...
# '''
# print(course)

# course = 'Python for Beginners'
# print(course[:])
#
# name = 'Lopez Jennifer'
# print(name[1:-1])

# format string
#-----------------------------------------------------------------------

# first = 'John'
# last = 'Smith'
# msg = f'{first} [{last}] is a colder'
# print(msg)

# string method
#------------------------------------------------------------------------

# course = 'Python for Beginners'
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course)
# print(course.find('P'))
# print(course.find('Beginners'))
# print(course.replace('Beginners', 'Absolute Beginners'))
# print(course.join('Python'))
# print(course.__sizeof__())e
# print('Python' in course)
# print(course.title())

# Arithmetic Operator
#-------------------------------------------------------------------------

# print(10 + 3)
# print(10 - 3)
# print(10 / 3)
# print(10 // 3)
# print(10 * 3)
# print(10 ** 3)

# x = 10
# x = x + 3
# x += 3
# print(x)

# # Math function
#------------------------------------------------------------------------

# import math
# x = 2.9
# print(round(x))
# print(math.floor(x))
# print(math.ceil(x))
# print(math.fabs(x))

# if statement
#----------------------------------------------------------------------------

# is_hot = False
# is_cold = False
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
#     print("Enjoy your day")
#
# elif is_cold:
#     print("It's a cold day")
#     print("Enjoy your weekend")
#
# else:
#     print("Enjoy your lovely day!")

# price = 1000000
# has_good_credit = True
#
# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
#
# print(f"Down payment: ${down_payment}")

# logical operator AND OR NOT
#--------------------------------------------------------------------

# has_high_income = True
# has_good_credit = True
#
# if has_high_income and has_good_credit:
#     print("You are eligible for apply a loan")
# else:
#     print("You are not eligible for apply a loan")

#
# has_high_income = True
# has_good_credit = False
#
# if has_high_income or has_good_credit:
#     print("You are eligible for apply a loan")
# else:
#     print("You are not eligible for apply a loan")

# has_good_credit = True
# # has_criminal_record = False
# #
# # if has_good_credit and not has_criminal_record:
# #     print("You are eligible for apply a loan")
# # else:
# #     print("You are not eligible for apply a loan")

# comparison operator: <, >, == , ! =
#---------------------------------------------------------------------------

# temperature = 30
#
# if temperature > 30:
#     print("It's a hot day")
# else:
#
#     print("It's a cold day")

# name = "John smith"
# if len(name) < 3:
#     print("name must be at least 3 characters")
# elif len(name) > 50:
#     print("name must be a maximum of 50 characters")
# else:
#     print("name looks good!")

# weight = int(input("weight: "))
# unit = input("(L)bs or (K)kg: ")
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"you has {weight * 0.45} in kilos")
# else:
#     converted = weight / 0.45
#     print(f"you has {weight / 0.45} in pounds")

# while loop
#-------------------------------------------------------------------------

# i = 1
# while i <= 5:
#     print(i)
#     i = i + 1
# print("Done!")
# pattern in while loop

# i = 1
# while i <= 5:
#     print("* " * i)
#     i += 1

# Guessing game
#----------------------------------------------------------------------------

# secret_number = 9
# guess_count_number = 0
# guess_limit_number = 3
# while guess_count_number < guess_limit_number:
#     guess_number = int(input("Guess: "))
#     guess_count_number += 1
#     if guess_number == secret_number:
#         print("You won!")
#         break
# else:
#     print("sorry, you failed!")

# car game
#----------------------------------------------------------------------

# command = ""
# started = False
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("A car is already started!")
#         else:
#             started = True
#             print("car started...")
#     elif command == "stop":
#         if not started:
#             print("A car is already stopped!")
#         else:
#             started = False
#             print("car stopped.")
#     elif command == "help":
#         print("""
# start- to start the car
# stop- to stop the car
# quit- to quit
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("sorry, I don't understand that")

# for loop
#-----------------------------------------------------------------------------

# for items in "Python":
#     print(items)

# for items in ["NIYOMWUNGERI", "Henry", "Placide"]:
#     print(items)

# for i in range(5):
#     i += 1
#     print("* " * i)

# prices = [10, 30, 50]
# total = 0
# for price in prices:
#     total = total + price
# print(f"The total price is : {total}Rwf")

# Nested loop
#-----------------------------------------------------------------------------------

# for x in range(4):
#     for y in range(3):
#         print(f"({x},{y})")

# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     print("x" * x_count)

# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#      output += "x"
#     print(output)
#
# names = ["NIYOMWUNGERI", "Henry", "Placide"]
# names[0] = "Onlooker"
# print(names)

# numbers = [50, 60, 70, 80, 100, 90]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

# 2D list
#------------------------------------------------------------------------

# matrix = [
#     [1, 2, 3],
#     [4, 5, 7],
#     [7, 8, 9]
# ]
# print(matrix[1][2])
# for row in matrix:
#     for item in row:
#       print(item)


# List of Method
#--------------------------------------------------------------------------

# numbers = [1, 2, 3, 4, 5, 5, 5, 7, 8, 9]
# numbers.append(10)
# numbers.insert(0, 0)
# numbers.remove(10)
# numbers.pop()
# # numbers.clear()
# print(numbers)
# print(5 in numbers)
# print(numbers.count(5))
# numbers.sort()
# numbers.reverse()
# print(numbers)

# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

# Tuples
#-----------------------------------------------------------------------

# numbers = (1, 2, 3)
# print(numbers[1])

# unpacking
#-----------------------------------------------------------------------

# coordinates = (4, 5, 6)
# x, y, z = coordinates
# print(x, y, z)

# Dictionaries
#----------------------------------------------------------------------

# customer = {
#     "name": "Henry Placide",
#     "age": 21,
#     "is_verified": True
# }
# customer["birthdate"] = "March 03 2002"
# print(customer["name"])
# print(customer.get("birthdate"))

# phone = input("Phone : ")
# digit_mapping = {
#     "1": "one",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }
# output = ""
# for ch in phone:
#     output += digit_mapping.get(ch, "!") + " "
# print(output)

# message = input("> ")
# word = message.split(' ')
# print(word)

# Function in Python
#--------------------------------------------------------------------------------

# def greet_user(first_name, last_name):
#     print(f'Hi {first_name} {last_name}')
#     print('welcome in simba superMarket')
#
# print("Start")
# greet_user(last_name="smith", first_name="John")
# print("Finish")

# def square(number):
#     return number * number
# print(square(10))

# Exception
#-------------------------------------------------------------------------------

# try:
#     age = int(input("age: "))
#     income = 20000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print("Age can't be 0.")
# except ValueError:
#     print("Invalid Input")

# Classes
#----------------------------------------------------------------------------------

# class Point :
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")
#
# point1 = Point(50, 60)
# print(point1.x)
# point1.x1 = 10
# point1.x2 = 20
# print(point1.x1)
# print(point1.x2)
# point1.draw()
#
# point2 = Point()
# point2.x = 13
# print(point2.x)

# class Person:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#        print(f'Hi I am  {self.name}')
#
# john = Person("Henry Placide")
# paris = Person("Hotele la Paris")
# john.talk()
# paris.talk()

# Inheritance
#----------------------------------------------------------------------------

# class Mammals:
#     def walk(self):
#         print("walk")
#
# class Dog(Mammals):
#     def bark(self):
#         print("bark")
#
# class Cat(Mammals):
#     def be_annoying(self):
#         print("annoying")
#
# dog1 = Dog()
# dog1.walk()
#
# cat1 = Cat()
# cat1.be_annoying

# Modules
#-----------------------------------------------------------------------------

# def lbs_to_kg(weight):
#     return weight * 0.45
# def kg_to_lbs(weight):
#     return weight / 0.45
# import Converters
# print(Converters.kg_to_lbs(70))

# def find_max(numbers):
#
#     maximum = numbers[0]
#     for number in numbers:
#         if number > maximum:
#             maximum = number
#             return maximum

# from utils import find_maximum
# numbers = [50, 70, 90, 100]
# maximum = find_maximum(numbers)
# print(maximum)

# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()

# from ecommerce.shipping import calc_shipping
# calc_shipping()

# Pick Randomly Values
#-----------------------------------------------------------------------------
#
# import random
# for i in range(3):
#     print(random.randint(10, 20))

# members = ["Henry", "Placide", "Mosh"]
# print(random.choice(members))

# class Dice:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second
#
#
# dice = Dice()
# print(dice.roll())

# Files and Dictionaries in Python
#-------------------------------------------------------------------------------

# from pathlib import Path
# path = Path("emails")
# print(path.rmdir())
#
# path = Path()
# for file in path.glob("*"):
#     print(file)

# import smtplib
#
# sender = "sender@gmail.com"
# receiver = "receiver@gmail.com"
# password = "password123"
# subject = "Python email test"
# body = "I wrote an email! :D"
#
# message = f"""From: Snoop Dog{sender}
# To: Nicholas Cage{receiver}
# Subject: {subject}\n
# {body}
# """
#
# server = smtplib.SMTP("smtp.gmail.com", 587)
# server.starttls()
#
# # try:
# server.login(sender, password)
# print("Logged in ...")
# server.sendmail(sender, receiver, message)
# print("Email has been sent!")
#
# # except smtplib.SMTPAuthenticationError:
# # print("unable to sign in!")

import pandas as pd
import smtplib

e = pd.read_excel("xxx")
emails = e['xxx'].values

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("shikamusenge720@gmail.com", "x-ray.123")

msg = "Hello this is a email from python"
subject = "Hello world"
body = "Subject: {}\n\n{}".format(subject, msg)

for email in emails:
    server.sendmail("you@your_email_address", email, body)
server.quit()





















































































