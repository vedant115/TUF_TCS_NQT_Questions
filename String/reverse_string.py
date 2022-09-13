str1 = "take u forward"
str2 = "I am very happy today"

# Method 1
print(str1[::-1])
print(str2[::-1])

# Method 2
print("".join(list(reversed(str1))))
print("".join(list(reversed(str2))))

#Method 3
ans=""
stack = []
for i in str1:
    stack.append(i)
while stack:
    ans+=stack.pop()
print(ans)

#Method 4
ans = list(str1)
for i in range(len(ans)//2):
    ans[i], ans[-1-i] = ans[-1-i], ans[i]
print("".join(ans))