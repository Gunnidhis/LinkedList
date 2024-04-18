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
        print("none\n")

    def middle_of_linked_list(self):
        slow = fast = self.head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)

    def last_nth_node(self, n):
        slow = fast = self.head
        for i in range(n):
            fast = fast.next
        while fast != None:
            slow = slow.next
            fast = fast.next
        print(slow.data)

    def starting_of_loop(self):
        slow = fast = self.head
        CycleFound = False
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow.data == fast.data:
                CycleFound = True
                break
        if CycleFound == True:
            slow = self.head
            while slow.data != fast.data:
                slow = slow.next
                fast = fast.next
        print(slow.data)


if __name__ == "__main__":
    myList = LinkedList()
    myList.InsertionAtBeginning(3)
    myList.InsertionAtBeginning(2)
    myList.InsertionAtBeginning(1)
    myList.InsertionAtMiddle(2, 4)
    # myList.InsertionAtMiddle(7,4)
    # myList.middle_of_linked_list()
    myList.printList()
    myList.last_nth_node(3)
