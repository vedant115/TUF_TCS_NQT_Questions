arr = [2,3,1,9,3,1,3,9]

l = list()
for i in arr:
    if i not in l:
        l.append(i)
print(l)
for i in range(len(l)):
    arr[i] = l[i]
print(arr)