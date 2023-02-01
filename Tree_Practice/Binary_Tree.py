'''
Set is a type of internal datastructure that eliminates duplicate elements but it lacks the ordering of elements(unordered datastructure)
Binary tree is a datastructure that has atmost 2 nodes
Binary Search Tree(BST) is a datastructure that stores data inorder to leverage both the set's functionality as well as ordering

Binary Search operation and binary search tree search operation both will be of O(logN) but binary search tree prevents duplicate entries so its better to construct and use a binary search tree instead of a list when skimming through large chunks of data

Traversal Techniques
    |___Breadth first search
    |___Depth First Search
            |___In order Traversal : Inorder refers to root or central node. In this traversal central node is traversed in order==> Left subtree -> Central Node -> Right subtree
            |___Pre order Traversal : Preorder refers to root or central node. In this traversal central node is traversed pre/before ==> Central Node -> Left subtree -> Right subtree
            |___Post order Traversal : Postorder refers to root or central node. In this traversal central node is traversed post/after ==> Left subtree -> Right subtree -> Central Node

Since BST is arranged as left part < central part < right part, inorder traversal automatically sorts entries while removing duplicates
If entries are strings or names, then they are sorted alphabetically using BST inorder traversal


The height of the node is the distance between the node and the farthest leaf node
So, height of a leaf node is 0, the layer above it is 1 and so on.

Level on the other hand is counted top down, i.e root node is level 0, the next one is level 1 and so on.
'''

class Binary_Search_Tree_Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        '''
        We need to check if the value already exists in the BST or not so we are using data instead of just adding a preinstantiated node like in tree datastructure
        '''
        if data == self.data:
            return
        
        if data < self.data:
            # Add in left tree

            # Check if left tree is not empty
            if self.left:
                self.left.add_child(data) # If the left subtree is not empty then the subtree is another tree so perform recursion
                # pass
            else:
                # If left tree is empty(reached leaf node) then instantiate a node and link it using self.left pointer
                self.left = Binary_Search_Tree_Node(data)
                # pass

        else:
            # Add in right tree

            # Check if right tree is not empty
            if self.right:
                self.right.add_child(data) # If the right subtree is not empty then the subtree is another tree so perform recursion
                # pass
            else:
                # If right tree is empty(reached leaf node) then instantiate a node and link it using self.right pointer
                self.right = Binary_Search_Tree_Node(data)
    
    def in_order_traversal(self):

        '''
        We are creating a list of elements and returning it, so this may exceed runtime if tree is very huge due to sheer number of write(append) operations

        In traversal, the base case is visiting base node itself as if the leaf node has no left or right nodes then base case will be visiting base/central node
        '''
        elements = []
        #Visit Left Subtree
        if self.left:
            elements += self.left.in_order_traversal() 

        #Visit Central / Base Node
        elements.append(self.data)

        #Visit Right Subtree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
        
    def pre_order_traversal(self):
        '''
        We are creating a list of elements and returning it, so this may exceed runtime if tree is very huge due to sheer number of write(append) operations
        '''
        elements = []

        #Visit Central / Base Node
        elements.append(self.data)

        #Visit Left Subtree
        if self.left:
            elements += self.left.pre_order_traversal()

        #Visit Right Subtree
        if self.right:
            elements += self.right.pre_order_traversal()        
        return elements

    def post_order_traversal(self):
        '''
        We are creating a list of elements and returning it, so this may exceed runtime if tree is very huge due to sheer number of write(append) operations
        '''
        elements = []

        #Visit Left Subtree
        if self.left:
            elements += self.left.post_order_traversal()

        #Visit Right Subtree
        if self.right:
            elements += self.right.post_order_traversal()

        #Visit Central / Base Node
        elements.append(self.data)

        return elements

    def BST_search(self, val):
        '''
        This function searches if the val exists in the binary search tree and returns True or False accordingly
        '''
        if self.data == val:
            return True

        if val < self.data:
            # Check in the left subtree
            # Check if left subtree exists
            if self.left:
                return self.left.BST_search(val) # If return is not used here, since there is no base function None will be returned instead of True/False
            else:
                return False

        if val > self.data:
            # Check in the right subtree
            # Check if right subtree exists
            if self.right:
                return self.right.BST_search(val)
            else:
                return False

    def find_min(self):
        '''
        The left most node is minimum, so traverse until self.left is None and return it else just call find_min() recursively
        '''
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        '''
        The right most node is maximum, so traverse until self.right is None and return it else just call find_max() recursively
        '''
        if self.right is None:
            return self.data
        return self.right.find_max()

    def calculate_sum(self):
        '''
        As the calculate_sum() propagates until self.left, left_sum will be the left node and right_sum will be the right node, so add all three and return from the highest level(leaf node's trio i.e left leaf, right leaf and base nodes)
        '''
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return left_sum + self.data + right_sum

    def delete_node(self, val):

        # Check if node to be deleted(value) is in left subtree
        if val < self.data:
            # Check if self.left is present
            if self.left:
                self.left = self.left.delete_node(val) # If return is used then testcase failing for deleting 17(wrong answer => [1, 4, 9, 18])
                ####### Check if self.left is absent we need to return None but that is taken care by Python, in other languages need to specify

        # Check if node to be deleted(value) is in right subtree
        elif val > self.data:
            # Check if self.right is present
            if self.right:
                self.right = self.right.delete_node(val)
                ####### Check if self.right is absent we need to return None but that is taken care by Python, in other languages need to specify

        # Check if node to be deleted(value) is center/base node and 
        else:
            # Check if node to be deleted(value) is center/base node and both left,right subtrees are absent
            if self.left is None and self.right is None:
                return None
            
            # Check if node to be deleted(value) is center/base node and left subtree is absent
            if self.left is None:
                return self.right
            # Check if node to be deleted(value) is center/base node and right subtree is absent
            elif self.right is None:
                return self.left
            
            '''
            We can either take the maximum value from left subtree or the minimum value from the right subtree to replace the deleted node
            
            Using minimum value from right subtree
            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right = self.right.delete_node(min_val)
            '''

            # Using maximum value from left subtree
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete_node(max_val)

        return self

def build_tree(elements):
    '''
    This function uses the first element of the elements list as the root node
    '''
    root = Binary_Search_Tree_Node(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 18, 4] # This list even has duplicates to check if set functionality is working
    numbers_tree = build_tree(numbers)
    # print("In order Traversal: ",numbers_tree.in_order_traversal())
    # print("Pre order Traversal: ",numbers_tree.pre_order_traversal())
    # print("Post order Traversal: ",numbers_tree.post_order_traversal())
    # print(numbers_tree.BST_search(20))
    # print(numbers_tree.BST_search(8))
    # print("Maximum Value: ",numbers_tree.find_max())
    # print("Minimum Value: ",numbers_tree.find_min())
    # print("Sum: ",numbers_tree.calculate_sum())

    numbers_tree.delete_node(20)
    print("After deleting 20 ",numbers_tree.in_order_traversal()) # this should print [1, 4, 9, 17, 18, 23, 34]

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34, 18, 4])
    numbers_tree.delete_node(9)
    print("After deleting 9 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 17, 18, 20, 23, 34]

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34, 18, 4])
    numbers_tree.delete_node(17)
    print("After deleting 17 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 9, 18, 20, 23, 34]

