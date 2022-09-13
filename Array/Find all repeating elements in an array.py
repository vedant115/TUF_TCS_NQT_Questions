arr = [1,1,2,3,4,4,5,2]

# method 1
d = {}
ans = []
for i in arr:
    d[i] = d.get(i, 0) + 1
  
for key in d:
    if d[key] > 1:
        ans.append(key)

print(ans)

# method 2

s = set()
ans = []
for i in arr:
    if (i in s) and (i not in ans):
        ans.append(i)
    s.add(i)
print(ans)

# method 3

arr = sorted(arr)
for i in range(len(arr)-1):
    if(arr[i] == arr[i+1]):
        print(arr[i], end=" ")