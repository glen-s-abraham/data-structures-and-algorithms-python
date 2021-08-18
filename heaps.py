"""
It's a binary tree.In a max heap, the keys of parent nodes
are always greater than ore equal to those of the children
and the highest key is the root node.In a min heap,the keys
of parent node are less than or equal to those of the children
and the lowest key is the root node.It's balanced.We insert
every new item to the next available place.Applications:Dijikstras
algorithm,Prims algorithm.The heap is one maximaly efficient
implementation of an abstract data type called a priority queue.
It has nothing to do with the pool of memory from which dynamically
allocated memory is allocated.
Heap properties:complete->we construct it from left to right across
each row.The key of the paretn must be larger/smaller than it's
children's keys.
if parentNode=i then leftChild=2i+1 rightChild=2i+2
Heapsort:comparison-based sorting algorithm.use a heap datastructure
rather than a linear-time search to find the maximum.although somewhat
slower in practise on most machines than a well-implemented quicksort,
it has the advantage of a more favourable worst case O(n log n)reuntime.
Heapsort is an as in place algorithm,but it's not stable.
Binomial heap:similar to a biary heap but also supports quick merging of
two heaps.It is important as an implementation of the mergable heap abstract
datatype,which is a priority queue supprting merge operation.A binomial heap
is implemented as a collection of binary tress.Insertion O(log n) time
complexity can be reduced to O(1) constant time complexity with the help of
binomial heaps.
Fibonacci Heap:Faster than the classic binary heap.Dijikstra's algorithn and
prims spanning tree algorithm runs faster if they rely on fibonacci heap
instead of binary heaps.But very hard to implement efficiently so usually
not worth theeffort.Unlike binary heaps,it can hahve several children:number
of children are usually kept low.we can achieve O(1) insert operation instead
of O(log n).Every node has degree at most O(logn) and the size of a subtree
rooted in a node of degree k is at least Fk+2,where Fk is the kth fibonacci
number.
"""


class Heap:
    """Data stucture for holding data"""
    HEAP_SIZE = 10

    def __init__(self):
        self.heap = [0]*Heap.HEAP_SIZE
        self.currentPosition = -1

    def insert(self, item):
        if self.isFull():
            print("Heap is full")
            return
        self.currentPosition = self.currentPosition + 1
        self.heap[self.currentPosition] = item
        self.fixUp(self.currentPosition)

    def isFull(self):
        if self.currentPosition == Heap.HEAP_SIZE:
            return True
        return False

    def fixUp(self, index):
        parentIndex = int((index - 1) / 2)
        while (
            parentIndex >= 0 and self.heap[parentIndex] < self.heap[index]
        ):
            temp = self.heap[index]
            self.heap[index] = self.heap[parentIndex]
            self.heap[parentIndex] = temp
            parentIndex = int((index - 1) / 2)

    def getMax(self):
        result = self.heap[0]
        self.currentPosition = self.currentPosition - 1
        self.heap[0] = self.heap[self.currentPosition + 1]
        del self.heap[self.currentPosition + 1]
        self.fixDown(0, -1)
        return result

    def fixDown(self, index, upto):
        if upto < 0:
            upto = self.currentPosition
        while index <= upto:
            lchild = 2 * index + 1
            rchild = 2 * index + 2
            if lchild <= upto:
                childToSwap = None
                if rchild > upto:
                    childToSwap = lchild
                else:
                    if self.heap[lchild] > self.heap[rchild]:
                        childToSwap = lchild
                    else:
                        childToSwap = rchild
                if self.heap[index] < self.heap[childToSwap]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[childToSwap]
                    self.heap[childToSwap] = temp
                else:
                    break
                index = childToSwap
            else:
                break

    def heapSort(self):
        for i in range(0, self.currentPosition + 1):
            temp = self.heap[0]
            print(temp)
            self.heap[0] = self.heap[self.currentPosition - i]
            self.heap[self.currentPosition - i] = temp
            self.fixDown(0, self.currentPosition - i - 1)


if __name__ == '__main__':
    heap = Heap()
    heap.insert(12)
    heap.insert(-3)
    heap.insert(23)
    heap.insert(4)
    heap.heapSort()
