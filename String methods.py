#Task 1: get 2 strings from user,concatenate, find the lengrh of concatenated
#string "pnja"

a = input(" Enter first string ")
b = input(" Enter second string ")

print(a + b)

print(len(a + b))

c = len(a)

d = len(b)

print(a[0]+a[-1]+b[0]+b[-1])

print(a[0::c-1]+b[0::d-1])



#Task 2 take user input, Output " PythoN"

a = input(" Enter a string ")

length = len(a)

c = a.upper()

print(c[0] + a[1:length - 1] +c[-1])

c = a[0].upper() + a[1:-1].lower()+a[-1].upper()

print(c)


#Task 3 : Get input from user and try to convert 2 and 2nd last letter to caps

a = input( "Enter the string ")

print(a[0] + a[1].upper() + a[2:-2] + a[-2].upper() + a[-1])

#task 4 Get input from user output output(python 5 times and number length of string)

a = input("enter the string")

b = input("Enter the rep")

length = len(a)

mid = length//2

print(a * int(b) + b * length)



#Task 5 first mid and last letter to caps

print(a[0].upper()+a[1:mid].lower()+a[mid].upper()+a[mid+1:-1].lower()+a[-1].upper())



#Task 6 : User from input and Print it in this way: 55533333

x,y = input("Enter a two value: ").split()

print(x * int(y) + y *int(x))
