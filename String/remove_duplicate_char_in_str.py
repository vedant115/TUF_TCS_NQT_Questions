s = "bcabc"

ans = ""

for i in s:
    if i not in ans:
        ans+=i

print(ans)

