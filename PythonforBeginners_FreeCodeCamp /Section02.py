# ---------------------------
# VARIABLES AND BASIC TYPES
# ---------------------------

# We are creating variables to store data
name = "Isabel"   # A string variable
age = 21          # An integer variable

# Check the type of the variable 'name'
print(type(name))  # This will print: <class 'str'>

# Compare if the type of 'name' is string
print(type(name) == str)  # True if 'name' is of type str

# Another way to check the type (better practice):
print(isinstance(name, str))  # True if 'name' is an instance of str


# ---------------------------
# FUNCTIONS
# ---------------------------

# Define a function to check if someone is an adult
def is_adult(age):
    # If the age is greater than 18, return True, otherwise return False
    if age > 18:
        return True
    else:
        return False

# A shorter version of the same function using a conditional expression
def is_adult2(age):
    return True if age > 18 else False


# ---------------------------
# STRING OPERATIONS
# ---------------------------

# Concatenate strings (join them together)
phrase = name + " is my name"  # Creates "Isabel is my name"

# Add more text to an existing string variable using +=
name += " is my first name"    # Now 'name' becomes "Isabel is my first name"

# Multiline string using triple quotes
print(""" Here
      there are
      multiple
      lines
""")

# String methods for case formatting
print("AnItADeV".upper())   # Converts to UPPERCASE
print("AnItADeV".lower())   # Converts to lowercase
print("AnItADeV".isupper()) # Checks if ALL characters are uppercase (False here)
print("AnItADeV".title())   # Converts to Title Case (Anitadev -> Anita Dev)

# Escape characters: \" lets us include quotes inside a string
cite = "The author said \"something\" "


# ---------------------------
# STRING INDEXING AND SLICING
# ---------------------------

word = "abcdefghi"

print(word[1])    # Access single character at index 1 -> 'b' (indexes start at 0)
print(word[-1])   # Access last character -> 'i'
print(word[1:3])  # Slice from index 1 up to (but not including) 3 -> 'bc'
print(word[:2])   # Slice from start to index 2 (not included) -> 'ab'
print(word[5:])   # Slice from index 5 to the end -> 'fghi'


# ---------------------------
# BOOLEAN VALUES IN CONDITIONS
# ---------------------------

done = 5  # In Python, any non-zero number is considered True in a condition

if done:  # This checks if 'done' is True
    print("yes")
else:
    print("no")


# ---------------------------
# COMPLEX NUMBERS
# ---------------------------

# Create a complex number (a number with real and imaginary part)
complex_num = 2 + 3j
print(complex_num)

# Another way using the complex() function
num = complex(2, 3)  # Creates the same complex number (2 + 3j)
print(num.real, num.imag)

# ---------------------------
# BUILT-IN FUNCTIONS FOR NUMBERS
# ---------------------------

# abs() gives the absolute value of a number (removes the negative sign if present)
print(abs(-5.5))  # Output: 5.5

# round() rounds a number to a given number of decimal places
# Here, 5.49 is rounded to 1 decimal place
print(round(5.49, 1))  # Output: 5.5


# ---------------------------
# ENUMS (Enumerations)
# ---------------------------

# Enums are a way to create a group of related named constants
# We use them when we want meaningful names for values instead of just numbers

from enum import Enum  # Import the Enum class from Python's standard library

# Define an Enum called 'State' with two possible values
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

# Access the value of an Enum member
print(State.ACTIVE.value)  # Output: 1

# Get Enum member by its value
print(State(1))  # Output: State.ACTIVE

# Get Enum member by its name (as a string)
print(State['ACTIVE'].value)  # Output: 1

# Convert Enum to a list of its members
print(list(State))  
# Output: [<State.INACTIVE: 0>, <State.ACTIVE: 1>]

# Get the number of members in the Enum
print(len(State))  # Output: 2

# ---------------------------
# USER INPUT AND OUTPUT
# ---------------------------

# input() asks the user to type something in the console and returns it as a string
age = input("What is your age? ")  # The message inside the quotes is shown to the user

# The value returned by input() is ALWAYS a string, even if the user types numbers

# Concatenate (join) strings using +
print("Your age is " + age)  # Combines "Your age is " with whatever the user typed