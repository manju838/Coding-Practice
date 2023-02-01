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

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    '''
    The height of the node is the distance between the node and the farthest leaf node
    So, height of a leaf node is 0, the level above it is 1 and so on.
    During iteration, the pointer goes beyond the leaf node(into None/NULL) so if we set the height value     as -1 there, tyhen it will be 0 at leaf node
    '''
    #If node doesn't exist, then return -1
    if root is None:
        return -1
    height_of_left_subtree = height(root.left)
    height_of_right_subtree = height(root.right)
    return(1+max(height_of_left_subtree, height_of_right_subtree))
    



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))
