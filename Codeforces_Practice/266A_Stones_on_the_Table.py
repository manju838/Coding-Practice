n = int(input()) #The number of stones on the table
#Needed: Count the minimum number of stones to take from the table so that any two neighboring stones had different colors
count = 0
#colors = input().split("") #When you don't have a seperator,directly concatenate but if you have something in the middle then use split
colors = list(input())
for i in range(len(colors) -1):
    if(colors[i] == colors[i+1]):
        count +=1
print(count)