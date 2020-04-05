## Task1
print("Task 1\n")

#create empty list

a = []

b = [5,6,7,8,9]

#concatenate it with [5,6,8,9]

c = a + b

print("Concatenation of a and b is ",c)

d = [8,9,1,5,6,7,8]

#add 8,9,1,5,6,7,8

list1 = d + c

print("Adding the elements to the list ", list1)

#find no of occurence of 8

count1 = list1.count(8)

print("the occurance of 8 in list is ",count1)

#find average of the list

avg1 = sum(list1)/len(list1)

print("the average of the list is ",avg1)

#find sum of list + min ele + max ele of list

x = sum(list1) + min(list1) + max(list1)

print("Sum of list + min ele + max ele of list is ",x)

#find mean median of list

print("the mean of the lis1 is ",avg1)

list1.sort()

print(list1)

length = len(list1)

print("the median of the list1 ",list1[length//2])

#remove duplicates from concatenated list and give output in tuple format

tuple1 = tuple(set(list1))

print("remove duplicates from concatenated list and give output in tuple format ,",tuple1)

print("\n")

##Task2
print("Task 2\n")


#create two empty sets
set1 = set()
set2 = set()

#update set1 with 7,8,9,1,2,3,4,5,0 

set3 = {7,8,9,1,2,3,4,5,0}

set1.update(set3)

#update set2 with 4,5,6,0 

set4 = {4,5,6,0}

set2.update(set4)

#check whether set2 is subset of set 1 ?

x = set2.issubset(set1)

print("check whether set2 is subset of set 1 ",x)

#check whether both are disjoint ? 

x = set1.isdisjoint(set2)

print("check whether both are disjoint ? ",x)

#remove 8 from set1

set1.remove(8)

print("remove 8 from set1 ",set1)

#discard 0 from set2

set2.discard(0)

print("discard 0 from set2 ",set2)

#find sum(set1 union set2)

x = set1.union(set2)

print("sum(set1 union set2) = ",sum(x))

print("\n")


##Task3
print("Task 3\n")

#create two tuples (1,4,5,6,7) (5,6,7,8,9)

tup1 = (1,4,5,6,7)

tup2 = (5,6,7,8,9)

#concatenate two tuples after duplicate removal from both

tup3 = tuple(set(tup1))+tuple(set(tup2))

print("concatenate two tuples after duplicate removal from both ",tup3)

#find the index value of 9

index = tup3.index(9)

print("Index value of 9 is ",index)

#find common elements between above elements with {0,4,5} 

inter = set(tup3).intersection({0,4,5})

print("common elements between above elements with {0,4,5} is ",inter)

#multiple above tuple 3 times

print("multiple above tuple 3 times ", tup3*3)

print("\n")


##Task4
print("task 4\n")

#create a dictionary

dict1 = {1:["english","maths","science",["bio-zoology","bio-botany","physics"]],2:(10,20,40,"python program")}

#extract botany

print("extract botany: ",dict1[1][3][1][4:10])

#extract "english","maths","science" from that dictionary and convert it into  tuple and print len

dict2 = dict1[1]

#extract "english","maths","science"

dict2.pop()

#convert it into  tuple

tuple1 = tuple(dict2)

#print len

print("Length of the converted tuple = ",len(tuple1))

#print all keys in dictionary

print(dict1.keys())

#extract "python" from dictionary

print("extract \"python\" from dictionary: ",dict1[2][-1][0:6])

#add all numbers in values under key 2

dict2 = dict1[2]

dict2 =list(dict2)

dict2.pop()

print("sum of all numbers in values under key 2 : ",sum(dict2))
