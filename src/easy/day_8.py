'''
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.
For example, the following tree has 5 unival subtrees:
   0
  / \\
 1   0
    / \\
   1   0
  / \\
 1   1
'''

from dataclasses import dataclass

@dataclass
class Tree:
    parent : int
    left : int
    right : int

    def __init__(self, parent, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right

def count_unival_subtrees(tree : Tree):
    counter : int = 0

    if tree.left is None and tree.right is None:
        return 1
    if tree.left == tree.right:
        counter += 1

    for node in [tree.right, tree.left]:
        if node is not None:
             counter += count_unival_subtrees(node)

    return counter
