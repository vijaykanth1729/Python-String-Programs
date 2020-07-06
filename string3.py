'''
print(ord('a'))==>97
print(chr(97))==>'a'
'''

input = "a4k3d2"

# ouput should be "aekndf" getting the net alphabet charcaters from current value of string..
output = ""
for ch in input:
    if ch.isalpha():
        output = output+ch
        x = ch
    else:
        newc = chr(ord(x)+int(ch))  # here using ord and chr functions to track the unicode conversions..
        output = output+newc
print(output)
