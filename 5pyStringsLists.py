# ---------------
# STRINGS + strings  in Python
# ---------------
""" w="welcome"
#  0123456 index
print(w)
print(w[2])
print(w[-1]) #reads reverse
print(w[-5])

# works same like range
print(w[0:3]) #starts from 0 | stop 3-1 | steps
print(w[0:])
print(w[0::1])
print(w[0::2])
print(w[::2]) #by default starts from 0

# reverse -ive decrement order
print(w[-1::-1])

print(w[-1:2:-1 ])

print(w[-4::-1])
"""

""" name='python'
age=23
F-string like template literals
print("welcome to {name}")
print("welcome to {}".format(name))
print("welcome to {1} {0}".format(name,age))
print("welcome to {1} {0}".format(name,age))
print(f"welcome to {name}. age {age}") """


# --------------------
# LISTS in python
# --------------------

# list in python are used to store multiple items in a singel variable.
# python lists are ordered and mutable, meaning you can modify their contents.
# Contrary to it, strings are IMMUTABLE.

# LIST SLICING-------
# slicing is same like STRINGS
""" fruits=["apple","banana","cherry"]
print(fruits[0]) #apple
print(fruits[-1]) #cherry
print(fruits[0:2]) #["apple","banana"] """

""" list=[10,20,30,40,"hello","ali",[50,60]]
print(list[1]) #10
print(list[-1]) #ali
print(list[-2]) #hello
print(list[-2][-2]) #second last 'l' in hello
print(list[1:4]) #returns list, in slicing of multiple values
print(list[-1::-1]) #reverses list """

# LIST ITERATING----------
""" l=[10,20,30,40,50]
leng=len(l)

for a in range(leng):
    print(a,l[a])

for n in l:
    print(n) """


# MUTATE list item
""" l=[1,2,3,4]
l[2]=10

print(l) """

# logical question
""" l=[1,2,3,4]
for n in l:
    l[-1]=n
print(l)

# l[-1]=1 [1,2,3,1]
# l[-1]=2 [1,2,3,2]
# l[-1]=3 [1,2,3,3] #because [-1] have 3 now
# l[-1]=3 [1,2,3,3] """

# LIST methods

# append() 
# adds an item at the end fruits.append("orange")

# extend()
# fruits.extend(kiwi,grapes,mango)

# insert()
# inserts at specified idx fruits.insert(1,"kiwi")

# pop() 
# remoes item by idx (last by default), fruits.pop()
# fruits.pop(2)

# remove()
# removes first occurrence by value, fruits.remove("banana")

# sort()
# sortList=[10,40,30,20,70,60]
# sorts list, sortList.sort()

# reverse()
# reverse list, fruits.reverser()

# len()
# returns number of items, len(fruits)

# clear()
# empties the list
# fruits.clear()


# ---------------
# STRINGS/LISTS PRACTICE QUESTIONS
# ---------------

# TASK1---------
# ID card 16-digit validation (using string conditions only)

""" # userInput=eval(input("enter id card no (16 digits) "))
userInput=input("enter id card no (16 digits) ")

if userInput.isdigit() and len(userInput):
    print("valid id card number")
else:
    print("invalid id card number") """

# TASK2------------
# PAN CARD number vlidation (using string conditions only)
# 1. pan number mus be exactly 10 chars
# 2. first 5 chars must be UPPERCASE (A-Z)
# 3. next 4 chars must be digits (0-9)
# 4. last character must be an uppercase (A-Z)
# ABCDE1234F

""" userInput=input("enter pan num (10 digits): ")
panNum=userInput.upper()

if len(panNum)==10 and panNum[0:5].isalpha() and panNum[5:9].isdigit() and panNum[-1].isalpha():
    print(panNum," is valid pan num")
else:
    print("please enter valid pan card num") """

# TASK3--------

# make a string reversed , 1234

""" userInput=input("Enter the value: ")
print(userInput)
revString=userInput[-1::-1]
print(revString) """


# TASK4---------
# count vowels in string

""" userInput=input("enter value: ")
vowels="aeiouAEIOU"
count=0

for a in userInput:
    if a in vowels:
        print(a)
        count+=1

print("") """


# TASK5-----------
# fIND palindrome string

""" userInput=input("enter a string: ")
print(userInput)
revString=userInput[-1::-1]
print(revString)

if revString==userInput:
    print("yes its palindrome")
else:
    print("not a palindrome") """


# LIST PRACTICE QUESTIONS------------

# Task1----------
# sum all numbers in a list

""" numList=[1,2,3,4,5]
temp=0
sumall=0

for n in numList:
    temp+=n
print(temp) """


# TASK2------
# Find the max and min value in a list

""" l=[10,25,33,99,77,55]
maxVal=l[0] #10

for n in l:
    if n>maxVal:
        maxValu=n
print(maxVal) """

