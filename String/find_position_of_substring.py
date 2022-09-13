s1 = "takeuforward"
s2 = "az"

def findIndex(s1, s2):
    for i in range(len(s1)):
        temp=i
        for j in range(len(s2)):
            if s1[temp] != s2[j]:
                j-=1
                break
            temp+=1
        if (j+1 == len(s2)):
            return i
    return -1


print(findIndex(s1, s2))