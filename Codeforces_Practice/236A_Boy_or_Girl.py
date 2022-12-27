user_name = list(set(input())) #list has no attribute unique,you need to use numpy array to use fn.,so go with set and then typecast to list
#print(len(user_name))
if(len(user_name)%2 ==0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!" )