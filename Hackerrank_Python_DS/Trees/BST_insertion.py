class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        #Enter you code here.
        # The first important note is this fn. is a part of a class so self needs to be used appropriately
        new_node = Node(val)
        # If tree is empty
        if self.root is None:
            self.root = new_node
            return
        # If tree not empty, get a pointer
        cur = self.root
        while cur:
            # val < cur.info
            if val < cur.info:
                # If left subtree is empty
                if cur.left is None:
                    cur.left = new_node
                    return
                # If left subtree is not empty
                cur = cur.left
            elif val > cur.info:
                # If right subtree is empty:
                if cur.right is None:
                    cur.right = new_node
                    return # If this return is not used then we need to write elif statement
                # If right subtree is not empty
                cur = cur.right
            
                    
        
        

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
