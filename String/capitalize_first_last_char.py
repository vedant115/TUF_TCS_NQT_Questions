str = "take u forward is awesome"

arr = str.split()

for i in range(len(arr)):
    if len(arr[i]) > 1:
        temp = arr[i][0].upper() + arr[i][1:len(arr[i])-1] + arr[i][-1].upper() 
        arr[i] = (temp)
    else:
        arr[i] = (arr[i].upper())
print(arr)