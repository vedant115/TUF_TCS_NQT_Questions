s = "Go Teams"

count=0
max=0
word=""
ans=""
for i in s:

    if i == " ":
        if count > max:
            max=count
            ans=word
        count=0
        word=""
    else:
        count+=1
        word+=i
if count > max:
        max=count
        ans=word
print(ans)