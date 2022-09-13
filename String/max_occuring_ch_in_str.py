s = "apple"

# Method 1

temp = {}
max=0
ans=""
for i in s:
    temp[i] = temp.get(i, 0) + 1
    if temp[i] > max:
        max = temp[i]
        ans = i

print(ans)


#Method 2
s = sorted(s)
ch=s[0]
count=0
max=0
ans=""
for i in s:
    if i == ch:
        count+=1
    else:
        if count > max:
            max = count
            ans = ch
        ch = i
        count = 1
if count > max:
    max = count
    ans = ch
print(ans)