arr = [1,2,3,4,5,6,7]
k = int(input())
n=len(arr)

# method 1
# print(arr[n-k:] + arr[:n-k])

# method 2
# temp = []
# for i in range(n-k, n):
#     temp.append(arr[i])
# for i in range(n-1-k, -1, -1):
#     arr[i+k] = arr[i]
# for i in range(k):
#     arr[i] = temp[i]
# print(arr)

# method 3
def reverse(tmp, s, e):
    print("fun")
    global arr 
    arr = tmp[:s] + sorted(tmp[s: e+1], reverse=True) + tmp[e+1:]
    print(arr)

reverse(arr, 0, n-k)
reverse(arr, n-k, n)
reverse(arr, 0, n)

print(arr)

