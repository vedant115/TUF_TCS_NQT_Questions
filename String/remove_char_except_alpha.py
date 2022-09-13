str1 = "take12% *&u ^$#forward"
str2 = "1.Python & 2.Java"
ans=""
for i in str2:
    if (i>='a' and i<='z') or (i>='A' and i<='Z'):
        ans+=i
print(ans)