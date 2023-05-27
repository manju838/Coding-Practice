from pkg_resources import get_distribution
from typing import Any, Deque, Dict, Iterator, List, Optional, Tuple, Union

# Define several variables and constants related to tree module

_ATTR_LEFT = "left"
_ATTR_RIGHT = "right"
_ATTR_VALUE = "value"
_NODE_VAL_TYPES = (float, int, str)

NodeValue = Any  # Union[float, int, str]
NodeValueList = Union[
    List[Optional[float]],
    List[Optional[int]],
    List[Optional[str]],
    List[float],
    List[int],
    List[str],
]


class BinaryTreeNode:
    def __init__(
        self,
        value: NodeValue,
        left: Optional["BinaryTreeNode"] = None, 
        right: Optional["BinaryTreeNode"] = None
        ) -> None:
        self.value = value
        self.left = left
        self.right = right
    
    def print_binary_tree(self, root: Optional["BinaryTreeNode"], prefix: str = "", subtree_flag = False) -> None:
        
        if root is None:
            return
        if not subtree_flag:
            print(prefix + str(root.value))
        else:
            print(prefix + "|__" + str(root.value))  # Print current node with prefix


        self.print_binary_tree(root.left, prefix + "|   ", subtree_flag = True)  # Recursively print left subtree
        self.print_binary_tree(root.right, prefix + "|   ", subtree_flag = True)  # Recursively print right subtree



if __name__ == '__main__':
    root = BinaryTreeNode("root")

    l1 = BinaryTreeNode("root_1_l1") # Parent_level_name
    r1 = BinaryTreeNode("root_1_r1")
    root.left = l1
    root.right = r1

    l2 = BinaryTreeNode("l1_2_l2")
    r2 = BinaryTreeNode("l1_2_r2")
    l1.left = l2
    l1.right = r2

    l3 = BinaryTreeNode("r1_2_l3")
    r3 = BinaryTreeNode("r1_2_r3")
    r1.left = l3
    r1.right = r3

    root.print_binary_tree(root)
    pass