class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    #Write your code here
    '''
    Here we need two variables one that is vertical like root is at origin and an x-axis kind of measurement and one is the level/ y-axis kind of measurement
    x-axis variable can be handled with -=1 if went left and +=1 if went right
    Create a dictionary with x-axis variable as key and value is a list with node value and level values.
    If x-axis variabke is not there add it,if there then check level and if level is lesser that the stored level then replace node value and level

    '''
    top_elements_dict = {}
    
    def traversal(root, x, y):
        if root:
            if x not in top_elements_dict:
                top_elements_dict[x] = [root, y]
            elif top_elements_dict[x][1] > y:
                top_elements_dict[x] = [root, y]
            
            # Visit left subtree
            traversal(root.left, x-1, y+1)
            # Visit right subtree
            traversal(root.right, x+1, y+1)
    
    traversal(root, 0, 0)
    for i in sorted(top_elements_dict):
        print(top_elements_dict[i][0], end = ' ')



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)