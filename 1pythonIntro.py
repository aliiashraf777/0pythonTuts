# 1. Programming Language: Python
# Python is a high-level, interpreted programming language known for its simplicity and readability. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Python is widely used in web development, data analysis, artificial intelligence, scientific computing, and more.

# 2. Key Features of Python:
# - Easy to Learn and Use: Python has a simple syntax that is easy to read and write, making it an excellent choice for beginners.
# - Interpreted Language: Python code is executed line by line, which makes debugging easier.
# - Dynamically Typed: You don't need to declare variable types explicitly; Python determines the type at runtime.
# - Extensive Standard Library: Python comes with a rich set of modules and libraries that provide pre-built functionalities for various tasks.
# - Cross-Platform: Python can run on various operating systems, including Windows, macOS, and Linux.

# 3. Python Syntax:
# - Indentation: Python uses indentation to define code blocks instead of braces or keywords. Proper indentation is crucial for the correct execution of Python code.


# ---------------
# Settig up python in your system
# ---------------
# 1. donwload python from the official website: https://www.python.org/downloads/ 

# install python in your system and check the version of python installed in your system by running the following command in your terminal or command prompt: python --version 

# 2. You can also check the version of python installed in your system by running the following command in your terminal or command prompt: python -V

# 2a. you need to setup VS code for python development, you can download VS code from the official website: https://code.visualstudio.com/download, and installed python extension in VS code for python development. with python Debugger extension you can debug your python code in VS code.

# 3. you can run scripts in python by using the command: python script_name.py

# 4. need to setup python environment in your system, you can use virtual environments. You can create a virtual environment using the following command: python -m venv env_name

# 5. To activate the virtual environment, use the following command:
# - On Windows: env_name\Scripts\activate
# - On macOS and Linux: source env_name/bin/activate

# 6. first line of python code
# print('Hello, World!')
# print("Hello, World!")
# print('''
# 1. Hello, world!
# 2. Multiple lines string python comment
# ''')
# print('Welcome', 1+1, "3rd statement")

# -------------
# Variables in Python
# -------------
# Variables are containers to store data, and extract them on need.
# python variants are dynamically typed (no need to declare types)

# x=10
# y=20
# print(x+y);

# Case Senstive variables
# x=20
# X=30
# print(X+x);

# --------------
# Python Data Types
# --------------
# data types are of 2-types
# 2a. Mutable 2b. Un-Mutable

# Number Types
#  int: 5, 100, -5
# float 5.5, 3.14
# complex: 3 + 4j

# Sequence Types
# str='Hello'
# list=[1,2,3]
# tuples=(1,2,3)

# Mapping Types - Dictionary
# dict: {"name": "John", "age": 25}

# Boolean
# True, False

# Set Type
# these have unique values - can't have duplicate values
# set: {1,2,3}

# name='ali'
# print(name, type(name))
# print('name')
# now 'name' is string not variable, important interview point

# list=[10,20,30,'40 string']
# print(list, type(list))

# notTuple={10} - needs multiple values
# tuple={10,20,'tupple'}
# print(tuple,type(tuple))

# dictionary={
# "name": "ali",
# "course: python",
# }

# --------------------
# Python vars, dTypes PRACTICE QUESTIONS
# --------------------

# ***Task1*** 
# rint your name, age and favorite language using variables
# name='Ali'
# age=27
# favLang='python, cpp, JS5, Java'

# print("name: ", name, " age: ", age, " favLang: ", favLang)
# print("name: ", name)
# print("age ", age)
# print("tablog")

# ***Task2***
# Swap values of two variables and print before and after

'''
x=10
y=20
print("x=", x, "y=", y)
temp=x #temp=10
x=y #x=20
y=temp #y=10
print("x=", x, "y=", y)
'''

'''
x=5
y=10
print("x=", x, "y=",y)
x=x+y #5+10 = 15
y=x-y #15-10 = 5
x=x-y #15-5 = 10
print("x=", x, "y=",y)
'''

# ***Task3***
# Store width and height in variables, Calc area
'''
width=5
height=5
area=width*height
print("Area",area)
'''

# ***Task4***
# Take name and age as input from the user an print a welcome message
'''
name=input("Enter your name:--") #string 
age=input("Enter your age:--")

print("Hey",name, "You are,",age,"years old")
'''

# ***Task5***
# you ought 3 items - Rs. 505, rs 25, and 30 cladulare

'''
item1=50.5
item2=25
item3=30
total=0
total=item1+item2+item3
print("Total",total)
'''