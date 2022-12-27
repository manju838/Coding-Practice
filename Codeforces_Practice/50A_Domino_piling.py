
m,n = input().split(" ")

if(int(m)%2 == 0 and int(n)%2 != 0):
    #even_side = m
    val = (int(m)/2)*int(n)
    
elif(int(n)%2 == 0 and int(m)%2 != 0):
    #even_side = n
    val = (int(n)/2)*int(m)
    
elif(int(m)%2 != 0 and int(n)%2!= 0):
    val = (int(m)//2)*int(n) + int(n)//2    
    
else:
    #int(m)%2 == 0 and int(n)%2 == 0
    val = (int(m)/2) * int(n)

print(int(val))