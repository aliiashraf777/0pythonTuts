# -----------
# TUPLE
# -----------

# An ordered immutable collection of items, defined using parenthesis()
# can contain mixed data types
# my_tuple=(1,"apple",3.14)
""" 
tuple=(10,20,30,40)

# on it works all slicing formulas
print(tuple[-1])
print(tuple[0])

# ITERATIONS from TUPLE
for n in tuple:
    print(n)

# TUPLE FUNCTIONS

m=max(t) #max value
print(m)
min=print(min(t)) #min value
print(min)
print(sum(t))
"""


# --------------
# DICTIONARY in Python
# --------------

""" an unordered, mutable, collection of key-value pairs
Defined using {}
my_dict = {"name": "ali","age":25 """

""" key features
keys must be unique}
values can be of any tupe
supports dynamic updates """

""" dict={
    1:10,
    "name":"ali",
    "age":10,
    "courseName":["pythonFastApi","mern","JAVA"]
} 
print(dict[1])
print(dict.get(1))
print(dict["age"])
print(dict.get("agess")) #error - key not present - gives NONE
print(dict["ages"]) #gives key error
print(dict["courseName"][1]) """

# for structured data we use DICTIONARY
""" student={
    "ST01":["Ali","ali@gmail.com"],
    "ST02":["Ashraf","ashraf@gmail.com"],
    "ST03":["Mughalzada","mughalzada@gmail.com"],
}
print(student["ST02"]) """

""" # Dictionary Methods
dict={
    1:10,
    "name":"ali",
    "age":10,
    "courseName":["pythonFastApi","mern","JAVA"],
    "phone":"iPhone"
}

# .keys() method - by default gives keys
print(student.keys()) # creates list
for key in student.keys():
    print(key)
    print(key,student[key])

# .values() method
print(student.values()) #creates values list
for values in student.values():
    print(values)

# .items() method
print(student.items())
for key,values in student.items():
    print(key,values)

# .get() method
print(dict.get("email","ali@gmail.com")) #fallback value also takes.

# .update(key,value) method
dict.update({"name":"Ali Ashraf"})
print(dict)

# update add method
dict["duration"]="4 years"

# delete method
print(dict)
del dict["1"]
print(dict)

# .pop() .popitem() method
print(dict,"before pop")
print(dict.pop("phone"))
print(dict,"after pop")

key,value=dict.popitem()

# .clear()
dict.clear()
print("dictionary after dict.clear() running")
 """

# -----------------
# SET in PYTHON
# -----------------

""" 
In Python a set is an unordered collection data type that stores UNIQUE ELEMENTS. Setars are defined using curly braces {} or by using built-in set() function
- an unordered, mutable, collection of UNIQUE  ELEMENTS
my_set={1,2,3,4,5}

no duplicate values
useful for membership testing
"""

set={1,2,3,4,5}
print(set,type(set))

for item in set:
    print(item)

# SETS METHODS IN PYTHON -------
set.add(6)
print(set)

# UNION IN SETS
# brings all values of both set, no duplicate
s1={1,2,3}
s2={3,4,5}

s3=s1.union(s2)
print(s3)

# INTERSECTION
s4=s1.intersection(s2)
print(s4)
print(s3)

p5=s1.difference(s2)