class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def InsertionAtBeginning(self, key):
        new_node = node(key)
        new_node.next = self.head
        self.head = new_node

    def InsertionAtMiddle(self, nodeAfter, key):

        h = self.head

        if h == None:
            print("Not Possible : empty list")
            return
        else:
            while h.data != nodeAfter:
                h = h.next
                if h == None:
                    print("NodeAfter dones't exist")
                    return
            new_node = node(key)
            new_node.next = h.next
            h.next = new_node

    def InsertionAtEnd(self, key):

        h = self.head

        if h == None:
            new_node = node(key)
            self.head = new_node
        else:
            while h.next != None:
                h = h.next
            new_node = node(key)
            h.next = new_node

    def printList(self):
        h = self.head
        while h != None:
            print(h.data, end="->")
            h = h.next
        print("none")

    def reverseList(self):
        # ratta maaro  sequence :prevP currP nextP
        prevP = nextP = None
        currP = self.head
        while currP != None:
            nextP = currP.next
            currP.next = prevP
            prevP = currP
            currP = nextP
        self.head = prevP
        return self.head


if __name__ == "__main__":
    myList = LinkedList()
    myList.InsertionAtBeginning(3)
    myList.InsertionAtBeginning(2)
    myList.InsertionAtBeginning(1)
    myList.InsertionAtMiddle(2, 4)
    myList.InsertionAtMiddle(7, 4)
    myList.reverseList()
    myList.printList()
