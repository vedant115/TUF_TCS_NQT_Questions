# s = "javA"
s = "take u forward IS Awesome"

#Method 1
print(s.swapcase())

#Method 2
ans=""
for i in s:
    if i.isupper():
        ans+=i.lower()
    else:
        ans+=i.upper()
print(ans)

#Method 3
ans=""
for i in s:
    if ord(i)>64 and ord(i)<91:
        ans+=chr(ord(i)+32)
    elif ord(i)>96 and ord(i)<123:
        ans+=chr(ord(i)-32)
    else:
        ans+=i

print(ans)

#Method 4
ans=""
for i in s:
    if ord(i)>64 and ord(i)<91:
        ans+=i.lower()
    elif ord(i)>96 and ord(i)<123:
        ans+=i.upper()
    else:
        ans+=i

print(ans)
