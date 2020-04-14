#write a function to check string is palindrome or not

def string1(x):
    if (x == x[::-1]):
        print("Palindrome")
    else:
        print("Not palindrome")

string1(input("Enter the number from user "))

#------------------------------------------------------------------------#

# write function to check whether a no is odd or even

def number1(x):
    if (x % 2 == 0):
        print("Number is Even")
    else:
        print("Number is odd")

number1(int(input("Enter the number from user ")))

#------------------------------------------------------------------------#


# write function to check whether a no is +ve or -ve

def number1(x):
    if (x > 0):
        print("Number is positive")
    else:
        print("Number is negative")

number1(int(input("Enter the number from user ")))

#------------------------------------------------------------------------#

# get two numbers from user and do below process (a + b)(a - b)

def multiple(x , y):
    val = (x + y) * (x - y)
    return val

a = int(input("Enter first number "))
b = int(input("Enter second number "))

print(multiple(a,b))

#------------------------------------------------------------------------#

# get three numbers from user and do below process (a + b)(a - b)(a-c)

def number(x, y, z):
    val = (a + b) * (a - b) * (a - c)
    return val

a = int(input("Enter first number "))
b = int(input("Enter second number "))
c = int(input("Enter third number "))

print(number(a,b,c))
