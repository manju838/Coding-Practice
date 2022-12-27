s = list(input())
lower = 0
upper = 0

for i in range(len(s)):
    if(s[i].isupper()):
        upper +=1
    elif(s[i].islower()):
        lower += 1

if(upper > lower):
    print(''.join(i for i in s).upper())
else:
    print(''.join(i for i in s).lower())
