s = "aaaabbbccz"
#expected output should be 4a3b2c1z
previous = s[0]
c=1
i=1
output=""
while i<len(s):
    if previous==s[i]:
        c=c+1
    else:
        output = output+str(c)+previous
        previous = s[i]
        c = 1
    if i ==len(s)-1:
        output = output+str(c)+previous
    i = i+1
print(output)
