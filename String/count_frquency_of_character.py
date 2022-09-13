s = "takeuforward"

#Method 1
d = {}
for i in s:
    d[i] = d.get(i, 0) + 1

for key in d:
    print(key, end="")
    print(d[key], end=" ") 

print()
#Method 2
s = "takeuforward"
s = sorted(s)
ch=s[0]
count=0
for i in s:
    if i == ch:
        count+=1
    else:
        print(ch, end="")
        print(count, end = " ")
        ch = i
        count = 1

print(ch, end="")
print(count, end = " ")