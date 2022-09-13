str1 = "Take you forward"
str2 = "How are you doing"

print(str1.replace(" ", ""))
print("".join(str1.split()))

# method 1
ans=""
for i in str2:
    if i != " ":
        ans+=i
print(ans)

# method 2

def remove_spaces(str):
    ans=['0']*len(str)
    count=0
    for i in str:
        if i != " ":
            ans[count]=i
            count+=1
    return("".join(ans)).rstrip('0')
print(remove_spaces(str1))