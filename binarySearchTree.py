"""
BST is used to implement lookup tables.
Keeps the key in sorted order so that lookup and other
operations can use binary search.
Each comparison allows the operations to skip over half
the tree.
Insertion:if the key is not equal to that of the root,
we search the left or right subtrees recursively.
Deletion:soft delete->do not actually remove the item
just mark it as deleted
deleting node with no child is easy:set it to null
Deleting node with one child:remove th node and replace
it with child.
Deleting node with two children:call the node to be
deleted i.Do not delete i directly.Instead, choose either
its in-order successor node or its in-order predecessor
node , j.Copy value of j to i then recursively call delete
on j until reaching one of the first two cases.
In-order traversal of a tree:gives the numerical order(ascending)
Space: Avg-O(n) Worst-O(n)
Insert: Avg-O(log n) Worst-O(n)
Delete: Avg-O(log n) Worst-O(n)
Search: Avg-O(log n) Worst-O(n)
Height,h:the length of the path from the root to the
deepest node in the tree.
we should keep the h at a minimum which is log n.
if the tree is unbalanced:the h=log n relation
is no more valid and the operation's running time is no more
logarithmic.
Inorder (Left, Root, Right)
Preorder (Root, Left, Right)
Postorder (Left, Right, Root)
predecessor node:the previous node in the in order traversal.
successor node:next node in the in-order traveral.
"""


class Node:
    """Data unit fot the tree"""
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        """Insert an element in the tree"""
        if data < self.data:
            if self.lchild is None:
                self.lchild = Node(data)
            else:
                self.lchild.insert(data)
        else:
            if self.rchild is None:
                self.rchild = Node(data)
            else:
                self.rchild.insert(data)

    def delete(self, data, parentNode):
        """Removes an element from the tree"""
        if data < self.data:
            if self.lchild is not None:
                self.lchild.delete(data, self)
        if data > self.data:
            if self.rchild is not None:
                self.rchild.delete(data, self)
        if data == self.data:
            if self.lchild is not None \
             and self.rchild is not None:
                self.data = self.rchild.getMin()
                self.rchild.delete(self.data, self)
            elif parentNode.lchild == self:
                if self.lchild is not None:
                    tempNode = self.lchild
                else:
                    tempNode = self.rchild
                parentNode.lchild = tempNode
            elif parentNode.rchild == self:
                if self.lchild is not None:
                    tempNode = self.lchild
                else:
                    tempNode = self.rchild
                parentNode.rchild = tempNode

    def getMin(self):
        """Return the minimum element"""
        if self.lchild is None:
            return self.data
        return self.lchild.getMin()

    def getMax(self):
        """Return the minimum element"""
        if self.rchild is None:
            return self.data
        return self.rchild.getMax()

    def inOrder(self):
        """
        Recursively call left subtree,
        Print root,
        Recursively call right subtree
        """
        if self.lchild is not None:
            self.lchild.inOrder()
        print(f'{self.data} ')
        if self.rchild is not None:
            self.rchild.inOrder()


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.insert(data)

    def remove(self, data):
        if self.root is not None:
            if self.root.data == data:
                temp = Node(None)
                temp.lchild = self.root
                self.root.delete(data, temp)
            else:
                self.root.delete(data, None)

    def getMax(self):
        if self.root is not None:
            return self.root.getMax()

    def getMin(self):
        if self.root is not None:
            return self.root.getMin()

    def traverseInOrder(self):
        if self.root is not None:
            self.root.inOrder()


if __name__ == '__main__':
    bst = BST()
    bst.insert(12)
    bst.insert(10)
    bst.insert(-2)
    bst.insert(1)
    bst.traverseInOrder()
    bst.remove(10)
    bst.traverseInOrder()
    print(bst.getMax())
    print(bst.getMin())
