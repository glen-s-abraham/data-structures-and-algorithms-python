"""
Consider the case of building a bst from a sorted array say 1,2,3,4
the resulting structure would be an equalent of a singly linked list
with O(n) complexity.
Running time of bst depends on the H of the tree:we should keep the
tree balanced to get the best performance.
In any AVL tree the heights of two child sub tree differ by atmost 1.
Another solution to the problem is red-black trees.
AVL trees are faster than red-black trees cause they are more rigidly
balanced but need ore work.
OS relies heavily on these data structures.
spaces avg:O(n) worst:O(n)
insert avg:O(log n) worst:O(log n)
delete avg:O(log n) worst:O(log n)
search avg:O(log n) worst:O(log n)
height is the length of the longest path from it to a leaf.
height(h)=max(leftChild.height(),rightChild.height())+1.
AVL algorithm uses the heigths of nodes,we want the heights as small
as possible:we store the heights parameters->if it gets high we fix it.
AVL trees require the heights of left and right child of every node to
differ at most +1 or -1.
|height(leftSubtree)-height(rightSubtree)|<=1.
Insertion:1)a simple BST insertion according to the keys
2)fix the AVL property on each insertion from insertion upward.
Check all the violations of avl tree.
Four Types of unbalanced situations
LL:doubly left heavy situation.Make right rotation
LR:we have to make left and right rotation
RL:we have to make left and right rotation
RR:we have to make a left rotation
"""
import sys


class Node:
    """Data unit for holding single data and children"""
    def __init__(self, data, parentNode):
        self.data = data
        self.parentNode = parentNode
        self.rchild = None
        self.lchild = None
        self.balance = 0

    def insert(self, data, parentNode):
        """Insert a node into the tree"""
        if data < self.data:
            if self.lchild is None:
                self.lchild = Node(data, parentNode)
            else:
                self.lchild.insert(data, parentNode)
        else:
            if self.rchild is None:
                self.rchild = Node(data, parentNode)
            else:
                self.rchild.insert(data, parentNode)
        return parentNode

    def traverseInorder(self):
        if self.lchild is not None:
            self.lchild.traverseInorder()
        print(self.data)
        if self.rchild is not None:
            self.rchild.traverseInorder()

    def getMax(self):
        if self.rchild is not None:
            self.rchild.getMax()
        else:
            return self.rchild.getMax()

    def getMin(self):
        if self.lchild is not None:
            self.lchild.getMin()
        else:
            return self.lchild.getMin()


class BalancedTree:
    """AVL tree"""
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            parentNode = Node(data, None)
            self.root = parentNode
        else:
            parentNode = self.root.insert(data, self.root)
        self.rebalanceTree(parentNode)

    def rebalanceTree(self, parentNode):
        self.setBalance(parentNode)
        if parentNode.balance < -1:
            if self.height(parentNode.lchild.lchild) >= self.height(
             parentNode.lchild.rchild):
                parentNode = self.rotateRight(parentNode)
            else:
                parentNode = self.rotateLeftRight(parentNode)
        elif parentNode.balance > 1:
            if self.height(parentNode.rchild.rchild) >= self.height(
             parentNode.rchild.lchild):
                parentNode = self.rotateLeft(parentNode)
            else:
                parentNode = self.rotateRightLeft(parentNode)
        if parentNode.parentNode is not None:
            self.rebalanceTree(parentNode.parentNode)
        else:
            self.root = parentNode

    def rotateLeftRight(self, node):
        print("Rotation Left Right")
        node.lchild = self.rotateLeft(node.lchild)
        return self.rotateRight(node)

    def rotateRightLeft(self, node):
        print("Rotation Right Left")
        node.rchild = self.rotateRight(node.rchild)
        return self.rotateLeft(node)

    def rotateLeft(self, node):
        print("Rotation Left")
        temp = node.rchild
        temp.parentNode = node.parentNode
        node.rchild = temp.lchild
        if node.rchild is not None:
            node.rchild.parentNode = node
        temp.lchild = node
        node.parentNode = temp
        if temp.parentNode is not None:
            if temp.parentNode.rchild == node:
                temp.parentNode.rchild = temp
            else:
                temp.parentNode.lchild = temp
        self.setBalance(node)
        self.setBalance(temp)
        return temp

    def rotateRight(self, node):
        print("Rotation right")
        temp = node.parentNode
        temp.parentNode = node.parentNode
        node.lchild = temp.rchild
        if node.lchild is not None:
            node.lchild.parentNode = node
        temp.rchild = node
        node.parentNode = temp
        if temp.parentNode is not None:
            if temp.parentNode.rchild == node:
                temp.parentNode.rchild = temp
            else:
                temp.parentNode.lchild = temp
        self.setBalance(node)
        self.setBalance(temp)
        return temp

    def setBalance(self, node):
        node.balance = (self.height(node.rchild)
                        - self.height(node.lchild))

    def height(self, node):
        if node is None:
            return -1
        else:
            return 1 + max(self.height(node.lchild),
                           self.height(node.rchild))


if __name__ == '__main__':
    bst = BalancedTree()
    bst.insert(1)
    bst.insert(2)
    bst.insert(3)
    bst.insert(4)
    bst.insert(5)
