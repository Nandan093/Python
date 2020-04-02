
list1 = [1,2,3,4,5,"Hello"]  # List

tuple1 = ("Nandan","Hello",4,6,8)  #Tuple

set1 = {"World",4,3,1,7,"hi"}    #Sets

#-----------------------------------------------------------------------#

#Conversion of list to Tuple

output = tuple(list1)

print("Conversion of list to tuple: ",output)

#Output - Conversion of list to tuple:  (1, 2, 3, 4, 5, 'Hello')

#-----------------------------------------------------------------------#

#Conversion of list to set

output = set(list1)

print("Conversion of list to set: ",output)

#Output - Conversion of list to set:  {1, 2, 3, 4, 5, 'Hello'}

#-----------------------------------------------------------------------#

#Conversion of tuple to list.

output = list(tuple1)

print("Conversion of tuple to list: ",output)

#Output - Conversion of tuple to list:  ['Nandan', 'Hello', 4, 6, 8]

#-----------------------------------------------------------------------#

#Conversion of tuple to set.

output = set(tuple1)

print("Conversion of tuple to set: ",output)

#Output - Conversion of tuple to set:  {'Hello', 4, 6, 8, 'Nandan'}

#-----------------------------------------------------------------------#

#Conversion of set to list

output = list(set1)

print("Conversion of set to list: ",output)

#output - Conversion of set to list:  [1, 3, 4, 7, 'hi', 'World']

#-----------------------------------------------------------------------#

#Conversion of set to tuple

output = tuple(set1)

print("Conversion of set to tuple: ",output)

#Output - Conversion of set to tuple:  (1, 3, 4, 7, 'hi', 'World')

#-----------------------------------------------------------------------#




