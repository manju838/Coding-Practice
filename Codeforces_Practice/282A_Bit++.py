n = int(input()) #the number of statements in the programme
x = 0 #Initial value Given
#The operation and the variable can be written in any order. i.e ++x and x++ are equal

for i in range(n):
    if( "++" in input()):
        x +=1
    else:
        x-=1
print(x)
