arr = [1,2,-1,1,3,1]

# method 1
d = {}
ans = []
for i in arr:
    d[i] = d.get(i, 0) + 1
for key in d:
    if d[key] == 1:
        ans.append(key)
print(ans)

# method 2

for i in arr:
    if arr.count(i) == 1:
        print(i, end=" ")