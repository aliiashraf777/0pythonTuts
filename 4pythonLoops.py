# -----------
# Python Loops
# -----------

# For Loop
# A FOR loop is used to iterate over a sequence(like a list, tuple, dictionary, string or a range of numbers).

# Syntax:
# for variable in sequence: 
    #Code block

# example
'''
fruits=["apple","banana","cherry"]
for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)
'''

# -------------
# Range in Python For loop
# -------------
""" range(5)
  start - 0 | stop - (5-1) | step+1

range(1,10)
start=1 | stop=10-1 | step+1

range(1,11,2)
start=1 | stop=11-1 | step+2 """

# -------------
# using range in For loop
# -------------
""" range(5)
for r in range(5):
    print(r,"r in range(5)")

for r in range(1,6):
    print(r,"r in range(1,6)")

for x in range(1,21,2):
    print(x,"x in range(1,21,2)") """

""" range(10,0,-1)
start(10) | stop(>0=1) | dec(-1)
for r in range(10,0,-1):
    print(r,"r in range(10,0,-1)")
print("------------------") """

""" for r in range(20,0,-2):
    print(r,"r in range(20,0,-2)") """


# iterating string using for loop
""" word="welcome"
for letter in word:
    print(letter,"letter in word") """

# iterating list using python
""" list=[10,20,30,40,50]
for element in list:
    print(element,"element in list")
 """

# end="" prints in same line
""" for n in range(1,6):
    print(n,end="")
print("")
for n in range(1,6):
    print(n,end=" ") """


# ------------------
# NESTED LOOP
# ------------------

""" for r in range(1,6):
    for n in range(1,6):
        print(n,end=" ")
    print("") """


# ---------------
# printing natural no's tables
# ---------------
""" for n in range(1,11):
    print(n)
    for t in range(1,11):
        print(n,"x",t,"=",n*t)
    # print('')
    print("------------") """


# ---------------
# WHILE loop in python
# ---------------

# it doesn't iterate from string,list,dictionary etc
# it needs a number or true to run
""" start=1
while start<=10:
    print(start)
    start+=1
print(start) #it gives last value = 11 """

'''
n=10
while n>=1:
    print(n)
    n-=1
    print(n)
'''


# ----------------
# Loop Control Statements
# ----------------

# PASS: do nothing (used as placeholder)
# Example:
# for a in range(10):
#     pass

# BREAK => exit the loop entirely
# Example:
'''
for a in range(1,101):
    if a%3==0 and a%5==0:
        print(a)
        break
'''

# CONTINUE => skip the rest of the current loop ITERATION
# Example:
'''
for n in range(1,11):
    if n==5:
        continue
    print(n)
'''
    
# --------------
# Practice Questions
# --------------

# TASK1: -------
# Sum of First 10 natural numbers
'''
total=0
for n in range(1,11):
    print(n)
    total+=n
print("")
print(total)
'''

# TASK2: -------
# Check if a number is a Perfect Number.
# A number is Perfect number if its divisible's sum(not including itself) is Equal to Number

# Example:
# 6 -> divisibles are 1+2+3 = 6
# so we'll sum to num%n==0 then compare to num

""" num=eval(input("enter a num: "))
perfTotal=0
for n in range(1,num):
    if num%n==0:
        print(n)
        perfTotal=perfTotal+n
print("---")
print(perfTotal)
print("---")

if perfTotal==num:
    print(num,"is perfect number")
else:
    print(num, "is not a perfect number") """


# TASK3: -----
# Check if a number is Prime
# Number which are divisble by 1 and itself no any inbetween number upto itself
# after 1/2 of a number, any no can't divide a number
# Example: 7

""" num=eval(input("enter a num")) #21
isPrime=True

midVal=num//2  #10
#1 is always true so skipped it
for n in range(2,midVal): 
    if num%n==0:
        isPrime=False
        break

if isPrime:
    print(num,"is prime")
else:
    print(num,"is not prime") """


# TASK4: -----
# Reverse a number using while loop
""" num=eval(input("enter the value: ")) #1234
print(num)
revNum=0
numLen=0

while num>0:
    numLen=numLen+1
    lastDigit=num%10 #4
    revNum=revNum*10+lastDigit #0*10+4 = 4
    num=num//10
print(revNum) """

# TASK6: -----
# Right-angle triangle of stars

n=5
# *
# **
# ***
# ****
# *****

for r in range(1,6):
    for c in range(1,r+1):
        print("*",end="")
    print()