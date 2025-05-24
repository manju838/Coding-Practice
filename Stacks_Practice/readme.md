## Stacks - Last In First Out[LIFO] 

Youtube Tutorial Video: https://www.youtube.com/watch?v=k1IaYPGel3s


- Linear datastructure(datastructure where elements are sequentially arranged and can be easily traversed like arrays, linkedlists, stacks, queues.)

Operations in Stack(All are O(1) time complexity):
- Push : Add an element to stack
- Pop  : Remove last/top element from stack
- Peek : View the last/top element in stack

- Stacks are implemented using ArrayList in java. 
- Array and ArrayList are two inbuilt java datastructures, with Array being a fixed size, accepts single datatype values while ArrayList can accept multiple datatypes and variable sizes
- In Python ArrayList is called List

Special Syntax Difference:
In Python:
```python
fruits = ['apple', 'banana', 'cherry']
x = fruits.pop(1)
print(x) # banana
print(fruits) # ['apple', 'cherry']
```
As shown above we can access not just the last element but even other elements using pop, though default will be last value. 
**Also array_list.pop() will return the last value in Python while it returns the index of the last element in Java.**

Applications of Stack:
1) Undo/back btn in browser
If you go through website1 -> website2 -> website3  and the press back btn, it pops website3 from stack, does a peek operation to find website2 and opens that site
1) Backtracking Mechanism
* Assume we are doing a DFS search, we go through the left nodes of a tree to reach the last node and still didnt find the value we are searching for, we backtrack one step back and search through the right subtree, and if not found we baccktrack two steps to reach a higher level and check for the right subtree.
* This problem can be engineered as follows: Go through a node, see if it has left subtree, add each central node of this tree and go to the last node while checking if we found our target value. If yes then return, else pop the last value stored in stack, do a peek and check if it has all the subtrees traversed. If yes, then pop that node else traverse the right subtree.
1) Parenthesis checker
While parsing through the parenthesis checker, if the bracket is a left opening type then add it to stack and if a right opening type is encountered, you get its left counterpart from a hashmap, do a peek and check if it matches. If yes, then pop the last bracket and continue traversal else return False. This application is used in IDEs and compilers.
