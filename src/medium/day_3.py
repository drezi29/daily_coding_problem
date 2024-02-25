'''
Given the root to a binary tree, implement serialize(root), 
which serializes the tree into a string, and deserialize(s), 
which deserializes the string back into the tree.
'''

from typing import Any, List


class Node:
    def __init__(self, parent, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return f"|Node {self.parent}, {self.left}, {self.right}|"

def serialize(root_node: Node) -> str:
    stack = []
    stack.append(root_node)
    elements_to_serialize = []

    while len(stack) > 0:
        node = stack.pop()
        if node is None:
            elements_to_serialize.append('-')
        else:
            elements_to_serialize.append(node.parent)
            stack.append(node.left)
            stack.append(node.right)

    return ','.join(elements_to_serialize)


def deserialize(serialized_tree: str) -> Node:
    elements_to_deserialize = serialized_tree.split(',')
    global offset 
    offset = 0
    return generate_node(elements_to_deserialize)

def generate_node(elements_to_deserialize: List[Any]):
    global offset
    if elements_to_deserialize[offset] == '-':
        return None
    
    parent = elements_to_deserialize[offset]
    offset += 1
    right = generate_node(elements_to_deserialize)
    offset += 1
    left = generate_node(elements_to_deserialize)
    return Node(parent, left, right)
