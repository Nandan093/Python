#Capitalize() ( Converts the first character to upper case )

a = "nandan"

print(a.capitalize())


#casefold() (Converts string into lower case)

a = "NANDAN"

print(a.casefold())


#center() (Returns centered string, it will make thr string to center of the length given in())

a = "Nandan"

print(a.center(10))


#count() (Returns the number of times a specified value occurs in a string)

a = "nandan"

print(a.count("n"))


#encode() (Returns an encoded version of the string,returns binary value on a string)

a = "Nandan"

print(a.encode())



#endswith()   (Returns true if the string ends with the specified value)

a = "Nandan"

print(a.endswith("n"))


#expandtabs() (Sets the tab size of the string, need to give escape sequence in string5)

a = "N\ta\tn\td\ta\tn"

print(a.expandtabs(6))


#find() (Searches the string for a specified value and returns the position of where)

a = "Nandan"

print(a.find("N"))


# format() (Formats specified values in a string)

course = "python"

print("I love {0} ".format(course))



#index() (Searches the string for a specified value and returns the position of where it was found)

a = "Nandan"

print(a.index("d"))


#isalnum() (Returns True if all characters in the string are alphanumeric)

a = "Nandan"

print(a.isalnum())
 


#isalpha()  Returns True if all characters in the string are in the alphabet

a = "Nandan"

print(a.isalpha())




#isdecimal() (Returns True if all characters in the string are decimals)

a = "10"

print(a.isdecimal())



#isdigit()  (Returns True if all characters in the string are digits)

a = "12345677"

print(a.isdigit())


#isidentifier()	(Returns True if the string is an identifier/variable)

a = "Nandan"

print(a.isidentifier())


#islower()  (Returns True if all characters in the string are lower case)

a = "nandan"

print(a.islower())


#isnumeric() (Returns True if all characters in the string are numeric)

a = "1234567"

print(a.isnumeric())


#isprintable()	(Returns True if all characters in the string are printable)

a = "Nandan\n I am here"

print(a.isprintable())



#isspace()  (Returns True if all characters in the string are whitespaces)

a = "       "

print(a.isspace())


#istitle()  (Returns True if the string follows the rules of a title)

a = "Hello, I Am Nandan"

print(a.istitle())


#isupper()  (Returns True if all characters in the string are upper case)

a = "NANDAN"

print(a.isupper())


#join()	(Joins the elements of an iterable to the end of the string)

x = ["I","Am","Nandan"]

print(",".join(x))


#ljust() (Returns a left justified version of the string)

a = "Nandan"

print(a.ljust(7),"loves python programming")


#lower() (Converts a string into lower case)

a = "NANDAN"

print(a.lower())


#lstrip() Returns a left trim version of the string

a = "___Nandan"

print(a.lstrip("_"))


#partition() (Returns a tuple where the string is parted into three parts)

a = "I am Nandan"

print(a.partition('Nandan'))


#replace() (Returns a string where a specified value is replaced with a specified value)

a = "Nandan"

print(a.replace("n","d"))


#rfind() (Searches the string for a specified value and returns the last position of where it was found)

a = "nandan"

print(a.rfind("n"))


#rindex() (Searches the string for a specified value and returns the last position of where it was found)

a = "Nandan"

print(a.rindex("N"))


#rjust() (Returns a right justified version of the string)

a = "Nandan"

print(a.rjust(8))


#rpartition() (Returns a tuple where the string is parted into three parts)

a = "Nandan hates lagging"

print(a.rpartition("hates"))


#rsplit() (Splits the string at the specified separator, and returns a list)

a = "Nandan is a programmer"

print(a.rsplit(" "))


#rstrip()   (Returns a right trim version of the string)

a = "Nandan_____"

print(a.rstrip("_"))


#split() Splits the string at the specified separator, and returns a list

a = "Nandan is a programmer"

print(a.split(" "))


#splitlines() (Splits the string at line breaks and returns a list)

a  = "Hello\n I am Nandan"

print(a.splitlines())


#startswith() (Returns true if the string starts with the specified value)

a = "Nandan"

print(a.startswith("N"))


#strip() (Returns a trimmed version of the string)

a = "    Nandan     "

print(a.strip(" "))


#swapcase() (Swaps cases, lower case becomes upper case and vice versa)

a = " I am Nandan"

print(a.swapcase())


#title() (Converts the first character of each word to upper case)

a = "i am nandan"

print(a.title())


#upper() (Converts a string into upper case)

a = "nandan"

print(a.upper())


#zfill() (Fills the string with a specified number of 0 values at the beginning)

a = "I am Nandan"

print(a.zfill(13))
