"""
3) Write following functions body. 2 Nodes are passed as parameter. You need to find Least
Common Ancestor and print its value. Node structure are as following:
class Node{
value;
parent;
}
Ancestor Definition:
1) Any node falls under parent chain till root node.
2) A node is an ancestor of itself.
For example: if we consider Node 7 it’s ancestors will be 1, 3, and 7.
All nodes values are unique for this tree.
You function needs to find least common ancestor (closest common ancestor). For an example
for the tree image,
if 6 and 7 passed to lca it should return 3
if 3 and 7 passed to lca it should return 3
def lca(node1, node2):
# Write function body
You may write additional function.
Explain the Runtime and Memory requirements for your solution.
"""


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent


def lca(node1, node2):
    """
    In this method first we iterate from node1 to root of the tree increasing by node ancestors one by one
    and check lowest common ancestors and save the ancestors in a list and similar for node2. This method requires two
    traversals of the tree.

    Time Complexity Best Case: O(1) when both node value have same.
    Time Complexity Worst Case: As this method requires two traversals of the tree so time complexity will be
    O(2h)≈ O(h) where h is the height of the tree.

    Space Complexity: This method will store the ancestors of node in a list. So in the worst case scenario,
    node1 or node2 is the leaf of the tree at the highest depth. So node would have h ancestors.
    The Space Complexity will be O(h).
    """
    if node1.value == node2.value:
        print(node1.value)
        return

    node_list = [node1.value, node2.value]
    while True:
        if node1.parent:
            node1 = node1.parent
            if node1.value in node_list:
                print(node1.value)
                return
            node_list.append(node1.value)
        if node2.parent:
            node2 = node2.parent
            if node2.value in node_list:
                print(node2.value)
                return
            node_list.append(node2.value)


if __name__ == '__main__':
    node1 = Node(1, None)
    node2 = Node(2, node1)
    node3 = Node(3, node1)
    node4 = Node(4, node2)
    node5 = Node(5, node2)
    node6 = Node(6, node3)
    node7 = Node(7, node3)
    node8 = Node(8, node4)
    node9 = Node(9, node4)

    lca(node6, node7)
    lca(node3, node7)
    lca(node8, node7)