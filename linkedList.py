"""
Each node is composed of data and a reference to the next node
Can be used to implement several other comon data types:stacks,queues
Indexing:O(n)
Insert At begining:O(1)
Insert at end:O(n)
Delete at begining:O(1)
Delete at end:O(n)
Waste space:O(n)
Use linked list if you want to insert/remove elements at begining
,size changes frequently,no random access
Advantages:Dynamic datastructures,memory allocation in runtime,
store items with diff sizes,easier to grow organically.
Disadvantages:waste memory because of references,
nodes need to be read in order,difficulty in reverse traversing
"""


class Node:
    """Data Storage structure for each Node"""
    def __init__(self, data):
        self.data = data
        self.next = None

    def remove(self, data, previousNode):
        """Removes an element from the list"""
        if self.data == data:
            previousNode.next = self.next
            del self.data
            del self.next
        else:
            if self.next is not None:
                self.next.remove(data, self)


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def inserAtStart(self, data):
        """Insert an element at the begining of the List"""
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def insertAtEnd(self, data):
        """Insert an element at the end of the list"""
        node = Node(data)
        if self.head is None:
            self.inserAtStart(data)
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = node
        self.length += 1

    def removeData(self, data):
        """Removes an element from the list"""
        if self.head is not None:
            if self.head.data == data:
                self.head = self.head.next
            else:
                self.head.remove(data, self.head)
        self.length -= 1

    def traverseList(self):
        """Traverse the list"""
        temp = self.head
        while temp is not None:
            print('{} '.format(temp.data))
            temp = temp.next

    def length(self):
        """Return the size of the list"""
        return self.length


if __name__ == '__main__':
    linkedList = LinkedList()
    linkedList.insertAtEnd(1)
    linkedList.inserAtStart(2)
    linkedList.insertAtEnd(3)
    linkedList.insertAtEnd(4)
    linkedList.traverseList()
    print()
    linkedList.removeData(3)
    linkedList.traverseList()
    print()
    linkedList.removeData(2)
    linkedList.traverseList()
