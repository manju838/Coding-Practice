n = 27
base_3_convert = ""
while(n):
    base_3_convert += str(n%3)
    n /= 3
        # print(len(base_3_convert))
a = reversed(base_3_convert)
for i in a:
    print(i)

# 27  9   3   1
# 0   0   0   1

#