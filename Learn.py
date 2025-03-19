#@Vics Python Referencing page



# 1.Basic syntax
# Print a message
print("Hello, Python!")

#Input
input("what is youre name")

# Variabls
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")




# 2. Basic Python operators

# Arithmetic  -  +,-,/,*,// ,**,%
#Logical      -  and,or,not
#Comparison   -  ==,!=,<,>.<=,>=
#Assignment   -  =, +=, -=, *=, /=
#Bitwise      -  ^,$,|,~,<<,>>
#Membership   -  in, not in
#Identity     -  is ,is not

#Arithmetic examples
# Arithmetic Operators
a = 10
b = 3

print("Arithmetic Operators:")
print(f"Addition: {a} + {b} = {a + b}")        # Output: 13
print(f"Subtraction: {a} - {b} = {a - b}")    # Output: 7
print(f"Multiplication: {a} * {b} = {a * b}") # Output: 30
print(f"Division: {a} / {b} = {a / b}")       # Output: 3.333...
print(f"Floor Division: {a} // {b} = {a // b}") # Output: 3
print(f"Modulus: {a} % {b} = {a % b}")        # Output: 1
print(f"Exponentiation: {a} ** {b} = {a ** b}") # Output: 1000
print()

# Comparison Operators
x = 5
y = 10

print("Comparison Operators:")
print(f"{x} == {y}: {x == y}")  # Output: False
print(f"{x} != {y}: {x != y}")  # Output: True
print(f"{x} > {y}: {x > y}")    # Output: False
print(f"{x} < {y}: {x < y}")    # Output: True
print(f"{x} >= {y}: {x >= y}")  # Output: False
print(f"{x} <= {y}: {x <= y}")  # Output: True
print()

# Logical Operators
print("Logical Operators:")
print(f"(5 > 3) and (10 < 20): {(5 > 3) and (10 < 20)}")  # Output: True
print(f"(5 > 3) or (10 > 20): {(5 > 3) or (10 > 20)}")   # Output: True
print(f"not (5 > 3): {not (5 > 3)}")                    # Output: False
print()

# Assignment Operators
num = 5
print("Assignment Operators:")
num += 3  # Equivalent to num = num + 3
print(f"After num += 3: {num}")  # Output: 8

num -= 2  # Equivalent to num = num - 2
print(f"After num -= 2: {num}")  # Output: 6

num *= 4  # Equivalent to num = num * 4
print(f"After num *= 4: {num}")  # Output: 24

num /= 2  # Equivalent to num = num / 2
print(f"After num /= 2: {num}")  # Output: 12.0
print()

# Bitwise Operators
p = 5  # Binary: 0101
q = 3  # Binary: 0011

print("Bitwise Operators:")
print(f"Bitwise AND: {p} & {q} = {p & q}")      # Output: 1 (Binary: 0001)
print(f"Bitwise OR: {p} | {q} = {p | q}")       # Output: 7 (Binary: 0111)
print(f"Bitwise XOR: {p} ^ {q} = {p ^ q}")      # Output: 6 (Binary: 0110)
print(f"Bitwise NOT: ~{p} = {~p}")              # Output: -6 (Two's complement)
print(f"Left Shift: {p} << 1 = {p << 1}")       # Output: 10 (Binary: 1010)
print(f"Right Shift: {p} >> 1 = {p >> 1}")      # Output: 2 (Binary: 0010)
print()

# Membership Operators
fruits = ["apple", "banana", "cherry"]

print("Membership Operators:")
print(f"'apple' in fruits: {'apple' in fruits}")          # Output: True
print(f"'mango' not in fruits: {'mango' not in fruits}")  # Output: True
print()

# Identity Operators
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print("Identity Operators:")
print(f"x is y: {x is y}")  # Output: True (same memory location)
print(f"x is z: {x is z}")  # Output: False (different memory location)
print(f"x is not z: {x is not z}")  # Output: True






