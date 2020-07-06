input = "a4b3c2z3d1"
#expected output should be "aaaabbbccz"
output = ""
for chr in input:
    if chr.isalpha():
        x = chr
    else:
        output = output+x*int(chr)
print(output)
