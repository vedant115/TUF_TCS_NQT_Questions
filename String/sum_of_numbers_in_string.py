str1 = "123xyz1xyz23"

#method 1
tot=0
n=""
for i in str1:
    if i.isdigit():
        n+=i
    else:
        if n != "":
            tot+=int(n)
            n=""
tot+=int(n)
print(tot)


#method 2 
arr=[]
n=""
for i in str1:
    if i.isdigit():
        n+=i
    else:
        if n != "":
            arr.append(int(n))
            n=""
arr.append(int(n))
print(sum(arr))