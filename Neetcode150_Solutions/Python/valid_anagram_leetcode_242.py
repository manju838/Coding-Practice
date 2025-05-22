class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Hashmap Approach:

        1) Version1:
        - Use hashmap which is dictionary in python
        - Idea is that anagrams have same string length and same letter frequency per string
        - Check if lengths of strings are same and if not return False
        - Iterate over string1(s), Note the frequency of s in hashmap
        - Iterate over string2(t), Reduce frequency by 1 for every letter in t, if frequency of a letter is 0, then delete the key from hashmap
            * if letter not present in hashmap return False
            * if length of hashmap is 0(empty hashmap) after reducing the frequency for all letters of t, then return True 
        
        2) Version2:
        - Check if both strings are of same length else return False
        - Don't use 2 loops, use the same index to either increment or decrement the hashmap by 1.
        - Delete any keys in hashmap with frequency 0.
        - If length of hashmap is 0, then return True

        Important -> **Version1 is faster because:**
        - range(len(s)) is indirect addressing as we iterate through index and then get the value while version1 simply gets the next value without index
        - If letters of s and t have -1 and 0 before entering the loop, 2 variables are reassigned values+ 2 variables are deleted while for version1 number of conditionals is far less per loop

        Time Complexity: O(n)
        Important -> **Space Complexity: O(1) since we are using a hashmap of size 26**
        
        Array Approach:
        - Check if length of both strings is same else return False
        - Since both strings are consist entirely of alphabets, use an array of size 26 and keep track of frequency in one of the 26 indices
        - For second string decrease the frequency from the corresponding index and if the entire array is 0s then its True
        - This approach needs function alphabet2index() which is present in java (charAt() function) but not in python
        
        Timestamp ending in youtube tutorial mentioned in readme: 18:30 
        """
        # Version1:
        if(len(s) != len(t)):
            return False
        hashmap = {} # Create a dictionary
        # Iterate through first string
        for element in s:
            if(element not in hashmap):
                # Add if element not present in dict
                hashmap[element] = 1
            else:
                # Increment the letter frequency
                hashmap[element] += 1
        
        for element in t:
            if(element not in hashmap):
                return False
            hashmap[element] -=1
            if(hashmap[element]==0):
                # Remove the key if frequency is 0
                del hashmap[element]
        if(len(hashmap) == 0):
            # If hashmap is empty, then it is anagram
            return True

        # Version2:

        # # Check if string lengths are same
        # if(len(s) != len(t)):
        #     return False
        # # Create a hashmap/dictionary
        # hashmap = {}
        # for element in range(len(s)):
        #     # Deal with s[element], increasing frequency in hashmap
        #     if(s[element] not in hashmap):
        #         # Add element into hashmap
        #         hashmap[s[element]] = 1
        #     else:
        #         # Increment element in hashmap
        #         hashmap[s[element]] += 1
            
        #     # Deal with t[element], reducing frequency in hashmap
        #     if(t[element] not in hashmap):
        #         # Add element into hashmap
        #         hashmap[t[element]] = -1
        #     else:
        #         # Increment element in hashmap
        #         hashmap[t[element]] -= 1
            
        #     # Remove keys with frequency 0, checking if element is present or not in hashmap is important if same element is present in both s[element] and t[element] then second delete will give error
        #     if(s[element] in hashmap and hashmap[s[element]] == 0):
        #         del hashmap[s[element]]

        #     if(t[element] in hashmap and hashmap[t[element]] == 0):
        #         del hashmap[t[element]]

        # if(len(hashmap) == 0):
        #     # If hashmap/dict is empty
        #     return True
        # else:
        #     # some element is not removed, so not anagram
        #     return False




        