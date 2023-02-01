class TreeNode:
    '''
    A tree is a recursive datastructure and so must have a data holder, track of children and pointer to parent
    '''
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
        # pass

    def print_tree(self, print_upto_level):
        if self.get_level() > print_upto_level:
            return
        spaces = ' ' * self.get_level() * 4
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + self.data)
        if self.children: # Since printing a recursive datastructure is recursive, the base case is during leaf node when self.children is empty or None
            for child in self.children:
                child.print_tree(print_upto_level)
                # pass


    def get_level(self):
        '''
        Level is checking from the leaf node to the root node
        '''
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
        # pass

def build_product_tree(upto_level):
    # Level 0
    root = TreeNode('Global')

    # Level 1
    india = TreeNode('India')
    usa = TreeNode('USA')
    root.add_child(india)
    root.add_child(usa)

    # Level 2
    gujarat = TreeNode('Gujarat')
    karnataka = TreeNode('Karnataka')
    india.add_child(gujarat)
    india.add_child(karnataka)
    new_jersey = TreeNode('New Jersey')
    california = TreeNode('California')
    usa.add_child(new_jersey)
    usa.add_child(california)

    # Level 3
    ahmedabad = TreeNode('Ahmedabad')
    baroda = TreeNode('Baroda')
    gujarat.add_child(ahmedabad)
    gujarat.add_child(baroda)
    bengaluru = TreeNode('Bengaluru')
    mysore = TreeNode('Mysore')
    karnataka.add_child(bengaluru)
    karnataka.add_child(mysore)
    princeton = TreeNode('Princeton')
    trenton = TreeNode('Trenton')
    new_jersey.add_child(princeton)
    new_jersey.add_child(trenton)
    san_francisco = TreeNode('San Francisco')
    mountain_view = TreeNode('Mountain View')
    palo_alto = TreeNode('Palo Alto')
    california.add_child(san_francisco)
    california.add_child(mountain_view)
    california.add_child(palo_alto)


    root.print_tree(upto_level)
    pass

if __name__ == '__main__':
    num = int(input(" Enter the level upto which you want to print the tree:"))
    build_product_tree(num)