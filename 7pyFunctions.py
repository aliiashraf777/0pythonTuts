# ----------------
# PYTHON FUNCTIONS
# ----------------

# a function is a named block of cod edeisgned to perform a specific task.
# - it can be called multiple times in a program
# - help in reducing code repetition and improving structure
# - DEFINED using the DEF KEYWORD
# def function_name():
#   function body

# ----------
# USER DEFINED FUNCTIONS
# ----------

# a user defines a function according to his need to repeat a speicific task like

""" def printName():
  print("my name")
printName() # function call """

# you can't call your function before function definition

# ---------
# PARAMETERS & ARGUMENTS in FUNCTIONS
# ---------

# PARAMETERS: Variables listed in function definition
# ARGUMENTS: Actual value passed to the function during a call

""" def add(x,y): #x, y are parameters
return x+y
add(2,3) #2,3 are arguements """

# RETURN STATEMENT
# Sends the result from a func back to caller
# Syntax: return value
# After return, the func exits immediately

""" def square(n):
return n*N """

# print(square(4)) #output: 16

# DEFAULT PARAMETER
""" def addData(m,n=2):
    return (n+m)
print(addData(2)) """

# *X = NOT SPECIFIC X VALUES
# if values length of arguments are not clear we use it
""" def sumData(*x):
    print(x)
sumData(10,20,30,40,50) """


# -------------
# LOCAL GLOBAL VARIABLES
# -------------

# LOCAL VARIABLES
# A variable declared inside a funciton
# only accessible within that funciton
# destroyed once the function ends

""" def display():
    msg="Hello"
    print(msg) """

# GLOBAL VARIABLES
# a varible created outside the function, and accessible from anywhere

""" x=10 #global variable
def displayData1():
    x=15 #local only
    global x #now local change becomes glob
    x=15
    print(x)

def displayData2():
    print(x)` """


# ---------------
# LAMBDA FUNCTION

# a single-line anonymous function createing using 'LAMBDA' keyword
# no def, no name- used for short operations
# syntax: lambda parameters: expression

""" add = lambda a,b: a+b
print(add(2,3)) #output: 5 """

# ----------
# RECURSIVE FUNCTION

# a function taht calls itself
# useful fo rsovling complex problems by breaking them into sub-progremsl
# requires a base condition to stop recursion

""" def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)
print(factorial(5)) #output 120 """


# ------------
# PRACTICE QUESTIONS

# TASK2: write a function that takes a list and returns aonly the even numbers

""" list comprehension happning here calling a function inside same function
def getAllEvenNum(list):
    print(list)
    finalList=[]
    for a in list:
        if a%2==0:
            finalList.append(a)
    return finalList 

    # using list comprehension
    # inside a list we run a loop and that too returns loop.
    finalList=[a for a in range(1,11)]
    finalList=[ n for n in list if n%2==0 ]
    return finalList

output=getAllEvenNum([10,20,30,40,50])
print(output)

"""

# TASK 3:--------------
# obtain a list that contains  elements obtained by sum of two corresponding elements of two lists.
# list1=[1,2,3,4,5,6]
# list2=[6,5,4,3,2,1]
# result=[7,7,7,7,7,7]

""" def displayCombineList(list1,list2):
    # finalList=[]
    # for x,y in zip(list1,list2):
    #     finalList.append(x+y)
    # return finalList

    # same output using list comprehension
    finalList=[ x+y for x,y in zip(list1,list2)]
    return finalList

list1=[1,2,3,4,5,6]
list2=[6,5,4,3,2,1]

output=displayCombineList(list1,list2)
print(output) """

# TASK4:---------------
# lst=['Ali','Ashraf','Mughalzada']
# write program to obtain list of uppercase items from 1st list

""" def changeInUpper(list):
    finalList=[]
    for x in list:
        finalList.append(x.uppercase)
    return finalList

lst=['Ali','Ashraf','Mughalzada']
changeInUpper(list) """


# TASK5:---------------
# lst=['Ali','Ashraf','Mughalzada']
# write program to obtain list of uppercase items from 1st list

def avgData(*allValue):
    print(allValue)
    avg=int(sum(allValue)/len(allValue))
    return avg

print(avgData(10,20,30,40,50))