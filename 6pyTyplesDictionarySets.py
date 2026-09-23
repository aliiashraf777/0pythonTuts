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
In Python a set is an unordered collection data type that stores UNIQUE ELEMENTS. Sets ars are defined using curly braces {} or by using built-in set() function
- an unordered, mutable, collection of UNIQUE  ELEMENTS
my_set={1,2,3,4,5}

no duplicate values
useful for membership testing
"""
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

# DIFFERENCE in sets of python
# provides those values which are not present in difference being checked by set
s6=s1.difference(s2) #1,2 is output
s7=s2.difference(s1) #4,5 is difference
 """

# ================================
# PRACTICE QUESTIONS
# ================================

# Task01------
# Count word frequency sentence = "python is fun and python is powerful"

""" sentence="python is fun and python is powerful"
list=sentence.split(" ") #['python','is',...]
wordCount={}

for word in list:
    print(word)
    wordCount[word]=wordCount.get(word,0)

# wordCount['python]=0+1 wordCount={"python":1}
# wordCount['is']=0+1 wordCont={'python':1,'is:1, 'fun':1}
print(wordCount) """


# TASK2-------
# Swap key and values data={'a':1,'b':2,'c':3}

""" 
data={'a':1,'b':2,'c':3}
finalAns={}

for k,v in data.items():
    print(k,v)
    finalAns[v]=k
print(finalAns)
 """

# TASK3-------
# Sum All Values prices={'apple':100,'banana':40,'cherry':60}

prices={'apple':100,'banana':40,'cherry':60}
# allValues=prices.values()
# print(sum(allValues))

""" total=0
for price in prices.values():
    print(price)
    total+=price
print(total) """


# TASK4-------
# find key with Max Values cores={'Alice':50,'Bob':70,'Charlie':65}

""" cores={'Alice':50,'Bob':70,'Charlie':65}

maxValueKey=''
maxValue=0

for k,v in cores.items():
    if v>maxValue:
        maxValue=v
        maxValueKey=k

print(maxValueKey, maxValue) """


# TASK5-------
# Group by Length words=["cat","dog","apple","banana","to","on"]

""" words=["cat","dog","apple","banana","to","on"]

groupWord={}

for v in words:
    length=len(words)
    if length not in groupWord:
        groupWord[length]=[v]
    else:
        groupWord[length].append(v)
print(groupWord) """
