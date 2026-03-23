##################################################
# PYTHON BEGINNER CHALLENGES
# Organized by Topic
##################################################


##################################################
# SECTION 1: BEGINNER BASICS
# Topics: variables, input/output, string methods,
#         type conversion, string indexing, swapping
##################################################

# --- 1.1 Greeting with Name and Age ---
name = input("What is your name?\n").lower()
age = int(input("How old are you?\n"))
print(f"Hello,\nGood morning {name}\nYou are {age} years old today")

# --- 1.2 Arithmetic with Two Numbers ---
num1 = int(input("Pick a number: "))
num2 = int(input("Pick another number: "))
result = num1 + num2 * 5      # Note: multiplication runs before addition (BODMAS)
print(result)
print(type(result))

# --- 1.3 Age Calculator from Birth Year ---
year = int(input("What is your birth year? "))
current_year = int(input("What year are we in now? "))
age = current_year - year
print(f"You are {age} years old this year")

# --- 1.4 Name Case Converter ---
name = input("What is your name? ")
print(name.lower())
print(name.upper())

# --- 1.5 Swap Two Variables ---
a = 5
b = 10
a, b = b, a     # Swap values in one step
print(a)
print(b)

# --- 1.6 Full Name Formatter ---
f_name = input("What is your first name? ")
l_name = input("What is your last name? ")
full_name = f"{f_name} {l_name}"
print(full_name)

# --- 1.7 String Indexing ---
language = "Python"
print(language[0])   # First character
print(language[-1])  # Last character


##################################################
# SECTION 2: CONTROL FLOW
# Topics: if/elif/else, conditionals
##################################################

# --- 2.1 Even or Odd Checker ---
num = int(input("Input a number: "))
if num % 2 == 0:
    print(num, "- Even")
else:
    print(num, "- Odd")

# --- 2.2 Grade Calculator ---
score = int(input("What is your score? "))
if score > 70:
    print("A")
elif score > 60:
    print("B")
elif score > 45:
    print("C")
elif score > 40:
    print("D")
else:
    print("F")


##################################################
# SECTION 3: LOOPS
# Topics: for loops, range(), accumulation
##################################################

# --- 3.1 Print Even Numbers from 1 to 50 ---
for num in range(1, 51):
    if num % 2 == 0:
        print(num)

# --- 3.2 Double Each Number from 1 to 50 ---
for num in range(1, 51):
    num += num
    print(num)

# --- 3.3 Multiplication Table for 7 ---
for num in range(1, 11):
    mul = num * 7
    print(f"7 x {num} = {mul}")


##################################################
# SECTION 4: DATA STRUCTURES
# Topics: lists, iteration, accumulation
##################################################

# --- 4.1 Print Fruits in Lowercase ---
fruits = ["Mango", "Banana", "Pawpaw", "Orange", "Lime"]
for fruit in fruits:
    print(fruit.lower())

# --- 4.2 Sum of 1 to 10 ---
score = 0
for num in range(1, 11):
    score += num
print(score)


##################################################
# SECTION 5: FUNCTIONS
# Topics: def, *args, return, strip/lower
##################################################

# --- 5.1 Name Cleaner (two args) ---
def text_clean(fname, lname):
    f_name = fname.strip().lower()
    l_name = lname.strip().lower()
    full_name = f"{f_name} {l_name}"
    print(full_name)

text_clean("Peter", "Osas  ")

# --- 5.2 Sum with *args ---
def total(*args):
    print(sum(args))

total(1, 4, 6)

# --- 5.3 Name Cleaner (single arg, no return) ---
# Note: this function prints nothing because return is commented out
def text_clean_single(fname):
    f_name = fname.strip().lower()
    # return f_name          # Uncomment to fix — currently returns None

new = text_clean_single("    vu  ")
print(new)   # Prints None because return is missing


##################################################
# SECTION 6: MINI PROJECTS
# Topics: combining all skills above
##################################################

