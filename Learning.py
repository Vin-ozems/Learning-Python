###################################################
# BEGINNER CHALLENGES
###################################################

#name = input("what is your name?\n").lower()
#Age = int(input("How old are you?\n"))
#print(f"""Hello,\nGood morning {name}\nyou are {Age}years old today""" )

# num1 = int(input("Pick a number "))
# num2 = int(input("Pick another number "))
# Result = num1 + num2 * 5
# print(Result)
# print(type(Result))

# Year = int(input("what is you birth year? "))
# Current_year = int(input("what year are we in now?"))
# Age = Current_year - Year 
# print(f"you are {Age}years old this year")

# name = input("what is your name? ")
# print(name.lower())
# print(name.upper())

# a = 5
# b = 10
# means swap the values of a and b in one step
# a, b = b, a
# print(a)
# print(b)

# f_name = input("what is you first name? ")
# L_name = input("what is your last name? ")
# full_name = f"{f_name} {L_name}"
# print(full_name)

# language = "Python"
# print(language[0])
# print(language[-1])


###################################################
# CONTROL FLOW AND LOOP
###################################################
# num = int(input("input a number "))
# if num % 2 == 0:
#     print(num)
#     print("Even")
# else:
#     print(num)
#     print("Odd")


# score = int(input("What is your score "))
# if score > 70:
#     print("A")
# elif score > 60:
#     print("B")
# elif score > 45:
#     print("C")
# elif score > 40:
#     print("D")
# else:
#     print("F")

# for num in range(1,51):
#     if num % 2 == 0:
#         print(num)

# for num in range(1,51):
#         num += num
#         print(num)

# for num in range(1,11):
#          mul = num * 7
#          print(f"7 * {num} = {mul}")


###########################################################################
# DATA STRUCTURES
###########################################################################
# Fruits = ["Mango", "Banana", "Pawpaw", "Orange", "Lime"]
# for fruit in Fruits:
#     print(fruit.lower())

# score = 0
# for num in range(1,11):
#     score += num
# print(score)


# def text_clean(fname, lname):
#     f_name = (fname.strip().lower())
#     l_name = (lname.strip().lower())
#     full_name = f"{f_name} {l_name}"
#     print(full_name )

# text_clean("Peter", "Osas  ")

# def total(*args):
#     print(sum(args))

# total(1, 4, 6)

# def text_clean(fname):
#     f_name = (fname.strip().lower())
#     # return f_name

# new = text_clean("    vu  ")
# print(new)

#  1. Personal Info Formatter
# Build a program that asks for a user’s 
# first name, 
# last name, 
# age, and 
# country, then formats and prints a neat profile sentence.
# Skills: variables, input/output, string formatting. 



# Here are 5 beginner → intermediate Python projects that move from variables to functions:

# 1. Personal Info Formatter
# Build a program that asks for a user’s first name, last name, age, and country, then formats and prints a neat profile sentence.
# Skills: variables, input/output, string formatting.
# def info():
#     first_name = input("What is your first name? ").strip().title()
#     last_name =  input("What is your last name? ").strip().title()
#     age = int(input("How old are you? "))
#     country = input("What country are you from? ").strip().title()
#     print (f"Hello {first_name} {last_name},\nHow are you today,\nyou are {age} years old\nand you are from {country}")

# info()

# 2. Simple Calculator
# Create a calculator that performs addition, subtraction, multiplication, and division using functions.
# Skills: variables, conditionals, functions, user input.

# def add(num1, num2):
#     addition = num1 + num2
#     return addition

# def sub(num1, num2):
#     subtraction = num1 - num2
#     return subtraction

# def div(num1, num2):
#     division = num1 / num2
#     return division

# def mul(num1, num2):
#     multiply = num1 * num2
#     return multiply

# def calculator():
#     print("Calculator Menu:\n1.Add\n2.Subtract\n3.Divide\n4.Multiply")
   
#     choice = int(input("Choose operation (1-4): "))
#     if choice > 4:
#         print("wrong input")
#     else:
#         num1 = int(input())
#         num2 = int(input())

#         if choice == 1:
#             result = add(num1,num2)
#         elif choice == 2:
#             result = sub(num1,num2)
#         elif choice == 3:
#             result = div(num1,num2)
#         elif choice == 4:
#             result = mul(num1,num2)
#         print(f"Result: {result}")
    
# calculator()



# 3. Temperature Converter
# Write a program that converts Celsius ↔ Fahrenheit using reusable functions.

def Temperature_Converter():
    # 1. Define celsius_to_fahrenheit function
    def celsius_to_fahrenheit(celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

    # 2. Define fahrenheit_to_celsius function
    def fahrenheit_to_celsius(fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return celsius

    print("Calculator Menu:\n1. C→F,\n2. F→C")
    choice = int(input("Choose operation (1 or 2): "))

    if choice > 2:
        print("wrong input")
    else:
    # 3. Get input and convert based on choice
        if choice == 1:
            temp = float(input("Enter temperature in Celsius: "))
            result = celsius_to_fahrenheit(temp)
            print(f"Result: {temp}°C = {result}°F")
        elif choice == 2:
            temp = float(input("Enter temperature in Fahrenheit: "))
            result = fahrenheit_to_celsius(temp)
            print(f"Result: {temp}°F = {result}°C")
        else:
            print("Wrong input")

Temperature_Converter()




# 4. Shopping List Manager
# Let users add items, remove items, and view their shopping list using functions and lists.
# Skills: lists, loops, functions.

# 5. Student Grade Analyzer
# Ask for several student scores, calculate average, highest, and lowest using functions.
# Skills: lists, loops, functions, basic statistics.

