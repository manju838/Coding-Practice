class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Timestamp in youtube tutorial mentioned in readme: 0:30
        Approach:
        - Create a set(hashset in python is set) to store all no.s, if unique present then return true
        - Time Complexity: O(n) [saving every element to hashset{O(n)}, checking if element is present in hashset{n elements * O(1) for each hashset search, total n+n = O(n)}]
        - Space Complexity: O(n) [since we are saving entire nums array]

        """
        hashset = set() 
        for element in nums:
            if(element in hashset):
                return True
            else:
                # Add new element in hashset
                hashset.add(element)
        return False # If loop is executed without triggering return True, then it is False
