# ------------
# OOP ADVANCE CONCEPTS
# ------------

# INHERITENCE
# POLYMORPHISM
# ENCAPSULATION
# MODULES

# INHERITENCE:--------
# Allows a class (child) to inherit properties and methods from another class (parent)
# promotes code reuse

# Syntax
""" class Vehicle:
    def start(self):
        print("Engine Started")

class Car(Vehicle):
    def music(self):
        print("Playing music")

car1=Car()
car1.start() #from parent
car1.music() #from child """

#--------
# Types of Inheritance
#--------

# 1. SINGLE INHERITANCE
# 2. MULTIPLE INHERITANCE
# 3. MULTILEVEL INHERITANCE
# 4. HIERARICHAL INHERITANCE
# 5. HYBRID INHERITANCE

# 1-SINGLE INHERITANCE:------
# Once CHILD class inherits from one PARENT class

""" class ElectronicDevice:
    def power_on(self):
        print("Powering On")

class Laptop(ElectronicDevice): #inheriting Parent class
    def code(self):
        print("coding on laptop")

laptop1:Laptop()
laptop1.power_on()
laptop1.code() """

# 2-MULTIPLE INHERITANCE
# One CHILD inherits from more than ONE PARENT class
# like a SMARTPHONE inherits from CAMERA & PHONE

""" class Camera:
    def take_photo(self):
        print("taking photo")

class Phone:
    def make_call(self):
        print("Calling someone")

class Smartphone(Camera, Phone):
    # multiple inherits
    def touche_screen(self):
        print("multiple inherits, multile parents")

Smartphone1=Smartphone()
Smartphone1.take_photo()
Smartphone1.make_call()
Smartphone1.touche_screen()
 """

# 3-MULTILEVEL INHERITANCE:-------
# A class INHERITS a CLASS, which inherits from ANOTHER class
# like: EV inherits from CAR, and CAR inherits from VEHICLE

""" class Vehicle:
    def move(self):
        print("vehicle moving")

class Car(Vehicle):
    def drive(self):
        print("car driving")

class EV(Car):
    def charge(self):
        print("Charging EV battery")

ev1=EV()
ev1.move()
ev1.drive()
ev1.charge() """

# 4-HIERARCHICAL INHERITANCE:---------
# A parent pass inheritance to MULTIPLE CHILDS

""" class Appliance:
    def power_on(self):
        print("Appliance is on")

class Fan(Appliance):
    def rotate(self):
        print("Fan rotating")

class Ac(Appliance):
    def cool(self):
        print("AC cooling")

fan1=Fan()
fan1.power_on()
fan1.rotate()

ac1=Ac()
ac1.power_on()
ac1.cool() """

# 5-HYBRID INHERITANCE
# Combination of two or more types of inheritance
# like: SmartTV inherits from TV (single), and TV inherits from ElectronicDevice(multilevel), plus adds INTERNET features (MULTIPLE)

""" class ElectronicDevice:
    def start(self):
        print("Device started")

class TV(ElectronicDevice):
    def display(self):
        print("TV displaying")

class Internet:
    def stream(self):
        print("Streaming online")

class SmartTv(TV, Internet):
    def hybridInheritance(self):
        print("hybrid inheritance example")

smartTv1=SmartTv()
smartTv1.start()
smartTv1.display()
smartTv1.stream()
smartTv1.hybridInheritance() """


# --------------
# POLYMORPHISM:-----------