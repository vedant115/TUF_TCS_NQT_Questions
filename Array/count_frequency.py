arr = [10,5,10,15,10,5]

#method 1
n=len(arr)
visited = [0]*n
for i in range(n):
    if visited[i] == 1:
        continue
    count=1
    for j in range(i+1, n):
        if arr[i] == arr[j]:
            visited[j] = 1
            count+=1
    print(arr[i]," - ", count)

#method 2
for i in set(arr):
    print(i," - ", arr.count(i))

#method 3
d1={}
for i in arr:
    if i not in d1:
        d1[i]=0
    d1[i]+=1
print(d1)

#method 4
d2={}
for i in arr:
    d2[i] = d2.get(i, 0) + 1

print(d2)

#method 5
from collections import defaultdict
d3=defaultdict(lambda: 0)

for i in arr:
    d3[i]+=1
print(dict(d3))

#method 6
from collections import Counter

print(dict(Counter(arr)))