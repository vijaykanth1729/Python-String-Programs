#write a program to print the characters are present at even index and odd index seperately for the given string??
s1 = "abcdefgh"
i=0
print("The characters present at even index")
while i<len(s1):
    print(s1[i])
    i+=2

i=1
print("The characters present at odd index")
while i<len(s1):
    print(s1[i])
    i+=2
#Alternatively we can do below snippet to do same thing..
# print(s1[0::2])
# print(s1[1::2])
