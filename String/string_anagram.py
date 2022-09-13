s1, s2 = map(str, input().split())

#Method 1
def countChars(s):
    temp = {}
    for i in s:
        temp[i] = temp.get(i, 0) + 1
    
    return temp

print(countChars(s1) == countChars(s2))

#Mehtod 2
s1 = sorted(s1)
s2 = sorted(s2)

print(s1 == s2)

# OR

flag = 0
for i in range(len(s1)):
    if s1[i] != s2[i]:
        flag=1
        print("False")
        break
if flag == 0:
    print("True")

# Method 3
d={}

for i in s1:
    d[i] = d.get(i, 0) + 1

for i in s2:
    d[i] = d.get(i, 0) - 1

flag = 0
for key in d:
    if d[key] != 0:
        flag = 1
        print("False")
        break
if flag == 0:
    print("True")