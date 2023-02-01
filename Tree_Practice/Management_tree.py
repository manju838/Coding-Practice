class TreeNode:

    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        '''
        This class just adds the child, it doesn't create a child
        '''
        child.parent = self # When self is the object used to append the child, then the parent of the child must be the object self itself 
        self.children.append(child) # Append the previously instantiated child to the list self.children
    
    def print_tree(self, property):

        if property == 'both':
            value = self.name + '(' + self.designation + ')'
        elif property == 'name':
            value = self.name
        else:
            value = self.designation 
        spaces = ' ' * self.get_level() * 4 # Define spacing proportional to level
        prefix = spaces + "|__" if self.parent else "" # If not root node(self.parent exists) add spacing and the lines else just print name as it is
        print(prefix + value)
        if self.children: # Base case of recursion is the leaf node where self.children is empty
            for child in self.children:
                child.print_tree(property) # Don't blunder self.print_tree()
    
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

def build_management_tree():
    # CTO Hierarchy
    infra_head = TreeNode("Vishwa","Infrastructure Head")
    infra_head.add_child(TreeNode("Dhaval","Cloud Manager"))
    infra_head.add_child(TreeNode("Abhijit", "App Manager"))

    cto = TreeNode("Chinmay", "CTO")
    cto.add_child(infra_head)
    cto.add_child(TreeNode("Aamir", "Application Head"))

    # HR hierarchy
    hr_head = TreeNode("Gels","HR Head")

    hr_head.add_child(TreeNode("Peter","Recruitment Manager"))
    hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

    ceo = TreeNode("Nilupul", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo

if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name")
    root_node.print_tree("designation")
    root_node.print_tree("both")





