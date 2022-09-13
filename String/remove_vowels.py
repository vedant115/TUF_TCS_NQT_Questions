str1 = "take u forward"
str2 = "I am very happy today"

def removeVow(str):
    ans = ""
    s=str.lower()
    for i in range(len(s)):
        if s[i] == 'a' or s[i] == 'i' or s[i] == 'e' or s[i] == 'o' or s[i] == 'u':
            continue
        else:
            ans+=str[i]
    return ans

print(removeVow(str1))
print(removeVow(str2))