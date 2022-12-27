'''
https://www.youtube.com/watch?v=JlMyYuY1aXU

Constructors are generally used for instantiating an object.
The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created. 
In Python the __init__() method is called the constructor and is always called when an object is created.

Constructors are either default constructor(doesn’t accept arguments, only argument is the reference to the instance(denoted by self)) or parameterised constructor(accepts programmer 
defined parameters in addition to instance reference(self))
'''

class directed_node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class bidirected_node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
        self.prev = None

class single_linked_list:
    def __init__(self):
        self.head = directed_node() # Head node is a placeholder that points to the first element of the linked list and thus is inaccessible.
    
    def append(self, data):
        new_node = directed_node(data)
        cur_ptr = self.head
        while(cur_ptr.next != None):
            cur_ptr = cur_ptr.next
        cur_ptr.next = new_node
    
    def length(self):
        cur_ptr = self.head
        total = 0
        while(cur_ptr.next != None):
            total +=1
            cur_ptr = cur_ptr.next
        return(total)
    
    def display(self):
        '''
        ele is a list of all data parts in a linked list but avoid this return if linked list is too big as it may lead to runtime issues
        '''
        ele = []
        cur_node = self.head
        while(cur_node.next != None):
            cur_node = cur_node.next # Before printing data part of a linked list, make sure to first traverse to the next node as the beginning started with a head node that doesn't have a data part
            print(cur_node.data)
            ele.append(cur_node.data)
            
        return(ele)
    
    def get(self, index):
        if index >= self.length():
            print("ERROR: Index out of bounds!")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if(cur_idx == index):
                return(cur_node.data)
            cur_idx +=1
        

if __name__ == '__main__':
    my_list = single_linked_list()
    my_list.display()
    
    my_list.append(8)
    my_list.append(7)
    my_list.display()