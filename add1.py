def add():
    num=[]
    for i in range(4):
        val = int(input())
        num.append(val)
    
    sum = 0
    for i in range(4):
        if num[i]%2 == 0:
            sum = sum + num[i]
    return("sum",sum)
print(add())