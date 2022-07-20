class _Node:
    def __init__(self, data, next=None, previous=None):
        self.previous = previous
        self.next = next
        self.data = data  # data is the value of the node

    def get_data(self):
        return self.data  # get the data of the node


class LinkedList:
    # LinkedList class
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addBeginningNode(self, data):
        newNode = _Node(data, next=self.head)
        self.head.previous = newNode
        self.head = newNode
        if self.tail is None:
            self.tail = self.head
        self.size += 1

    def addEndingNode(self, data):
        newNode = _Node(data, previous=self.tail)
        self.tail.next = newNode
        self.tail = newNode
        self.size += 1

    def add(self, data, index=-1):

        newNode = _Node(data)
        if self.size == 0:
            self.tail = self.head = newNode
        elif index == -1 or index == self.size:
            newNode.previous = self.tail
            self.tail.next = newNode
            self.tail = newNode
        elif index == 0:
            newNode.next = self.head
            self.head.previous = newNode
            self.head = newNode
        else:
            itr = self.head
            count = 0
            while count != index - 1:
                count += 1
                itr = itr.next
            newNode.next = itr.next
            newNode.previous = itr
            itr.next = newNode
        self.size += 1

    def printMyList(self):

        itr = self.head
        if not itr:
            raise Exception("Empty linked list")

        print(itr.get_data())
        while itr.next:
            print(itr.next.get_data())
            itr = itr.next

    def pop(self, idx=-1):
        if idx > self.size - 1:
            raise Exception("Index out of bounds")
        if idx == -1 or idx == self.size - 1:
            self.tail = self.tail.previous
            self.tail.next = None
            self.size -= 1
        elif idx == 0:
            self.head = self.head.next
            self.head.previous = None
            self.size -= 1
        else:
            count = 0
            itr = self.head
            while count < idx:
                itr = itr.next
                count += 1
            itr.previous.next = itr.next
            itr.next.previous = itr.previous
        self.size -= 1


if __name__ == "__main__":
    mylist = LinkedList()
    mylist.add(5)
    mylist.add(6)
    mylist.add(7)
    mylist.add(2, 1)
    mylist.add(1, 0)
    mylist.add(8, 2)
    mylist.add(8, 4)
    mylist.add(8, -1)
    # mylist.pop(5)
    mylist.printMyList()
