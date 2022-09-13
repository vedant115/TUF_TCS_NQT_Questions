str = "HI AMY AND JAY"

# Method 1
ans = 0
for i in str:
    if i == " ":
        ans+=1
ans+=1
print(ans)

# Method 2
print(len(str.split()))

# Method 3
print(str.count(" ")+1)
