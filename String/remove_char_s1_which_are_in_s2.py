s1 = "abcdef"
s2 = "cefz"

temp = ""

for i in s1:
    if i not in s2:
        temp+=i

print(temp)