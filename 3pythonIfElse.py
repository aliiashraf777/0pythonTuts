# -------------
# Python Conditional Statements
# -------------

# use to contrl the flow of the program based on conditions

# 1. If Statement
'''
age=18
if age>=18;
    print("eligible vote")
'''

'''
age=input("Enter age: ")
age=int(input("enter age:")) #20
print(age,type(age))
age=float(input("enter age")) #22.5
print(age,type(age))
age=eval(input("enter age")) #user any input
print(age,type(age))

if age>=18:
    print("yes")
    print(age)

    print("yes",end='')
    print(age)
'''

# 2. if-else
'''
num=eval(input("enter number:"))
if num%2==0:
    print("event")
else:
    print("odd")
'''

# 3. if-elif-else ladder
'''
marks=eval(input("add marks"))
if marks>=90:
    print("grade a")
elif marks>=75:
    print("grade b")
elif marks>=60:
    print("grade c")
else:
    print("fail")
'''

# 4. nested if
'''
num=eval(input("add num"))
if num>0:
    if num%2==0:
        print("even")
    else:
        print("+ odd num")
'''

# 5. match case (like switch)
'''
num1=eval(input("enter val1"))
num2=eval(input("enter val2"))
userCh=input("enter user choice") #*,-,/,*
print(num1)
print(num2)
print(userCh)

match userCh:
    case "+":
        print("num1+num2",num1+num2)
    case "-":
        print("num1-num2",num1-num2)
    case "*":
        print("num1*num2",num1*num2)
    case "/":
        print("num1/num2",num1/num2)
'''


# ------------
# Practice Tasks
# ------------

# Tas1
# check zero,positive, -ive num

'''
num=eval(input("enter num"))

if num==0:
    print(num, "zero")
elif num>0:
    print(num, "positivie")
else:
    print(num,"negative num")
'''


# Task2
# check if a year is a leap year or not
# year=eval(input("add year"))
# if (year%4==0 and year%100!=0) or (year%400==0):
#     print(year,'leap year')

# Task3
# check if a number is ivisible by both 3 & 5
# num=eval(input("add num"))
# if (num%3==0 and num%5==0):
#     print(num)

# Task4
# menu-driven clculator (using if-elif-else)
