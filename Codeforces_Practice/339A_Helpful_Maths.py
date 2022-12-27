"""
I am taking input by appending into a list but as a matter of fact,input().split("+") itself creates a list,so what I am writing is a list of lists.
So I am unable to convert string list into an int list.The below are my incorrect implementations
arr = [input().split("+")]
print(arr) #[['2', '1', '3']]
        (or)
arr = []
arr.append(input().split("+"))
"""
arr = input().split("+")
#print(arr)
arr = list(map(int, arr)) #map fn maps a datatype with a elements of a list.So first map list with required datatype and typecast to list is pretty important skill to manage data
#arr_list = [int(i) for i in arr] #Even this works fine
#print(type(arr[0]))
arr.sort()
#print(arr)
print('+'.join(str(i) for i in arr)) #Make sure to typecast with string before joining and whatever is written between quotes(+ here) will be the joiner,just opposite to seperator in split()