# --- 6.1 Personal Info Formatter ---
def info():
    first_name = input("What is your first name? ").strip().title()
    last_name  = input("What is your last name? ").strip().title()
    age        = int(input("How old are you? "))
    country    = input("What country are you from? ").strip().title()
    print(f"Hello {first_name} {last_name},\nHow are you today?\nYou are {age} years old\nand you are from {country}.")

info()


# --- 6.2 Simple Calculator ---
def add(num1, num2):      return num1 + num2
def sub(num1, num2):      return num1 - num2
def div(num1, num2):      return num1 / num2
def mul(num1, num2):      return num1 * num2

def calculator():
    print("Calculator Menu:\n1. Add\n2. Subtract\n3. Divide\n4. Multiply")
    choice = int(input("Choose operation (1-4): "))

    if choice < 1 or choice > 4:
        print("Wrong input")
        return

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    operations = {1: add, 2: sub, 3: div, 4: mul}
    result = operations[choice](num1, num2)
    print(f"Result: {result}")

calculator()


# --- 6.3 Temperature Converter ---
def temperature_converter():
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    print("Temperature Converter:\n1. Celsius → Fahrenheit\n2. Fahrenheit → Celsius")
    choice = int(input("Choose operation (1 or 2): "))

    if choice == 1:
        temp = float(input("Enter temperature in Celsius: "))
        result = celsius_to_fahrenheit(temp)
        print(f"Result: {temp}°C = {result:.2f}°F")
    elif choice == 2:
        temp = float(input("Enter temperature in Fahrenheit: "))
        result = fahrenheit_to_celsius(temp)
        print(f"Result: {temp}°F = {result:.2f}°C")
    else:
        print("Wrong input")

temperature_converter()


##################################################
# SECTION 7: BUILT-IN FUNCTIONS
# Topics: enumerate, reversed, zip, map,
#         filter, lambda
##################################################

# --- 7.1 Student Position Tracker (enumerate) ---
names = ["John", "Mary", "David"]
for index, name in enumerate(names, start=1):
    print(index, name)

# --- 7.2 Countdown System (reversed) ---
numbers = [1, 2, 3, 4, 5]
for number in reversed(numbers):
    print(number)

# --- 7.3 Product & Price Pairing (zip) ---
products = ["Rice", "Beans", "Oil"]
prices   = [5000, 3000, 2500]
for product, price in zip(products, prices):
    print(f"{product} - {price}")

# --- 7.4 Convert Names to Uppercase (map + lambda) ---
names = ["john", "mary", "david"]
uppercase_names = list(map(lambda x: x.upper(), names))
print(uppercase_names)

# --- 7.5 Extract Passing Scores (filter + lambda) ---
scores = [45, 70, 32, 88, 55]
passing = list(filter(lambda x: x >= 50, scores))
print(passing)

# --- 7.6 Add Bonus to Salaries (map + lambda) ---
salaries = [50000, 60000, 70000]
with_bonus = list(map(lambda x: x + 10000, salaries))
print(with_bonus)

# --- 7.7 Filter Even Numbers (filter + lambda) ---
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

# --- 7.8 Rank Players by Score (zip + enumerate) ---
players = ["John", "Mary", "David"]
scores  = [90, 85, 95]
for index, (player, score) in enumerate(zip(players, scores), start=1):
    print(f"{index}. {player} scored {score}")

# --- 7.9 Reverse & Index Names (reversed + enumerate) ---
names = ["Ada", "Tobi", "Kunle"]
for index, name in enumerate(reversed(names), start=1):
    print(index, name)

# --- 7.10 Filter & Transform Products (filter + map + lambda) ---
prices = [1200, 4500, 3000, 800]
taxed  = list(map(
    lambda x: int(x * 1.1),
    filter(lambda x: x >= 1000, prices)
))
print(taxed)


##################################################
# SECTION 8: BONUS CHALLENGE
# Topics: zip, filter, enumerate, lambda combined
##################################################

# Print only passing students (score >= 50) with numbering
names  = ["John", "Mary", "David"]
scores = [40, 75, 90]

result = enumerate(
    filter(lambda x: x[1] >= 50, zip(names, scores)),
    start=1
)

for index, (name, score) in result:
    print(f"{index}. {name} - {score}")