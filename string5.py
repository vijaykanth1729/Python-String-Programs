#write a program to merge characters of 2 strings into a single string by taking characters alternatively..
#s1 = "RAVI"
#S2 = "TEJA"
#output="RTAEVJIA"
s1 = "RAVI"
s2 = "TEJA"
output = ""
i,j=0,0
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output = output+s1[i]
        i+=1
    if j<len(s2):
        output = output+s2[j]
        j+=1
    '''
    below logic doesnt work if both strings lengths are not same..
    '''
    # output = output+s1[i]+s2[j]
    # i+=1
    # j+=1

print(output)
