s = "z2a3b7c1"
#output should be sorted with first alphabelts and then digits like, "abcz1237"
alphabets = []
digits = []
for ch in s:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        digits.append(ch)

# print(sorted(alphabets))
# print(sorted(digits))
output = "".join(sorted(alphabets)+sorted(digits))
print(output)
