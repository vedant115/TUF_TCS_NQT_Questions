str1 = "Hello"
str2= "World"

#Method 1
print(str1 + str2)

#Method 2
print(str1, end="") 
print(str2)

#Method 3
print("".join([str1, str2]))

#Method 4
print("%s%s"%(str1, str2))

#Method 5
print("{}{}".format(str1, str2))
