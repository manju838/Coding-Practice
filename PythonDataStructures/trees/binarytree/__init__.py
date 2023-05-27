from dataclasses import dataclass # Useful when dealing with Databased classes
from typing import Any, Deque, Dict, Iterator, List, Optional, Tuple, Union # Adds type hints, for more info, go through DataClasses_Practice/Notes.txt 

__all__ = [ #list that includes the names of several objects, functions, and variables.
    "Node",
    "tree",
    "bst",
    "heap",
    "build",
    "build2",
    "get_index",
    "get_parent",
    "number_to_letters",
    "NodeValue",
    "NodeValueList",
]


from binarytree.exceptions import (
    NodeIndexError,
    NodeModifyError,
    NodeNotFoundError,
    NodeReferenceError,
    NodeTypeError,
    NodeValueError,
    TreeHeightError,
)

# Define several variables and constants related to binarytree module
_ATTR_LEFT = "left"
_ATTR_RIGHT = "right"
_ATTR_VALUE = "value"
_NODE_VAL_TYPES = (float, int, str) # Acceptable datatypes for node value

NodeValue = Any  # Union[float, int, str]
NodeValueList = Union[
    List[Optional[float]],
    List[Optional[int]],
    List[Optional[str]],
    List[float],
    List[int],
    List[str],
]

@dataclass # If this @dataclass is not used, a class needs to be written with init, functions/variables for all these and other dunder methods and must maintain uniformity, this does all that so that user can just overwrite the basic dunder methods 
class NodeProperties:
    height: int
    size: int
    is_max_heap: bool
    is_min_heap: bool
    is_perfect: bool
    is_strict: bool
    is_complete: bool
    leaf_count: int
    min_node_value: NodeValue
    max_node_value: NodeValue
    min_leaf_depth: int
    max_leaf_depth: int

class Node:
    """Represents a binary tree node.

    This class provides methods and properties for managing the current node,
    and the binary tree in which the node is the root.
    
    :param value: NodeValue (must be a float/int/str).
    :param left: Left child node (default: None).
    :param right: Right child node (default: None).
    """

    def __init__(
            self,
            value: NodeValue,
            left: Optional["Node"] = None,
            right: Optional["Node"] = None
            ) ->None:
        self.value = value,
        self.left = left,
        self.right = right
    
    def __repr__(self) -> str:
        """Return the string representation of the current node.
        """
        return "Node({})".format(self.val)
    
    def __str__(self) -> str:
        """
        Return the  binary tree in a string form in terminal.
            >>> from binarytree import Node
            >>>
            >>> root = Node(1)
            >>> root.left = Node(2)
            >>> root.right = Node(3)
            >>> root.left.right = Node(4)
            >>> 
            >>> print(root)
            <BLANKLINE>
              __1
             /   \\
            2     3
             \\
              4
            <BLANKLINE>

        .. note::
            To include level-order_ indexes in the output string, use
            :func:`binarytree.Node.pprint` instead.

        .. _level-order:
            https://en.wikipedia.org/wiki/Tree_traversal#Breadth-first_search

        """
        lines = _build_tree_string(self, 0, False, "-")[0]
        return "\n" + "\n".join((line.rstrip() for line in lines))

