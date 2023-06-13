def Vowel(s):
    l=["a","e","i","o","o","A","E","I","O","U"]
    res=""
    for i in s:
        if i not in l:
            res+=i;
    return res

s=input()
outputstring=Vowel(s)
print(outputstring)