# https://leetcode.com/problems/integer-to-roman/description/?envType=problem-list-v2&envId=math

class Solution:
    def intToRoman(self, num: int) -> str:
        # Note the table highest to lowest, so that we can do greedy approach
        symbol_to_val = [
            ("M",1000),
            ("CM", 900),  # Subtractive case
            ("D",500),
            ("CD", 400),  # Subtractive case
            ("C",100),
            ("XC", 90),   # Subtractive case
            ("L",50),
            ("XL", 40),   # Subtractive case
            ("X",10),
            ("IX",9),     # Subtractive case
            ("V",5),
            ("IV", 4),    # Subtractive case
            ("I",1),  
        ]           
        res_str = []

        for sym,val in symbol_to_val:
            if(num/val !=0):
                rep = num//val
                res_str.append(rep*sym)
                num -= rep*val
        return "".join(res_str)