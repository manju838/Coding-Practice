#Make sure to use python3,I faced a problem earlier due to version,and don't use s[i] to add values,it gives index out of range error,use concatenation or append initially and when printing then use index
s = []
n = int(input())#No.of follow up lines
#print(n)
for i in range(n):
    k = input()
    #print("k",k)
    s.append(k)

# print(s)

for i in range(n):
    if len(s[i]) <= 10:
        print(s[i])
    else:
        print(s[i][0] + str(len(s[i])-2) + s[i][-1])

    