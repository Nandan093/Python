#with/without vowel check
a = ["hello", "bcd", "gcd", "hhmmm", "python"]
print("Input list ",a)
vowel= []
without_vowel = []

for i in a:
    if ("a" in i or "e" in i or "i" in i or "o" in i or "e" in i):
        vowel.append(i)
    else:
         without_vowel.append(i)

print("The list with vowels ", vowel)
print("The list without vowels ",without_vowel)


#Starts with h :

h = []

for i in a:
    if(i[0] == "h"):
        h.append(i)

print("The list with first letter h ",h)

#Ends with d

d =[]

for i in a:
    if(i[-1] == "d"):
        d.append(i)

print("The list with last letter d ",d)
