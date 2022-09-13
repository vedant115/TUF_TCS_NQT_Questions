s = "zxcbg"
# s = "edcba"

#Method 1
l = list(s)

for i in range(len(s)-1):
    for j in range(len(s)-1-i):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]

print("".join(l))

#Method 2
print("".join(sorted(s)))