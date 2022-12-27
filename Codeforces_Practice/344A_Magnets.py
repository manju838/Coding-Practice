n = int(input())
group = 1
if n ==1:print(1)
else:
    var = int(input()) # 10
    first = int(var/10) # 1
    second = var%10 # 0
    for i in range(1,n):
        var2 = int(input()) # 01
        pre = int(var2/10) # 0
        nex = var2%10 #1
        #print(first, second, pre, nex)
        if second == pre:
            group +=1
        first = pre 
        second = nex
        #print(first, second, pre, nex)
        #print(group)

    print(group)

# Mistake: In C, num%10 will give the last number and number /10 will remove last digit.But in python it will give float number and so for 01/10,in C it returns 0 while in python it returns 0.1