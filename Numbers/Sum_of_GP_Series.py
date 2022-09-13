a, r, n = map(float, input("a, r, n - ").split())

#Method 1
sum=0
for i in range(int(n)):
    sum+=a
    a*=r
print(sum)

#Method 2
print(a*(r**n-1)/(r-1))