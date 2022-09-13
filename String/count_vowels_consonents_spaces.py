
def returnCount(s):
    
    vow = ['a', 'e', 'i', 'o', 'u']
    countVow = 0
    countCon = 0
    countSpa = 0
    for i in range(len(s)):
        if s[i].lower() in vow:
            countVow+=1
        elif s[i].lower() == ' ':
            countSpa+=1
        else:
            countCon+=1

    print(" vowels : {}\n consonants : {}\n spaces : {}".format(countVow, countCon, countSpa))

def returnCount2(s):
    countVow = 0
    countCon = 0
    countSpa = 0

    s = s.lower()
    for i in s:
        if i == 'a' or i == 'i' or i == 'e' or i == 'o' or i == 'u':
            countVow+=1
        elif i > 'a' and i <= 'z':
            countCon+=1
        elif i == ' ':
            countSpa+=1
    print(" vowels : {}\n consonants : {}\n spaces : {}".format(countVow, countCon, countSpa))

str1 = "Take u forward is Awesome"
str2 = "India won the cricket match"

returnCount2(str1)
returnCount2(str2)