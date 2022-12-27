n, k = input().split(" ")#n is no.of participants,k is last participant who will advance to next round,remember to change to int
s = [int(n) for n in input().split()]
val = 0
# for i in range(int(n)):
#     s.append(input())

# print(s)
# print("k",s[int(k) - 1])
"""
Analysis:
My first mistake is taking the input via an array while in question,everything is given in a single line,space seperated.
My second and most important was not taking 0 into consideration.   
Though the code works for general cases if an array of 0's are given like in the below example,it goes wrong

4 2
0 0 0 0
I corrected this mistake by making an if else case to prevent if all inputs are zero
if(s[int(k) - 1]!=0 and s[0] !=0):
    val = int(k) #Since desending order all k participants will move on to next round and kth participant is (k-1) index
    for i in range(int(k),int(n)):
        if(s[i] >= s[int(k) - 1]):
            val +=1
        else:
            break
    
else:
    val = 0
------
But if the inputs have a combination of both 0's and positive values like given below,my code fails.So I wrote the crude solution which worked
5 5
3 2 1 0 0

"""

for i in range(len(s)):
    if(s[i] >= s[int(k) - 1] and s[i] > 0):
        val +=1

print(val)