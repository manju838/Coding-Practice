n,t = map(int, input().split(" ")) #represent the number of children in the queue and the time after which the queue will transform into the arrangement you need to find
# n = int(n)
# t = int(t) #map fn is used to map the variable to a particular datastructure,so the same work of type casting by these commented lines can be done using it

queue = list(input())

for i in range(t): #Since t gives the no.of transformations or passes needed
    j = 1
    while j < n: # counter which is limited to no.of children,since its comparison I can start from 1 and not 0
        if queue[-j] == 'G' and queue[-j-1] == 'B': #Since I chose and started from 1,go in reverse direction
            queue[-j], queue[-j-1] = queue[-j-1], queue[-j]
            j += 2
        else:
            j += 1

print(''.join(queue))

# # for i in range(t):
# #     for j in range(0,n):
        
# #         if(s[j-1] == "B" and s[j] == "G"):
# #             s[j-1] = "G"
# #             s[j] = "B"
# #             print(s)
# #             j = j+1        

# for i in range(t): #t is the no.of passes through the string
#     for j in range(1,n+1): #n is the no.of children,I need to check 2 people at a time and then skip them, Eg:n = 5 =>(1,2),(3,4),5
#         if(j+1 <= n+1):
#             if(s[j] == 'B' and s[j+1] == 'G'):
#                 s[j] = 'G'
#                 s[j+1] = 'B' #I completed this set of (j,j+1),so we need to now go to j+2
#                 j = j+1 #I am increasing ine here,when the next loop comes in I will increase another 1
                
        
# print(''.join(i for i in s))

