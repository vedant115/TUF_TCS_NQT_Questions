s = "abcdxyz"
# s="Java"

ans = ""

for i in s:
    if i == "Z":
        ans+="A"
    elif i == "z":
        ans += "a"
    else:
        ans+=chr(ord(i)+1)

print(ans)