#3. Python Data types

#1. int -Integer (whole numbers)
x = 10
#2.float -Floating-point number (decimals)
pi = 3.14
#3.complex -Complex numbers
c = 3 + 4j
#4.str -Strings (text)
name = "Alice"
#5.list -Ordered, mutable collection
fruits = ["apple", "banana"]
#6. tuple -Ordered, immutable collection
coordinates = (10, 20)
#6. dict -Key-value pairs
person = {"name": "Alice", "age": 25}
#8. set -Unordered collection of unique items
unique_numbers = {1, 2, 3}
#9. frozense -Immutable set
immutable_set = frozenset([1, 2, 3])
# 10 bool
Boolean (
True
or
False
)
is_active = True
#11. bytes-Immutable sequence of bytes
binary_data = b"hello"
#12 .bytearray -Mutable sequence of bytes
mutable_binary = bytearray(b"hello")
#13. memoryview -Memory view of an object
view = memoryview(b"data")
#14.  NoneType  -Represents no value
result = None





#4.Control structures

#If -Else statements
num = 10
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

#for loop
for i in range(5):
    print(i)

#while loop
count = 0
while count < 5:
    print(count)
    count += 1






# 5. Functions
# Simple Function
def greet(name):
    return f"Hello, {name}!"

print(greet("Bob"))  # Output: Hello, Bob!

# Function with Default Arguments
def power(base, exponent=2):
    return base ** exponent

print(power(3))      # Output: 9
print(power(3, 3))   # Output: 27

#functions without return
def greet(name):
    print(f"Hello, {name}!")

greet("Bob")



#6. Class and objects
#creating a class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        return f"Car: {self.brand} {self.model}"
# creating an objects
car1 = Car("Toyota", "Corolla")
print(car1.display())


#Classes and Inheritance

#Example
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()

print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!






# 7. Data structures 

#Lists
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

#Tuples
coordinates = (10, 20)
print(coordinates[0])  # Output: 10

#Dictionaries
person = {"name": "Alice", "age": 25}
print(person["name"])

#sets
numbers = {1, 2, 3, 4, 5}
print(3 in numbers)  # Output: True

#all in one
# List
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
fruits.append("orange")

# Tuple (Immutable)
coordinates = (10, 20)
print(coordinates[0])  # Output: 10

# Set (Unique elements)
unique_numbers = {1, 2, 3, 3}
print(unique_numbers)  # Output: {1, 2, 3}

# Dictionary (Key-Value pairs)
person = {"name": "Alice", "age": 25}
print(person["name"])  # Output: Alice



#8 .Error Handling
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Enter a number.")

#Another example
class MyCustomError(Exception):
    pass

try:
    raise MyCustomError("Something went wrong!")
except MyCustomError as e:
    print(f"Caught an exception: {e}")


#9. File Handling

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, File!")

# Reading from a file
with open("example.txt", "r") as file:
    print(file.read())




#10.Also to learn

#Decorators -a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure
def decorator_func(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@decorator_func
def say_hello():
    print("Hello!")

say_hello()

#Generators-Generators are a way to create iterators in Python.They use the yield keyword to produce values one at a time, instead of storing all values in memory.
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)

# Another example
# Generator Function
def generate_numbers():
    for i in range(5):
        yield i  # Yields one value at a time

# Using the Generator
gen = generate_numbers()
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2

# Alternatively, iterate over it
for num in generate_numbers():
    print(num)


#Threading -a built-in module that allows various threads to execute concurrently
import threading

def print_numbers():
    for i in range(5):
        print(i)

t1 = threading.Thread(target=print_numbers)
t1.start()
t1.join()

#Another example
import threading

def task():
    print("Task executed by:", threading.current_thread().name)

thread = threading.Thread(target=task)
thread.start()
thread.join()

#Multiprocessing
from multiprocessing import Process

def task():
    print("Task executed by process:", __name__)

process = Process(target=task)
process.start()
process.join()

