'''
Plays using the complement numbers principle, take no. and check if complement is present in HashMap (dictionary), if yes give indices of current element, complement from HashMap else just add this element into HashMap. 
Note: HashMap adds only elements and their indices, complements are computed realtime and checked.

Time Complexity: O(n)
Space Complexity: O(n)'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevHashMap = {}
        for idx,element in enumerate(nums):
            complement = target - element
            if complement in prevHashMap:
                return([prevHashMap[complement], idx])
            prevHashMap[element] = idx
        return