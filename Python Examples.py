##Python Examples

#--+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--#

##Python Syntax

print("Python Syntax\n")

#Print "Hello World

print("Hello World")

#Comments in python

print("Hello World") #print Hello world

#Docstrings

'''a = 34
b = "Nandan"
c = 4.56
d = True'''

print("\n")

#--+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--#

#Python Variables

print("Python Variables\n")

#Create a Variable

name = "Python"
print("create variable = ",name)

#Output both text and variable

name = "Nandan"
print("Output both text and variable: ",name + " likes programming")

#Add a variable to another variable

name = "Nandan likes to play"

play = "badminton"

print("Add a variable to another variable: ",name + play)

print("\n")

#--+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--#

#Python Numbers

print("Python Numbers\n")

#Verify the type of object

x = "Nandan"

print("Verify the type of object: ",type(x))

#Create integers

int1 = 546

print("Create integers: ",int1,type(int1))

#Create floating point numbers

float1 = 45.6765

print("Create floating point numbers : ",float1,type(float1))

#Create scientific numbers with an "e" to indicate the power of 10

e = 12E4

print("Create scientific numbers with an \"e\" to indicate the power of 10:",e)

#Create a complex numbers

complex1 = 3 + 5j

print("Create a complex numbers : ",complex1)

print("\n")

#--+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--#

#Python Casting

print("Python Casting\n")

#Casting - Integers

x = 4.5667

print("Casting - Integers {0} is".format(x),int(x),type(int(x)))

#Casting - floats

x = 76

print("Casting - float {0} is".format(x),float(x),type(float(x)))

#Casting - strings

x = 76

print("Casting - strings {0} is".format(x),str(x),type(str(x)))

print("\n")

#--+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--#

#Python Strings

print("Python Strings\n")

print("String = ","Nandan")
 
#Get the character at position 1 of string

name = "Nandan"

print("Get the character at position 1 of string: ",name[1])

#Substring, get the position from position 2 to position 5 (not included)

name = "Nandan"

print("Substring, get the position from position 2 to position 5: ",name[2:5])

#Remove whitespaces from the beginning and end of the string

name = "    Nandan   "

print("Remove whitespaces from the beginning and end of the string:",name.strip())

#Return tne length of the string

name = "Nandan"

print("Return tne length of the string: ",len(name))

#Convert the string to lower case

name = "Nandan"

print("Convert the string to lower case :",name.lower())

#Convert the string to upper case

name = "Nandan"

print("Convert the string to upper case :",name.upper())

#Replace a string with another string

name = "Nandan"

print("Replace 'd' by 'h' in string: ",name.replace("d","h"))

#Split a string into substring

name2 = "Hello Python"

print("String = ",name2)

print("Split a string into substring : ,",name2.split())

print("\n")

#--+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--#

#Python Operators

print("Python Operators\n")

x = 34

y = 7

print("x = ",x,"y = ",y)

#Addition operator

print("Addition operator of x and y : ", x + y)

#Subraction operator

print("Subraction operator of x and y : ", x - y)

#Multiplication operator

print("Multiplication operator of x and y : ", x * y)

#Division operator

print("Division operator of x and y : ", x / y)

#Modulus operator

print("Modulus operator of x and y : ", x % y)

#Assignment operator

print("Assignment operator of x as 5 : ", 5)

print("\n")

#--+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--#

#Python Lists

print("Python Lists\n")

#Create a list

list1 = [1,2,3,"Nandan",True,4.65]

print("Create a list\nlist1 = ",list1)

#Access the items in list

list1 = [1,2,3,"Nandan",True,4.65]

print("Accessing the second element in list1 = ",list1[1])

#Change the value of a list item

list1 = [1,2,3,"Nandan",True,4.65]

list1[3] = "Python"

print("Changing 'Nandan' to 'python' from list1 = ",list1)

#Loop through a list

list1 = [1,2,3,"Nandan",True,4.65]

print("Loop through a list:")

for x in list1:
    print(x,end=" ")

#Check if a list item exists

list1 = [1,2,3,"Nandan",True,4.65]

if "Nandan" in list1:
    print("\nNandan is exist in list1")

#Get the length of the list

list1 = [1,2,3,"Nandan",True,4.65]

print("the length of the list1: ",len(list1))

#Add the item to the end of the list

list1 = [1,2,3,"Nandan",True,4.65]

list1.append("Python")

print("Adding python to the list1 at the end : ",list1)

#Add an item at the specified index

list1 = [1,2,3,"Nandan",True,4.65]

list1.insert(2,"Python")

print("Adding python at position 2 in list 1: ",list1)

#Remove an item

list1 = [1,2,3,"Nandan",True,4.65]

list1.remove("Nandan")

print("Removing Nandan from list1 :",list1)

#remove last item

list1 = [1,2,3,"Nandan",True,4.65]

list1.pop()

print("Removing the last item from the list1:",list1)

#removing an item in specified index

list1 = [1,2,3,"Nandan",True,4.65]

list1.pop(3)

print("Removing Nandan from position 3: ",list1)

#Empty a list

list1 = [1,2,3,"Nandan",True,4.65]

list1.clear()

print("Clearing the items in list1 : ",list1)

#Using the list() constuctor to make a list

x = (1,2,3,4,5)

list1 = list(x)

print("converting (1,2,3,4,5) into a list1 by using list() : ",list1)

print("\n")

#--+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--#

#Python Tuples

print("Python Tuples\n")

#Create a tuple

tuple1 = (1,2,"python",4.6,True)

print("tuple1 = ",tuple1)

#Access tuple items

print("Accessing python from tuple : ",tuple1[2])

#Change tuple values

