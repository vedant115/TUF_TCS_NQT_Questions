str =  "ABCDCBA"

# method 1
if str == str[::-1]:
    print("palindrome")
else:
    print("not palindrome")

# method 2
flag=0
for i in range(len(str)//2):
    if str[i] != str[-1-i]:
        flag=1
        break
if flag != 1:
    print("palindrome")
else:
    print("not palindrome")