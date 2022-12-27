n = input()
#number is nearly lucky if the number of lucky digits in it is a lucky number

total = n.count("4") + n.count('7')
if total == 4 or total == 7:
    print("YES")
else:
    print("NO")
