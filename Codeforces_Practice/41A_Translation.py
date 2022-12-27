print("YNEOS"[(input()[::-1]!=input())::2]) 
#Slicing is [<start> : <stop> : <step>]
#Take first input, input()[::-1],so don't care about start and stop as its not given but check for step -1 => abcd -> dcba
#If dcba != abcd then value is true or 1 else its false or 0 
# Now  value is YES if this is 0 else 1, stop value is not given but step is 2