arr = [1,2,3,2,4,3,1,2]
arr = [-199,6,7,-199,3,5]

d = {}
arr = sorted(arr)
for i in arr:
    d[i] = d.get(i, 0) + 1

arr = sorted(d, key=lambda x: d[x], reverse=True)

ans=[]
for i in arr:
    ans += [i] * d[i]
print(ans)