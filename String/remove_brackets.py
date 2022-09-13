str1 = "a+((b-c)+d)"
str2 = "(((a-b))+c)"

ans=""
for i in str1:
    if i != "(" and i != ")":
        ans+=i
print(ans)