k,n,w = input().split() #make sure you don't leave spaces when assigning input().split() or when typecasting using a list
#w bananas,k dollar arithmetic difference per banana,has n dollars
#k, n, w = [int(i) for i in given]
#Must satisfy price =w/2(2k + (w-1)k)
k,n,w = [int(k), int(n),int(w)]
#print(type(k))
if(n- (w/2)*(2*k + (w-1)*k) >= 0):
    print(0)
else:
    print(int((w/2)*(2*k + (w-1)*k) -n))