#NB :Key Differences
#Threading : Suitable for I/O-bound tasks (e.g., file reading, network requests).
#Multiprocessing : Suitable for CPU-bound tasks (e.g., heavy computations).

#web scraping- an automated method used for collecting large amounts of data from websites and storing it in a structured form
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)


#Working with ApI'
#examples
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if response.status_code == 200:
    data = response.json()
    print(data["title"])  # Output: "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"








#11. List Comprehensions-List comprehensions provide a concise way to create lists.
#Syntax:
[expression for item in iterable if condition]
#Example
# Create a list of squares
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Filter even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]




#12. Lamda Functions -Lambda functions are small, anonymous functions defined using the lambda keyword
#syntax
lambda arguments: expression

#example

# Simple Lambda Function
double = lambda x: x * 2
print(double(5))  # Output: 10

# Using Lambda with `map()`
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]

# Using Lambda with `filter()`
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4]





# 13. Regular Expressions (re Module)- Regular expressions allow you to search and manipulate strings based on patterns.
#Example:
import re

text = "The rain in Spain falls mainly in the plain."

# Search for a pattern
match = re.search(r"Spain", text)
if match:
    print("Found:", match.group())  # Output: Found: Spain

# Find all occurrences
matches = re.findall(r"in", text)
print(matches)  # Output: ['in', 'in', 'in', 'in']



#13 . Functional programming tools
#examples
from functools import reduce

# Map
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]

# Filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4]

# Reduce
product = reduce(lambda x, y: x * y, numbers)




#14. Concatinations in python
#a.  String Concatenation  -Strings are concatenated using the + operator. This combines two or more strings into one.
# 1. Basic String Concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe

# Adding Strings with Numbers (Convert Number to String)
age = 30
greeting = "I am " + str(age) + " years old."
print(greeting)  # Output: I am 30 years old.

#2.  List Concatenation -Lists are concatenated using the + operator. This combines two or more lists into one.
# Concatenating Two Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)  # Output: [1, 2, 3, 4, 5, 6]

# Adding a Single Element to a List
new_element = [7]
combined_list += new_element
print(combined_list)  # Output: [1, 2, 3, 4, 5, 6, 7]


#3. Tuple Concatenation -Tuples are concatenated using the + operator. This combines two or more tuples into one.
# Concatenating Two Tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Adding a Single Element to a Tuple
new_element = (7,)
combined_tuple += new_element
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7)

#4. Concatenating Other Data Types -For non-string data types (e.g., integers, floats), you need to convert them to strings before concatenation.
# Concatenating Numbers as Strings
num1 = 10
num2 = 20
result = str(num1) + " + " + str(num2) + " = " + str(num1 + num2)
print(result)  # Output: 10 + 20 = 30

# Concatenating Mixed Data Types
name = "Alice"
age = 25
height = 5.5
info = name + " is " + str(age) + " years old and " + str(height) + " feet tall."
print(info)  # Output: Alice is 25 years old and 5.5 feet tall.

#5. Using join() for String Concatenation      -the join() method is a powerful way to concatenate a list of strings with a specific delimiter.
# Joining Strings with a Space
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)  # Output: Python is awesome

# Joining Strings with a Comma
fruits = ["apple", "banana", "cherry"]
fruit_list = ", ".join(fruits)
print(fruit_list)  # Output: apple, banana, cherry

#6.Concatenation with f-Strings (Formatted Strings)    -f-Strings (introduced in Python 3.6) allow you to embed expressions inside string literals using {}.
# Using f-Strings for Concatenation
name = "Alice"
age = 25
height = 5.5
info = f"{name} is {age} years old and {height} feet tall."
print(info)  # Output: Alice is 25 years old and 5.5 feet tall.

# Embedding Expressions
x = 10
y = 5
result = f"The sum of {x} and {y} is {x + y}."
print(result)  # Output: The sum of 10 and 5 is 15.

