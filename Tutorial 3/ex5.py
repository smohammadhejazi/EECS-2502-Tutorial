"""Tree Practice

=== Module description ===
This file contains starter code for Tutorial 3.
It is divided into three parts:
- Task 1, which contains one Tree method to implement.
- Task 2, which asks you to implement two operations that allow you
  to convert between trees and nested lists.
"""


class Tree:
    """A recursive tree data structure.

    === Private Attributes ===
    @type _root: object | None
        The item stored at the tree's root, or None if the tree is empty.
    @type _subtrees: list[Tree]
        A list of all subtrees of the tree.

    === Representation Invariants ===
    - If self._root is None then self._subtrees is empty.
      This setting of attributes represents an empty Tree.
    - self._subtrees does not contain any empty Trees.
    """
    def __init__(self, root, subtrees):
        """Initialize a new Tree with the given root
        value and subtrees.

        If <root> is None, the tree is empty.

        @type self: Tree
        @type root: object
        @type subtrees: list[Tree]
        @rtype: None
        """
        self._root = root
        self._subtrees = subtrees

    def get_root(self):
        return self._root
    
    def get_subtrees(self):
        return self._subtrees

    def is_empty(self):
        """Return True if this tree is empty.

        @type self: Tree
        @rtype: bool
        """
        return self._root is None

##############################################################################
# Task 1: Another tree method
##############################################################################
    # TODO: Implement this method!
    def __eq__(self, other):
        """Return whether <self> and <other> are equal.

        @type self: Tree
        @type other: Tree
        @rtype: bool
        """
        if self.get_root() != other.get_root():
            return False
        
        for i in range(len(self.get_subtrees())):
            if self.get_subtrees()[i] != other.get_subtrees()[i]:
                return False
        
        return True



##############################################################################
# Task 2: Trees and nested lists
##############################################################################
    # TODO: Implement this method!
    def to_nested_list(self):
        """Return the nested list representation of this tree.

        @type self: Tree
        @rtype: list
        """
        if self.is_empty():
            return []
        
        if len(self.get_subtrees()) == 0:
            return [self.get_root()]
        
        nested = []
        nested.append(self.get_root())
        for i in range(len(self.get_subtrees())):
            nested.append(self.get_subtrees()[i].to_nested_list())
        return nested




# TODO: Implement this function!
def to_tree(obj):
    """Return the Tree which <obj> represents.

    Precondition: <obj> is a valid nested list representation of a tree.
                  (In particular, <obj> is not an int.)

    You may not access Tree attributes directly. This function can be
    implemented only using the Tree constructor.

    @type obj: list
    @rtype: Tree
    """
    if obj is None:
        return Tree(None, [])
    
    if len(obj) == 1:
        return Tree(obj[0], [])
    
    subtrees = []
    for i in range(1, len(obj)):
        subtrees.append(to_tree(obj[i]))
    return(Tree(obj[0], subtrees))


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='pylintrc.txt')
