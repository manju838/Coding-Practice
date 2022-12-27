arr = [] 

# The j-th integer in the i-th line of the input represents the element of the matrix that is located on the intersection of the i-th row and the j-th column.
#A matrix looks beautiful, if the single number one of the matrix is located in its middle

#Needed: So my no. must be at arr[2][2]
for i in range(5):
    a, b, c, d, e = input().split(" ")
    k = [int(a), int(b), int(c), int(d), int(e)]
    arr.append(k)
    if(1 in k):
        row = i
        for j in range(5):
            if(arr[i][j] == 1):
                col = j
                break
print(abs(row - 2) + abs(col - 2))

#print(arr)


