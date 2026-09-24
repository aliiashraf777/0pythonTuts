# -------------------
# FILE HANDLING IN PYTHON
# -------------------

# FILE DATA-READ
# FILE DATA-WRITE
# FILE DATA-APEND


# FILE-MODES IN PYTON
# MODE | dESCRIPION

# 'r' - Read (default), file must exist1
# 'w' - Write, creates or truncates file
# 'a' - Append to file
# 'r+' = read & write
# 'w+' = write and read
# 'a+' = append and read
# 'b' = Binary mode - imgs reading

""" file=open("demo.txt","w")
file.write("welcome to file handling\n")
file.write("2nd line \n")

# to write multiple lines at onece
file.writelines(["line 1\n", "line 2\n", 'line 3\n'])
file.close() """

# FILE POINTER FUNCTIONS:----------
# tell() - returns current position
# seek(offset) - moves to specified position
# file.seek(0)
# post = file.tell()


# same above file handling using "with"
""" with open("demo.txt", "r") as file:
    # file.writelines("line 1\n", "line 2\n", "line 3\n")

    print(file.read()) 
    # when it ran cursor moves to end of line - we use seek()
    file.seek(0)
    print(file.readlines())
    file.seek(0)
    list=file.readlines()
    print(list)
    file.seek(0)
    print(file.readlines())
    print(file.tell())
    file.seek(0)
    print(file.tell())

with open("demo.tsx","a") as file:
    file.writelines(["mubashir","ashraf","mughalzada"])
    file.seek()
"""

# File With "w+" mode
""" file=open("base.txt","w+")
file.write("base file with w+")
file.seek(0)
print(file.read())
file.seek(0)
file.close() """


# PRACTICE QUESTIONS:-----------

# TASK1:-------
# write a program to read a text file and count the number of words.

""" file=open("count.txt","w")
data=file.writelines(["line 1\n","line 2\n","line 3\n"])
file.seek(0)
print(data)
file.seek(0)
file.close()

# file=open("count.txt","r+")

with open("count.txt","r") as file:
    data=file.read().split(" ")
    print(data)
    print("word count",len(data)) """


# TASK2:-------
# create a program to copy the content of one file into another

""" with open("demo.txt","r") as file:
    data=file.read()

    file2=open("copy.txt","w")
    file2.write(data)
    file2.close()
    file.close() """

# TASK3:------
# write a func to find how many times a word appears in a file.

""" def getMyWord(fileName,word):
    with open(fileName,"r") as file:
        data=file.read().lower().split(" ")

        countMyWord=data.count(word.lower())
        file.seek(0)
        return countMyWord

print(getMyWord("demo.txt","line")) """

# TASK4:------
# create a file and store 5 lines using writelines()

with open("lines5.txt","w+") as file:
    file.writelines(["line 1\n","line 2\n","line 3\n","line 4\n","line 5\n"])
    file.close()
