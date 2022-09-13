arr = [9, 4, 1, 7 , 6, 2]

# method 1
mn=smn=999999
mx=smx=0

for i in arr:
    if i < mn:
        mn=i
    if i > mx:
        mx=i

for i in arr:
    if i < smn and i != mn:
        smn = i
    if i > smx and i != mx:
        smx = i


print("second min",smn,"\nsecond max", smx)

# method 2

mn1=smn1=999999
mx1=smx1=0

for i in arr:
    if i < mn:
        smn=mn
        mn=i
    elif i < smn and i != mn:
        smn=i
    if i > mx:
        smx=mx
        mx=i
    elif i > smx and i != mx:
        smx = i

print("second min",smn,"\nsecond max", smx)

# method 3

arr = sorted(arr)
print("second min", arr[1])
print("second max", arr[-2])