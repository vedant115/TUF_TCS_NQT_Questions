n = int(input("Enter Number : "))

mx=0
mn=99999
while n:
    digit = n%10
    mx = max(mx, digit)
    mn = min(mn, digit)
    n//=10

print("Largest digit: ",mx , "\nSmallest digit: ", mn)
