import math
n = "11111"
N = n[::-1]
ans=""
temp=0
for i in range(len(N)):
    ind = i%3
    if N[i] == "1":
        temp += math.pow(2, ind)

    if ind == 2:
        ans += str(int(temp))
        temp=0
ans += str(int(temp))
print(ans[::-1])
