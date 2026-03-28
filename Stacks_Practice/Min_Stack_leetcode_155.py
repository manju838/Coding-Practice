class MinStack:
    """
    Timestamp in youtube tutorial mentioned in readme: 42:25

    Idea is to store both the value as well as the minimum value till that point in the stack node.
    
    Possible Mistakes:
    - I tried defining a variable self.min_val=None and doing a comparison (val < self.min_val) which gives an error as we cant compare None with min_val. We cant define this variable as 0 either as this stack accepts negative values.
    - I used the following way for getting the minimum value (to avoid writing self.stack.append((val, self.stack[-1][1]))):
    self.stack.append((val, min(val, self.stack.getMin())))
    
    This is incorrect as self.stack is a list and it doesnt have a fn getMin(). getMin() is a fn for MinStack class and self is the object of this class, so it should be self.getMin()

    Time Complexity: O(1)
    Space Complexity: O(1)    
    """

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            # self.stack.append((val, min(val, self.stack.getMin())))
            self.stack.append((val, min(val, self.getMin())))

        # if val < self.min_val:
        #     self.min_val = val
        # # Adding a tuple of the value to be pushed as well as the min_value
        # self.stack.append((val, self.min_val))

    def pop(self) -> None:
        popped_item = self.stack.pop() # This operation in python not just removes the top element but also returns it, so its not like accessing the element but still not touching the variable.       

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()