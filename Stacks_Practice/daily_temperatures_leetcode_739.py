class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Timestamp in youtube tutorial mentioned in readme: 19:20
        
        If using bruteforce approach, time complexity is O(n^2)
        In this problem we are using temperature values just for comparison and we are actually returning index values that satisfy the condition. 
        As we traverse the array, if we are trying to solve this in one array pass, we might need to compare multiple temperature values quickly and array does this in O(1)
        So we maintain an array that has our results and a stack that keeps track of all the elements that dont satisfy the condition
        So we store the index differences (our outputs) and since we need the closest values that satisfy this condition, LIFO based stack will workout 

        Our approach is as follows:
        - First create an array that stores the results to be returned and initialise them to 0
        - Create a stack(which is implemented using an ArrayList, a List in python)
        - We have 3 cases: when stack is empty, when stack has multiple indices and condition is satisfied, when stack has multiple indices and condition is not satisfied
        - We need to iterate through the input array but we are focussed on indices, so we use range instead of outright using "for ele in temperatures:"
        - We have to loop until condition is satisfied, so we use while loop
        - When condition is not satisfied, we just need to add the index to stack, so we keep it outside the loop

        One small note:
        We defined peek_idx inside the while loop as it needs to be updated. But the condition checking cant see this 
        """
        idx_stack = []
        temp_length = len(temperatures)
        result_array = [0] * temp_length

        for idx in range(temp_length):
            while(len(idx_stack)!=0 and temperatures[idx] > temperatures[idx_stack[-1]]):
                peek_idx = idx_stack[-1]
                idx_diff = idx - peek_idx
                result_array[peek_idx] = idx_diff
                idx_stack.pop()
            idx_stack.append(idx)
        
        return result_array
                
                 