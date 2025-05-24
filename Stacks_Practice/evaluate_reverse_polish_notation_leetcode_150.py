class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Timestamp in youtube tutorial mentioned in readme: 32:55
        
        This code deals with Reverse Polish Notation(Polish postfix notation) where "operators(+,-,*,/ operations) follow their operands(numbers)" instead of "operators preceding their operands" as in normal arithmentic(Polish prefix notation)
        4 - 3 + 5 is written as 4 3- 5+ 

        - We keep adding numbers to stack and if an operation comes up, pop the last two numbers and replace it with its result 


        Possible mistakes:
        - Append the numbers and not the string directly to numbers_stack
        - Dont forget to typecast div result to integer
        """
        numbers_stack = []
        possible_operators = ["+", "-", "*", "/"]
        for ele in tokens:
            if(ele not in possible_operators):
                numbers_stack.append(int(ele))
            else:
                ultimate_number = numbers_stack.pop()
                penultimate_number = numbers_stack.pop()
                if ele == "+":
                    simplify = penultimate_number + ultimate_number
                elif ele == "-":
                    simplify = penultimate_number - ultimate_number
                elif ele == "*":
                    simplify = penultimate_number * ultimate_number
                elif ele == "/":
                    simplify = int(penultimate_number / ultimate_number)
                numbers_stack.append(simplify)
        return numbers_stack.pop()
        