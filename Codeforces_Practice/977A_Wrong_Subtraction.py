n,k = input().split(" ") #the number from which Tanya will subtract and the number of subtractions correspondingly.

n = int(n)
k = int(k)

for i in range(k):
    if(n%10 !=0):
        n = n-1
    else:
        n = n/10
print(int(n))