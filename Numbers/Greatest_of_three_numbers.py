a, b, c = map(int, input("enter three numbers ").split())

#Method 1 
print(max(a, b, c))

#Method 2
if (a>b and a>c):
    print(a)
elif (b>a and b>c):
    print(b)
else:
    print(c)