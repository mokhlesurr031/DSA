class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def push_at_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is Node:
            self.head = new_node
            return

        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node

    def push_at_index(self, prev_node, new_data):
        if prev_node is Node:
            print("The given prev node must be in LL")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node


if __name__=='__main__':
    llist = LinkedList()
    f = Node(1)
    llist.head = f

    s = Node(2)
    t = Node(3)

    llist.head.next = s
    s.next = t
    llist.printList()
    print("----")
    llist.push_at_beginning(3)
    llist.printList()
    print("------------")
    llist.push_at_index(s.next, 12)
    llist.append(34)
    llist.printList()
