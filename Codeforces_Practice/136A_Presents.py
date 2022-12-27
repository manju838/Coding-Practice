n, friend_list, dictionary = int(input()), map(int, input().split(" ")), {}
for i, j in enumerate(friend_list):
    dictionary[j] = i+1
for i in range(n):
    print(dictionary[i+1], end = ' ')
