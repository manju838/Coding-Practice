""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    '''
    Using Recursion
    '''
    def check(root, min_value, max_value):
        # Empty node is a valid BST
        if root is None:
            return True
        # If the node value fails to come
        if root.data <= min_value or root.data >= max_value:
            return False
        # Once the check if completed at node, make sure that both left and right subtrees are valid BSTs
        return check(root.left, min_value, root.data) and check(root.right, root.data, max_value)
    # Return the output as function
    return check(root,0,10000)

                