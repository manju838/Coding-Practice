class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Timestamp in youtube tutorial mentioned in readme: 18:35 

        - Since sum of 2 numbers is target, both the numbers are complementary of each other.
        - Given exactly one soln, so we can return if we get soln.
        - Bruteforce approach would be going through each element and checking if its complement is in array{O(n^2)}
        - So, instead of looping as mentioned above, if we can get the index of complement in O(1) once we pass through the element, it is most efficient.
        - Iterate through the array, Use a hashmap(dictionary in python) to store the complement of the element with index of the element and check if element is present in hashmap 
        Time Complexity: O(n) for array traversal + n*O(1) for hashmap lookup = O(n)

        """
        hashmap = {}
        idx = 0 # Track the index of element
        for element in nums:
            # Check if element in hashmap
            if(element in hashmap):
                return [hashmap[element], idx]
            else:
                # Store the complement of the element as key and index of the element as value
                hashmap[(target-element)] = idx
            
            idx +=1



        