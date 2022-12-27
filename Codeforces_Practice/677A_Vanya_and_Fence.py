n, h = input().split(" ")
heights_list = map(int, list(input().split(" ")))
width = 0
for i in heights_list:
    if(i>int(h)):
        width +=2
    else:
        width +=1
print(width)