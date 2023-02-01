class TreeNode:
    '''
    A tree node class must have a data location, what are its children and what are its parents
    '''
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        '''
        This class just adds the child, it doesn't create a child
        '''
        child.parent = self # child is added to the self object and this self is the parent of the child object
        self.children.append(child)# Append the previously instantiated child to the list self.children
    
    def print_tree(self):
        '''
        ----> Iterative Version <----
        i.e print data, go through the entire children list and print it
        print(self.data)
        for child in self.children:
            print(child.data)
        '''
        '''
        ---> Recursive Version <---
        i.e Since tree is a recursive datastructure(each child of a tree is a tree, called subtree)
        '''
        spaces = ' ' * self.get_level() * 4
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children: # When at leaf node, self.children is empty, so specify that
            for child in self.children:
                child.print_tree() # Made a mistake here previously, if self.print_tree() is called then it keeps on printing Electronics until maximum recursion depth is reached
    
    def get_level(self):
        '''
        level is just the name of a pointer like next in a linked list. This simplifies this code to be counting elements of a linked list problem
        '''
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
        
    
def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()
    #return root

if __name__ == '__main__':
    build_product_tree()
    # root.print_tree()
    pass