#7. Concatenation with format() -The format() method allows you to insert values into placeholders {} in a string.
# Using format() for Concatenation
name = "Alice"
age = 25
info = "{} is {} years old.".format(name, age)
print(info)  # Output: Alice is 25 years old.

# Specifying Positional Arguments
info = "{1} is {0} years old.".format(age, name)
print(info)  # Output: Alice is 25 years old.

# Named Placeholders
info = "{name} is {age} years old.".format(name="Bob", age=30)
print(info)  # Output: Bob is 30 years old.


#8. Concatenation with += Operator   -The += operator appends to an existing variable.

# String Concatenation with +=
message = "Hello"
message += " World!"
print(message)  # Output: Hello World!

# List Concatenation with +=
numbers = [1, 2, 3]
numbers += [4, 5]
print(numbers)  # Output: [1, 2, 3, 4, 5]

#9. Concatenation with * (Repetition) -The * operator repeats a sequence a specified number of times.
# Repeating Strings
stars = "*" * 10
print(stars)  # Output: **********

# Repeating Lists
numbers = [0] * 5
print(numbers)  # Output: [0, 0, 0, 0, 0]


#15. inbuilt Functions
#a. Mathematical functions
# 1. abs(x)  -Returns the absolute value of a number.
print(abs(-10))  # Output: 10

#2. divmod(a, b)  -Returns a tuple (quotient, remainder) of dividing a by b.
print(divmod(10, 3))  # Output: (3, 1)

#3.max(iterable, *[, key, default]) -Returns the largest item in an iterable or among arguments.
print(max([1, 5, 3, 9]))  # Output: 9
print(max("apple", "banana", "cherry"))  # Output: 'cherry'

#4.min(iterable, *[, key, default]) -Returns the smallest item in an iterable or among arguments.
print(min([1, 5, 3, 9]))  # Output: 1
print(min("apple", "banana", "cherry"))  # Output: 'apple'

#5.pow(x, y[, z])   -Raises x to the power of y. If z is provided, it computes (x ** y) % z.
print(pow(2, 3))  # Output: 8
print(pow(2, 3, 5))  # Output: 3 (8 % 5)


#6. round(number[, ndigits])  -Rounds a number to ndigits precision after the decimal point.
print(round(3.14159, 2))  # Output: 3.14

#7.sum(iterable, /, start=0)  -Sums all items in an iterable, optionally starting from start.
print(sum([1, 2, 3, 4]))  # Output: 10
print(sum([1, 2, 3, 4], 10))  # Output: 20

#b. Type conversation functions
# 1. bool([x])  -Converts a value to a Boolean (True or False).
print(bool(0))      # Output: False
print(bool("Hello"))  # Output: True

#2. int([x[, base]]) -Converts a value to an integer.
print(int("10"))       # Output: 10
print(int("101", 2))   # Output: 5 (binary to decimal)

#3. float([x])  -Converts a value to a floating-point number.

print(float("3.14"))  # Output: 3.14

#4.str(object='')  -Converts a value to a string.

print(product)  # Output: 24

#5. str(object='')  -Converts a value to a string.

print(str(123))  # Output: '123'

#6 list([iterable]) -Converts an iterable to a list.
print(list("hello"))  # Output: ['h', 'e', 'l', 'l', 'o']

#7. dict(**kwarg)  -Creates a dictionary.
print(dict(name="Alice", age=25))  # Output: {'name': 'Alice', 'age': 25}

#8.set([iterable])  -Creates a set from an iterable.
print(set([1, 2, 2, 3]))  # Output: {1, 2, 3}

#9.frozenset([iterable]) -Creates an immutable set.
print(frozenset([1, 2, 3]))  # Output: frozenset({1, 2, 3})

#10. chr(i)   -Returns the string representing a character whose Unicode code is i.
print(chr(65))  # Output: 'A'

#11.ord(c)   -Returns the Unicode code point for a character.
print(ord('A'))  # Output: 65

