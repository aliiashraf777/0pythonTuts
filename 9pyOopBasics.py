# ------------
# OOP IN PYTHON
# ------------

# OOP (Oject Oriented Programming) is a style of writing code where we model real-world things as objects with DATA and BEHAVIOR

# Think of MOBILE phone
# It has DATA: brand, price, model, storage
# It has BEHAVIOR: call, click, photo, browse internet
# In OOP, we represent this phone as an OBJECT, and we write code to describe it.

# WHY USE OOP:----------
# Organizes code in a cleaner, real-world way
# makes code reusable and easier to manager
# helps build large, scalble softwares.

# OOP KEY CONCEPTS:--------
# 1. CLASS - Blueprint or design
# A class is like a template for creating objs

""" class MobilePhone:
    def __init__ (self,brand,price):
        self.brand=brand
        self.price=price """

# FUNCTION VS METHOD
# Function: Standalone block of code.
# Method: Function inside a class, works, with object data.

""" def greet(): #FUNCTION
    print("hi from Function!")

class Sample:
    def greet(self): #METHOD
        print("Hi from CLASS!") """

""" class Calculator:
    def addData(self,num1,num2):
        return(num1+num2)

    def minData(self,num1,num2):
        return num1-num2

obj=Calculator()
print(obj.addData(10,20))
print(obj.jadd)
print(obj.minData(50,25)) """


# CLASS CONSTRUCTORS:---------
""" class MobilePhone:
    def __init__(self,phoneName,phonePrice):
        self.phoneName=phoneName
        self.price=phonePrice
        MobilePhone.mobileCount+=1

    def showDetails(self):
        print(f"Brand Name:{self.brand} Price {self.price}")

phone1=MobilePhone("vivo 27",10000)
phone2=MobilePhone("apple" "" 28)
phone1.showDetails()
phone2.showDetails()

print(MobilePhone.mobileCounts)
print(phone1.brand)
print(phone2.brand) """


# PRACTICE QUESTIONS:---------
# Create a class iwth attribute

""" class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary

    def showEmployeeDetails(self):
        print(f"Employee id: {self.id} \n Employee name: {self.salary} \n Price: {self.salary}\n -----------\n")

Employee1=Employee("Employee1","Employee1",130000)
Employee1.showEmployeeDetails()
print(Employee1.id) """

# TASK2:------
# Design a class Laptop with attributes like brand, model, and price. Add a method app_discount() that reduces the price by 10%

""" class Laptop:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def apply_discount(self):
        print(f"Brand name: {self.brand}")
        print(f"Model name: {self.model}")
        print(f"Brand price: {self.price}")
        discount=self.price*(10/100) #10%
        print(f"Discount applied {discount} (10%)")
        discounted_price=self.price - discount
        return print(f"discounted_price: {discounted_price}")

Laptop1=Laptop("hp","elitebook",34000)
Laptop2=Laptop("Lenovo","T14 Gen2",110000)

Laptop1.apply_discount() """


# TASK3:-----------
# Create a Customer class and a BankAccount class. Each customer can hae one Bank Account. Implement methods to DEPOSIT and WITHDRAW money

class BankAccount:
    def __init__(self,name):
        self.amount=0
        self.name=name

    def deposit(self,depAmount):
        self.amount+=depAmount

    def withdraw(self,wthdAmount):
        self.amount-=wthdAmount

    def displayAmount(self):
        print(f"Name {self.name}")
        print(f"Amount: {self.amount}")

BankAccount1=BankAccount("Ali")
BankAccount1.deposit(50000)
BankAccount1.deposit(50000)
BankAccount1.displayAmount()