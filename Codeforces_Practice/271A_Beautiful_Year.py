y = int(input())
#the minimum year number that is strictly larger than y and all it's digits are distinct
y +=1
while len(set(str(y))) != len(str(y)):
    y +=1

print(y)
