"""Tree Practice


=== Module description ===
This module contains sample tests for Tutorial 3.

"""
import unittest
from hypothesis import given, assume
from hypothesis.strategies import integers, lists, recursive, builds, just

from ex5 import Tree, to_tree


##############################################################################
# Helper functions
##############################################################################


def _tree_size(t):
    """Return the size of the given tree.

    @type t: Tree
    @rtype: int
    """
    if t.is_empty():
        return 0
    else:
        s = 1
        for subtree in t._subtrees:
            s += _tree_size(subtree)
        return s


def item():
    """Generate an integer between -10000 and 10000."""
    return integers(min_value=-10000, max_value=10000)


def single_root():
    """Generate a tree with a single node.

    The root value is an integer between -10000 and 10000.
    """
    return builds(Tree,
                  item(),
                  just([]))


def trees():
    """Generate a non-empty tree with integer items between -10000 and 10000."""
    return recursive(single_root(),
                     lambda children:
                         builds(Tree,
                                item(),
                                lists(children)))





##############################################################################
# Helper functions (Hypothesis custom strategies)
##############################################################################
class TreeEqTest(unittest.TestCase):
    @given(trees())
    def test_tree_equals_itself(self, tree):
        self.assertTrue(tree == tree)

    def test_empty(self):
        tree1 = Tree(1, [])
        tree_emp = Tree(None, [])
        self.assertFalse(None)
        self.assertFalse(tree_emp == tree1)
        self.assertFalse(tree1 == tree_emp)
		
    def test_empty1(self):
        tree_emp = Tree(None, [])
        tree_emp2 = Tree(None, [])
        self.assertTrue(tree_emp == tree_emp2)
        self.assertTrue(tree_emp2 == tree_emp)


class ToNestedListTest(unittest.TestCase):
    def test_one(self):
        t = Tree(1, [])
        self.assertEqual(t.to_nested_list(), [1])

    def test_list(self):
        t5 = Tree(5, [])
        t4 = Tree(4, [t5])
        t3 = Tree(3, [t4])
        t2 = Tree(2, [t3])
        t1 = Tree(1, [t2])

        self.assertEqual(t1.to_nested_list(), [1, [2, [3, [4, [5]]]]])


class ToTreeTest(unittest.TestCase):
    def test_one(self):
        t = to_tree([1])
        self.assertEqual(t._root, 1)
        self.assertEqual(t._subtrees, [])

    def test_line(self):
        t = to_tree([10, [2], [4], [5], [3]])
        self.assertEqual(t._root, 10)
        self.assertEqual(t._subtrees[0]._root, 2)
        self.assertEqual(t._subtrees[1]._root, 4)
        self.assertEqual(t._subtrees[2]._root, 5)
        self.assertEqual(t._subtrees[3]._root, 3)
        self.assertEqual(_tree_size(t), 5)





if __name__ == '__main__':
    unittest.main(exit=False)