#12.bin(x) -Converts an integer to a binary string prefixed with '0b'.
print(bin(10))  # Output: '0b1010'

#13.hex(x)  -Converts an integer to a hexadecimal string prefixed with '0x'.
print(hex(255))  # Output: '0xff'

#14.oct(x)  -Converts an integer to an octal string prefixed with '0o'.
print(oct(8))  # Output: '0o10'

#c. Input output functions
#1.input([prompt])  -Reads input from the user.
name = input("Enter your name: ")
print(f"Hello, {name}!")


#2.print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)    -Prints objects to the text stream.
print("Hello", "World", sep=", ")  # Output: Hello, World

#3.open(file, mode='r', encoding=None, ...)  -Opens a file and returns a file object.
with open("example.txt", "w") as file:
    file.write("Hello, File!")

# d. Functional Programming Tools
# 1. map(function, iterable, ...)   -Applies a function to every item of an iterable.
numbers = [1, 2, 3]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # Output: [1, 4, 9]

#2. filter(function, iterable)  -Filters elements of an iterable based on a condition.
numbers = [1, 2, 3, 4]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # Output: [2, 4]

#3.zip(*iterables)  -Aggregates elements from multiple iterables into tuples.
names = ["Alice", "Bob"]
ages = [25, 30]
zipped = zip(names, ages)
print(list(zipped))  # Output: [('Alice', 25), ('Bob', 30)]

#4, enumerate(iterable, start=0)  -Adds a counter to an iterable.
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
# Output:
# 0 apple
# 1 banana
# 2 cherry

# e. Miscellaneous Functions   -These functions perform various utility tasks.
#1. len(s)   -Returns the length of an object.
print(len("hello"))  # Output: 5
print(len([1, 2, 3]))  # Output: 3
#2. type(object)  -Returns the type of an object
print(type(10))  # Output: <class 'int'>
#3.isinstance(object, classinfo)  -Checks if an object is an instance of a class or tuple of classes.
print(isinstance(10, int))  # Output: True
#4. issubclass(class, classinfo)  -Checks if a class is a subclass of another class 
class A: pass
class B(A): pass
print(issubclass(B, A))  # Output: True
#5.callable(object)  -Checks if an object is callable (e.g., a function or class).
def func(): pass
print(callable(func))  # Output: True
#6.dir([object])    -Returns a list of valid attributes for an object.
print(dir(str))  # Output: List of string methods
#7.help([object])    -Provides documentation for an object.
help(len)
#8. id(object)       -Returns the identity (memory address) of an object.
x = 10
print(id(x))
#9. sorted(iterable, *, key=None, reverse=False)  -Returns a sorted list from an iterable.
print(sorted([3, 1, 4, 1, 5]))  # Output: [1, 1, 3, 4, 5]
#10. reversed(seq)       -Returns a reverse iterator.
print(list(reversed([1, 2, 3])))  # Output: [3, 2, 1]
#11. globals()        -Returns a dictionary of the current global symbol table.
print(globals())
#12locals()           -Returns a dictionary of the current local symbol table.
print(locals())
#13 eval(expression[, globals[, locals]])    -Evaluates a string as a Python expression.
print(eval("2 + 3"))  # Output: 5
#14.exec(object[, globals[, locals]])  -Executes dynamically created program code.
exec("print('Hello, World!')")



#Specialized Functions
#all(iterable)   -Returns True if all elements of an iterable are true.
print(all([True, 1, "Hello"]))  # Output: True

#2. any(iterable)  -Returns True if any element of an iterable is true
print(any([False, 0, ""]))  # Output: False

#3.hasattr(object, name)  -Checks if an object has a named attribute.
class Test:
    x = 10
print(hasattr(Test, "x"))  # Output: True

#4. getattr(object, name[, default]) -Gets the value of a named attribute.
class Test:
    x = 10
print(getattr(Test, "x"))  # Output: 10

