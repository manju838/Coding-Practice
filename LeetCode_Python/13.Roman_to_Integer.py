class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_HashMap = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        sum = 0
        for idx in range(len(s)):
            if(idx+1 < len(s) and roman_to_int_HashMap[s[idx]] < roman_to_int_HashMap[s[idx+1]]):
                sum -= roman_to_int_HashMap[s[idx]]
            else:
                sum += roman_to_int_HashMap[s[idx]]
        return(sum)


