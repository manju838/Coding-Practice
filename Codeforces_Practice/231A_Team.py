counter = 0
n = int(input())#No.of problems in contest
for i in range(n):
    s1,s2,s3 = input().split(" ")
    if(int(s1) + int(s2) + int(s3) >=2):
        counter +=1
    
print(counter)