n, a, d = map(int, input().split())

#Method 1
sum=0
for i in range(n):
    sum+=a
    a+=d
print(sum)

#Method 2
print((n/2.0)*(2.0*a+(n-1)*d))