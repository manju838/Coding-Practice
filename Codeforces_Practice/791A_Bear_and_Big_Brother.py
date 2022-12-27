a,b = input().split(" ") #the weight of Limak and the weight of Bob respectively.

a = int(a)
b = int(b)
t = 0
#print(type(a),type(b))

#3ta > 2tb, we need to find t
while(a <= b): #Make sure you don't ignore equality
    a = a*3
    b = b*2
    t = t+1
    #print(a,b,t)
    if(a>b):
        break

print(t)

