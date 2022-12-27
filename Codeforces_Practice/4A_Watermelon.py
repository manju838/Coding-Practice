w = int(input())#w is weight of watermelon
#Weight w must be divided into two even no.s,so our w is even
if(w%2 ==0 and w > 2):
    print("YES")
else:
    print("NO")