#5. setattr(object, name, value)  -Sets the value of a named attribute.
class Test:
    x = 10
setattr(Test, "x", 20)
print(Test.x)  # Output: 20

#6.delattr(object, name)  -Deletes a named attribute.
class Test:
    x = 10
delattr(Test, "x")
print(hasattr(Test, "x"))  # Output: False







# 16 Methods used in python
#a. String Methods
# 1..upper() -Converts all characters in a string to uppercase.
text = "hello"
print(text.upper())  # Output: "HELLO"

#2. .lower() -Converts all characters in a string to lowercase.

text = "HELLO"
print(text.lower())  # Output: "hello"

#3..capitalize() -Capitalizes the first character of a string.
text = "hello world"
print(text.capitalize())  # Output: "Hello world"

#4..title() -Capitalizes the first letter of each word in a string.
text = "hello world"
print(text.title())  # Output: "Hello World"

#5..strip() -Removes leading and trailing whitespace (or specified characters).
text = "   hello   "
print(text.strip())  # Output: "hello"

text = "xxxhelloxxx"
print(text.strip("x"))  # Output: "hello"

#6. split(separator) -Splits a string into a list based on a separator.
text = "apple,banana,cherry"
print(text.split(","))  # Output: ['apple', 'banana', 'cherry']

#7..join(iterable)  -Joins elements of an iterable into a single string, separated by the original string.
words = ["Python", "is", "fun"]
print(" ".join(words))  # Output: "Python is fun"

#8.find(substring) -Returns the index of the first occurrence of a substring (or -1 if not found).
text = "hello world"
print(text.find("world"))  # Output: 6

#9..startswith(prefix) and .endswith(suffix)  -Checks if a string starts or ends with a specific substring.
text = "hello world"
print(text.startswith("hello"))  # Output: True
print(text.endswith("world"))    # Output: True

#b.List Methods

#1..append(item) -Adds an item to the end of a list.
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # Output: ['apple', 'banana', 'cherry']

#2. .extend(iterable)  -Adds multiple items to the end of a list.
fruits = ["apple", "banana"]
fruits.extend(["cherry", "date"])
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']

#3. .insert(index, item)  -Inserts an item at a specific position.
fruits = ["apple", "banana"]
fruits.insert(1, "cherry")
print(fruits)  # Output: ['apple', 'cherry', 'banana']

#4. .remove(item) -Removes the first occurrence of an item.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry']

#5..pop([index])  -Removes and returns an item at a specific index (default is the last item)
fruits = ["apple", "banana", "cherry"]
fruit = fruits.pop(1)
print(fruit)   # Output: "banana"
print(fruits)  # Output: ['apple', 'cherry']

#6..clear() -Removes all items from a list.
fruits = ["apple", "banana"]
fruits.clear()
print(fruits)  # Output: []

#7..index(item) -Returns the index of the first occurrence of an item.
fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana"))  # Output: 1

#8.count(item)  -Counts the number of times an item appears in a list.
fruits = ["apple", "banana", "apple"]
print(fruits.count("apple"))  # Output: 2

#9. .sort()  -Sorts a list in ascending order (modifies the list in place).
numbers = [3, 1, 4, 1, 5]
numbers.sort()
print(numbers)  # Output: [1, 1, 3, 4, 5]

#10. .reverse() -Reverses the order of a list (modifies the list in place).
numbers = [1, 2, 3]
numbers.reverse()
print(numbers)  # Output: [3, 2, 1]

#c. Dictionary Methods
#1. .keys()  -Returns a view of all keys in a dictionary.
person = {"name": "Alice", "age": 25}
print(person.keys())  # Output: dict_keys(['name', 'age'])

#2..values()  -Returns a view of all values in a dictionary.
person = {"name": "Alice", "age": 25}
print(person.values())  # Output: dict_values(['Alice', 25])

