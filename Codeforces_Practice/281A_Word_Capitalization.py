string = list(input()) #'str' object does not support item assignment,so I converted it to list
string[0] = string[0].upper()
#print(string) #['M', 'a', 'n', 'j', 'u'] for word manju,so we need to join
print(''.join(i for i in string))