tuple1 = (1,2,"python",4.6,True)

#tuple1[2] = "Nandan"

print("Changing the value of python to Nandan in tuple1: Assignment not allowed in tuple1")

#Loop through a tuple

tuple1 = (1,2,"python",4.6,True)

print("loop through a tuple",end = ":")

for i in tuple1:
    print(i,end=" ")

#Check if a tuple item exists

tuple1 = (1,2,"python",4.6,True)

if "python" in tuple1:
    print("\nChecking if python exist in tuple1 or not")

#Delete a tuple

tuple1 = (1,2,"python",4.6,True)

#del tuple1

print("Deleting a tuple1: This will delete tuple1 permanently from database")

#Using the tuple() constuctor to create a tuple

x = [1,2,3,"Nandan",True,4.65]

print("converting [1,2,3,'Nandan',True,4.65] to tuple1 by using tuple():",tuple(x))
    
print("\n")

#--+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--#


#Python Sets

print("Python Sets\n")

#Create a set

set1 = {1,5,7,"Data science",5.6}

print("set1 = ",set1)

#Loop through the set

set1 = {1,5,7,"Data science",5.6}

print("Loop through sets: ",end = " ")

for i in set1:
    print(i,end = " ")

#Check if an item exists

set1 = {1,5,7,"Data science",5.6}

if "Data science" in set1:
    print("checking if  data science exists in set1 or not")

#Add items to a set

set1 = {1,5,7,"Data science",5.6}

set1.add(4)

print("Adding 4 to the set1: ",set1)

#Adding multiple items to a set

set1 = {1,5,7,"Data science",5.6}

set1.update({4,9,"Python"})

print("Adding {4,9,'Python'} to the set1: ",set1)

#Get the length of the set

set1 = {1,5,7,"Data science",5.6}

print("The length of set1 : ", len(set1))

#Remove an item in a set

set1 = {1,5,7,"Data science",5.6}

set1.remove("Data science")

print("Removing Data science from set1 :",set1)
 
#Remove an item in the set by using the discard() method

set1 = {1,5,7,"Data science",5.6}

set1.discard("Data science")

print("Removing Data science from set1 by using dicard() :",set1)

#Remove the last item in the set by using the pop() method

set1 = {1,5,7,"Data science",5.6}

set1.pop()

print("Removing last item in the set by using pop() : ",set1)

#Empty a set

set1 = {1,5,7,"Data science",5.6}

set1.clear()

print("Clearing all items in the set1 : ",set1)

#Delete a set

set1 = {1,5,7,"Data science",5.6}

#del set1

print("del set1:  This will delete tuple1 permanently from database")

#Using the set() constuctor to create a set

x = [1,2,3,"Nandan",True,4.65]

print("converting [1,2,3,'Nandan',True,4.65] to set1 by using set():",set(x))
    
print("\n")

#--+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--#

#Python Dictionaries

print("Python Dictionaries\n")

#Create a dictionary

dic1 = {"Nandan":"Data science","Suchi":"Java","Manu":"SAP MM"}

print("dic1 = ",dic1)

#Access the items of a dictionary

dic1 = {"Nandan":"Data science","Suchi":"Java","Manu":"SAP MM"}

print("Accessing the Suchi from dictionary: ",dic1["Suchi"])

#Change the value of a specific items in a dictionary

dic1 = {"Nandan":"Data science","Suchi":"Java","Manu":"SAP MM"}

dic1["Nandan"] = "python"

print("Changing the value of Nandan from Data science to python: ",dic1)

#Print all key values in the dictionary one by one

dic1 = {"Nandan":"Data science","Suchi":"Java","Manu":"SAP MM"}

print("Printing all keys names one by one :")

for keys in dic1:
    print(keys)

#Print all key values in the dictionary one by one

dic1 = {"Nandan":"Data science","Suchi":"Java","Manu":"SAP MM"}

print("Printing all values  one by one :")

for values in dic1:
    print(dic1[values])

#Using the values() function to return values in dictionary

dic1 = {"Nandan":"Data science","Suchi":"Java","Manu":"SAP MM"}

print("Printing the values by using values() function to return values in dictionary :")

for i in dic1.values():
    print(i)

#Loop through both keys and values, by using the items() function

dic1 = {"Nandan":"Data science","Suchi":"Java","Manu":"SAP MM"}

print("Printing the key value by using item(): ")

for i in dic1.items():
    print(i)

#Check if the key exists

dic1 = {"Nandan":"Data science","Suchi":"Java","Manu":"SAP MM"}

if "Manu" in dic1:
    print("Checking if Manu exists in dic1 or not")
 
#Get the length of dictionary
    
dic1 = {"Nandan":"Data science","Suchi":"Java","Manu":"SAP MM"}

print("Length of dictionary dic1 is ",len(dic1))


#Add an element to a dictionary

dic1 = {"Nandan":"Data science","Suchi":"Java","Manu":"SAP MM"}

dic1.update({"Jack":"Data analytics"})

print("Adding an item to dic1: ",dic1)

#Remove an item from a dictionary

dic1 = {"Nandan":"Data science","Suchi":"Java","Manu":"SAP MM"}

dic1.pop("Nandan")

print("Removing Nandan from the dic1 : ",dic1)

#Empty a dictionary

dic1 = {"Nandan":"Data science","Suchi":"Java","Manu":"SAP MM"}

dic1.clear()

print("Clearing the items in the dic1 ",dic1)

#Using the dict() constructor to create a dictionary

dic1 = dict(Nandan="Data science",Suchi="Java",Manu="SAP MM")

print("Using the dict() constructor to create a dictionary :",dic1)

#--+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--#