#4. .items()  -Returns a view of all key-value pairs as tuples.
person = {"name": "Alice", "age": 25}
print(person.items())  # Output: dict_items([('name', 'Alice'), ('age', 25)])

#5. .get(key, default)  -Returns the value for a key, or a default value if the key doesn’t exist.
person = {"name": "Alice"}
print(person.get("age", 30))  # Output: 30

#6..update(other_dict) -Updates a dictionary with key-value pairs from another dictionary.
person = {"name": "Alice"}
person.update({"age": 25})
print(person)  # Output: {'name': 'Alice', 'age': 25}

#7. .pop(key, default)  -Removes and returns the value for a key, or a default value if the key doesn’t exist.
person = {"name": "Alice", "age": 25}
age = person.pop("age")
print(age)     # Output: 25
print(person)  # Output: {'name': 'Alice'}

#8. .clear()  -Removes all key-value pairs from a dictionary.
person = {"name": "Alice", "age": 25}
person.clear()
print(person)  # Output: {}

#d. Tupple Methods
#1..count(item)  -Counts the number of times an item appears in a tuple.
numbers = (1, 2, 3, 2)
print(numbers.count(2))  # Output: 2

#2. .index(item)  -Returns the index of the first occurrence of an item.
numbers = (1, 2, 3)
print(numbers.index(2))  # Output: 1

#e. Set Methods
#1. .add(item)  -Adds an item to a set.
fruits = {"apple", "banana"}
fruits.add("cherry")
print(fruits)  # Output: {'apple', 'banana', 'cherry'}

#2. .remove(item)   -Removes an item from a set (raises an error if the item doesn’t exist).
fruits = {"apple", "banana"}
fruits.remove("banana")
print(fruits)  # Output: {'apple'}

#3. .discard(item)  -Removes an item from a set (does nothing if the item doesn’t exist).
fruits = {"apple", "banana"}
fruits.discard("cherry")  # No error
print(fruits)  # Output: {'apple', 'banana'}

#4..union(other_set) -Returns a new set containing all unique items from both sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5}

#5. .intersection(other_set) -Returns a new set containing items common to both sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.intersection(set2))  # Output: {3}

#6. .difference(other_set) -Returns a new set containing items in the first set but not in the second.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.difference(set2))  # Output: {1, 2}


#7..symmetric_difference(other_set) -Returns a new set containing items in either set but not both.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.symmetric_difference(set2))  # Output: {1, 2, 4, 5}


#f.Other useful methods

#1. .copy()  -Creates a shallow copy of an object.
list1 = [1, 2, 3]
list2 = list1.copy()
print(list2)  # Output: [1, 2, 3]

#2. .format() (String Method) -Formats a string with placeholders.
text = "My name is {} and I am {} years old."
print(text.format("Alice", 25))  # Output: "My name is Alice and I am 25 years old."

#3..isinstance(object, classinfo)  -Checks if an object is an instance of a class.
print(isinstance("hello", str))  # Output: True




#17. Python modules and their functions

#pre-Installed with python

#os	             -Interact with the operating system (file handling, environment variables, etc.)
#sys	         -System-specific parameters and functions (command-line arguments, interpreter control)
#math	         -Mathematical functions like square root, power, trigonometry, etc.
#random-         -Generate random numbers, shuffle lists, and choose random elements
#datetime	     -Work with dates and times
#time	         -Handle time-related functions (delays, timestamps)
#re	             - expressions for pattern matching
#json	         -Encode and decode JSON data
#csv	          -Read and write CSV files
#sqlite3         -Interface for SQLite databases
#threading	      -Multithreading for parallel execution
#multiprocessing  -Run multiple processes in parallel
#collections	  -Advanced data structures (deque, namedtuple, Counter, etc.)
#functools	      -Higher-order functions and function manipulation (e.g., lru_cache)
#itertools	      -Iterator functions for efficient looping
#logging	      -Logging for debugging and tracking application events
#hashlib	      -Hashing algorithms like MD5, SHA-256
#argparse	      -Command-line argument parsing


