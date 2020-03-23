#Task 1: get 2 strings from user,concatenate, find the lengrh of concatenated
#string "pnja"

a = input(" Enter first string ")
b = input(" Enter second string")

print(len(a + b))

print(a[0]+a[-1]+b[0]+b[-1])



#Task 2 take user input, Output " PythoN"

a = input(" Enter a string")

length = len(a)

c = a.upper()

print(c[0] + a[1:length - 1] +c[-1])
