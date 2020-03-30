#1. Difference between copy() and assignment (=)

  #copy() - this function is to copy the elements from other list.

#E.g.,

a = [1,2,3,4,5]

b = a.copy()

print("Copy of list is ",b)

  #Assignment(=): its just assigning the list with other variables

b = a

print("Assigning list to other variables ",b)


#2. difference between del() function and clear() function

    #del() - this function is to remove the specific index.

a = ["nandan", 3, True,5.54]

del a[3]

print("Deleting the value in list ",a)

    #remove() - this function is to remove element from the list.

a = ["Nandan", 3, True, 5.54]

a.remove("Nandan")

print("Removing the element from list ",a)

#3 how to reverese the list.

    #reverse()- this function is used to reverse the list according to index.


a = ["Nandan", 3, True, 5.54]

a.reverse()

print("Reversing the elements in list ",a)


