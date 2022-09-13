s = "sinstriiintng"

#Method 1
d = {}
for i in s:
    d[i] = d.get(i, 0) + 1

for key in d:
    if d[key] > 1:
        print(key,"-", d[key])

#Method 2
arr = [0]*26

for i in s:
    arr[ord(i)-ord('a')] +=1

for i in range(len(arr)):
    if arr[i] > 1:
        print(chr(ord('a')+i), "-", arr[i])


