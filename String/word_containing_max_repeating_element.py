# s = "abcdefghij google microsoft"
s = "cameron blue"

words = s.split()
ans=""
max=0
for w in words:
    count=0
    for i in w:
        if w.count(i) > 1:
            count+=1
    if count > max:
        max=count
        ans=w
if ans == "":
    print("-1")
else:
    print(ans)