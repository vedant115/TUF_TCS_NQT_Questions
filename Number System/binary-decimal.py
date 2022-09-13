no = "1001"
base=1
ans=0
for i in range(len(no)-1, -1, -1):
    if no[i] == "1":
        ans+=base
    base*=2

print("ans - ",ans)