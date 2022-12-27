n = int(input()) #the number of the tram's stops. 
a = []
total = 0
#The number of people who exit at a given stop does not exceed the total number of people in the tram immediately before it arrives at the stop.

for i in range(n):
    x,y = input().split(" ")

    total = total + int(y) - int(x)
    a.append(total)
    if(total < 0):
        print("Terminated")
        break
    
print(max(a))