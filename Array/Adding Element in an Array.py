arr = [1,2,3,4,5]

def addBeg(n):
    arr.append(0)
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = n
    return arr
print((addBeg(0)))

def addEnd(n):
    # arr.append(n)
    arr.append(0)
    arr[len(arr)-1] = n
    return arr
print((addEnd(6)))

def addAtPos(n, pos):
    arr.append(0)
    for i in range(len(arr)-1, pos, -1):
        arr[i] = arr[i-1]
    arr[pos] = n
    return arr
print(addAtPos(8, 3))