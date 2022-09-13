arr = [4, 2, 8, 6, 15, 5, 9, 20]
arr = [8, 7, 1, 6, 5, 9]

arr = sorted(arr)
for i in range(0, len(arr)//2):
    print(arr[i], end=" ")

for j in range(len(arr)-1, len(arr)//2-1, -1):
    print(arr[j], end=" ")