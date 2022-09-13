arr = [1,1,2,2,2,3,3]

#Method 1
s = set(arr)
ind=0
for i in s:
    arr[ind] = i
    ind+=1
print(arr)

#Method 2
l = list()
for i in arr:
    if i not in l:
        l.append(i)
for i in range(len(l)):
    arr[i] = l[i]
print(arr)

#Method 3
i=0
for j in range(1, len(arr)):
    if arr[i] != arr[j]:
        i+=1
        arr[i] = arr[j]
print(arr)