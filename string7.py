# reverse the content of the string using slice operator..
'''Representing in 4 ways ,....'''
x = "ramamrao"
output=""
print(x[::-1])

print(''.join(reversed(x)))

for i in range(len(x)-1,-1,-1):
    data=''.join(x[i])

n = len(x)
i = 1
while i<n+1:
    output=output+x[n-i]
    #print(x[n-i])
    i+=1
print(output)
