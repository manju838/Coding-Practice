#https://www.youtube.com/watch?v=O1KeXo8lE8A
class Questions_Practice:
    def Canonical_2_Unix_Path(self, path :str) -> str: # ->str means return type of this is str, a: int is a is integer(datatype definition)
        stack = []

        for dir in path.split("/"):
            if dir == '.':                  # If '.' then stay in current directory (don't do anything)
                pass            
            elif dir == '':                 # If there are //, then dir will be empty (don't do anything)
                pass
            elif dir == "..":               # If there is '..' then go back to parent directory iff stack is not empty
                if stack:
                    stack.pop()
                else:
                    print("Stack Empty!")
            else:                           # Normal entry
                stack.append(dir)
        
        return "/" + "/".join(stack) #join takes in iterable values like lists and joins them with the character in the quotes
                
class Find_Max_and_Min_Stack_in_order1:
    """
    Idea to find min and max values for every step is to create seperate stacks and keep appending the max/min values wrt last value
    So, O(2n) for initialization and O(1) for finding min or max values
    """
    def _init_(self):
        self.stack = []
        self.min_stack = []
        self.max_stack = []
    
    def push(self, x):
        self.stack.append(x)
        if self.stack:  # Check if stack is empty
            self.min_stack.append(min(x,self.min_stack[-1]))
            self.max_stack.append(min(x, self.max_stack[-1]))
        else:
            self.min_stack.append(x)
            self.max_stack_append(x)
    
    def pop(self):
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
            self.max_stack.pop()
        else:
            print("Empty Stack!")
    
    def top(self): #A function for peek operation
        if self.stack:
            return self.stack[-1]
        else:
            print("Stack Empty!")
    
    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            print("Empty Stack")
    
    def getMax(self):
        if self.max_stack:
            return self.max_stack[-1]
        else:
            print("Empty Stack!")
     
class Paranthesis:
    def _init_(self):
        self.stack = []

    def is_expression_Valid(self, s: str) -> bool:
        mapping = {
            "}":"{",
            "]":"[",
            "(":")"
        }

        for c in s:
            if c is "({[":
                self.stack.append(c)
            else:
                if self.stack:
                    if mapping[c] == self.stack[-1]:
                        self.stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(self.stack) == 0:
            return True
        else:
            return False
    
    def if_redundant_braces(self,s:str)->bool:
        """
        (a),((a+b)), (a+(a+b))
        There should be no operators between two braces
        Note this fn only considers curly braces
        """  
        for c in s:
            if c != ")":
                self.stack.append(c)
            else:
                non_redundant_count = 0
                while self.stack[-1] != "(":
                    popped = self.stack.pop()
                    if popped in "+-*/":
                        non_redundant_count +=1
                self.stack.pop() # This is to remove opening ( brace

                if non_redundant_count == 0:
                    return False
        return True
    # 1 hr
    def remove_min_braces_to_make_valid_expression(self, s: str) -> str:
        """
        The idea of this problem
        (Manj(unad h  )
        0123456789 10 11
        Brace at index 0 is making expression redundant, remove that and expression is valid. Given only braces can be removed
        """
        is_ok = [0] * len(s) # None of the elements of the string are going to satisfy the valid expression is the initial flags, later we will change this



