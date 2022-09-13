arr = [2,4,1,3,5]
arr = [2,5,1,7]

arr = sorted(arr)

n=len(arr)
mid=n//2

if n%2 == 0:
    print((arr[mid]+arr[mid-1])/2)
else:
    print(arr[mid])