#Data science
 
#numpy	        -Numerical computing, multi-dimensional arrays, fast operations
#pandas	        -Data manipulation and analysis, DataFrames (like Excel tables)
#matplotlib	    -Data visualization with charts and plots
#seaborn	    -Statistical data visualization (built on top of Matplotlib)
#scipy	        -Scientific computing (optimization, integration, signal processing)
#scikit-learn	-Machine learning algorithms (classification, regression, clustering)
#tensorflow	    -Deep learning framework from Google
#keras	        -High-level API for TensorFlow (simplifies deep learning models)
#pytorch	    -Deep learning framework from Facebook (flexible and dynamic)
#statsmodels	-Statistical modeling and hypothesis testing
#xgboost	    -Extreme Gradient Boosting for high-performance ML models


#Web Development
#flask	         -Lightweight web framework for creating APIs and web apps
#django	         -High-level web framework for rapid development of secure websites
#fastapi	     -High-performance API framework for Python
#bottle	         -Minimalist web framework
#tornado	     -Asynchronous web framework
#requests	     -Send HTTP requests (GET, POST, etc.)
#beautifulsoup4	 -Web scraping (parse HTML/XML data)
#selenium	     - Automate web browsers for testing and scraping
#scrapy	         - Advanced web scraping framework

#Cybersecurity and cryptography
#cryptography	   -Encrypt and decrypt data (AES, RSA, hashing)
#pycryptodome	   -Cryptographic functions like RSA, AES, SHA
#hashlib	       -Hashing functions (MD5, SHA-256, etc.)
#paramiko	       -SSH and SFTP operations
#scapy	           -Packet sniffing and network analysis
#nmap	           -Python interface for the Nmap scanner


#Networking & Automation
#socket	    -Network communication (TCP/UDP sockets)
#paramiko	-SSH automation for remote server management
#pyserial	-Serial communication (e.g., Arduino, Raspberry Pi)
#pyautogui	-GUI automation (keyboard, mouse control)
#requests	-Sending HTTP requests to APIs
#asyncio	-Asynchronous programming for handling multiple network tasks


# Blockchain & Web3
#web3.py	       -Interact with Ethereum blockchain (smart contracts, transactions)
#eth-brownie	   -Smart contract development and testing framework
#pybitcointools	   -Bitcoin transactions and wallet management
#etherscan	       -Fetch data from Ethereum blockchain explorer


# Image Processing & Computer Vision
#pillow	    -Image manipulation (resize, convert, filter)
#opencv	    -Computer vision (face detection, object tracking)
#tesseract	-Optical Character Recognition (OCR)


# GUI Development (Desktop Apps)
#Library	-Function
#tkinter	-Built-in GUI library (basic applications)
#pyqt	    -Feature-rich GUI development (based on Qt framework)
#kivy	    -Multi-platform GUI development (Windows, Mac, Linux, Android, iOS)
#wxPython	-Native-looking GUI for desktop applications

#9. Game Development
#pygame	     -Game development (graphics, sound, animations)
#pyglet	     -3D game and multimedia applications
#panda3d	 -3D game engine


#10. Automation & Web Scraping
#selenium	            -Automate browser tasks (testing, scraping)
#pyautogui	            -Automate keyboard and mouse actions
#scrapy                 -Web scraping and data extraction
#bs4 (BeautifulSoup)	-Parse HTML for web scraping
#shutil             	-Automate file operations (copy, move, delete)


#11. Database Management
#sqlite3	  -Lightweight database built into Python
#sqlalchemy	  -SQL toolkit and ORM (Object-Relational Mapping)
#pymongo	  -Interact with MongoDB (NoSQL)
#redis	      -Redis database interactions (caching, real-time applications)
#

#Robotics and IoT
#gpiozero	-Control Raspberry Pi GPIO pins
#pyserial	-Serial communication with hardware
#openai   	-AI-powered automation