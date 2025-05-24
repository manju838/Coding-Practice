class Solution:
    """
    For all anagram problems like this one, grouping anagrams can be done by a hashing function, i.e input -> hashing fn,f(x) -> hash
    All anagrams will have same hash

    Approach to this problem:
    - For anagrams constructed using strings, alphabets are 26, so make generate a hash of length 26 with each digit indicating the frequency of the letter.
    - ord() fn in python takes a letter and converts it into a ASCII number, in java we do this by casting a char to an int. i.e ord('a') in python == int('a') in java
    - Add all the hash values to a hashmap and add all the input strings to the list corresponding to the hash
    
    Wrong approaches/mistakes made while trying
    - Used ord(a) instead of ord('a')
    - For encoding, use list only. i.e [0] * 26. Using string or integer directly gives errors as mentioned in alphabetical_encoding()
    - Missed braces in list(encoding_hashmap.values()) and instead used list(encoding_hashmap.values) which is incorrect 
    - Note that in groupAnagrams() strs is typecasted as a list in the leetcode boilerplate (List[str]), so the return statement is just return[strs] and not return[[strs]]
    - Thought of using set of ord() values instead (i.e {97,98,99} for string 'abc') as ord() generation for each letter is O(1) and set comparison is O(n) where n is length of set(not the entire input). The problem with this approach is it is incapable of handling duplicate letters in the string
    """
    def alphabetical_encoding(self, s:str) -> str:
        """
        This fn takes in a string and returns a onehot encoded tuple (for immutability) for all the 26 alphabets
        Eg: abc -> 111000000..(3 ones followed by 23 zeros)

        encoding = 0 * 26   ==> TypeError: 'int' object is not subscriptable
        encoding = '0' * 26 ==> TypeError: can only concatenate str (not "int") to str
        """
        encoding = [0] * 26
        for char in s:
            idx = ord(char) - ord('a') # ASCII values for [A-Z] are [65,90] while for [a-z] are [97,122]
            encoding[idx] += 1
        return(tuple(encoding)) # Tuple makes the encoding immutable

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Check if strs has a single element and return a nested list with only single element
        if(len(strs)==1):
            # print('strs',strs)
            return[strs]
  
        encoding_hashmap = {} # A hashmap to keep track of encoding as key and list of elements that generate this as value
        for ele in strs:
            ele_encoding = self.alphabetical_encoding(ele)
            if(ele_encoding not in encoding_hashmap):
                # Add encoding to hashmap if not present
                encoding_hashmap[ele_encoding] = [ele]
            else:
                # Append the list of elements generating the encoding
                encoding_hashmap[ele_encoding].append(ele)
        
        return(list(encoding_hashmap.values()))