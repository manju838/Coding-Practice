string1 = input().upper()
string2 = input().upper()
val = 0

# for i in range(min(len(string1),len(string2))):
#     if(ord(string1[i]) < ord(string2[i])):
#         val = -1
#     elif(ord(string1[i]) > ord(string2[i])):
#         val = 1
if (string1 < string2):
    val = -1
elif(string1 > string2):
    val = 1
else:
    val = 0


print(val)