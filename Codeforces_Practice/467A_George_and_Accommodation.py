n = int(input())
count = 0
for i in range(n):
    pi, qi = input().split(" ")
    if (int(qi)- int(pi) )>= 2:
        count += 1
print(count)
