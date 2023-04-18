
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None

    def __str__(self):
        return self.value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        curr = self.head
        while curr.next_node:
            curr = curr.next_node
        curr.next_node = new_node

    def reverse(self):
        temp = LinkedList()
        curr = self.head
        if curr.next_node:
            while curr:
                if temp.head:
                    new_node = Node(curr.__str__())
                    new_node.next_node = temp.head
                    temp.head = new_node
                else:
                    temp.head = Node(curr.__str__())

                curr = curr.next_node
        else:
            temp.add(curr)

        return temp


    def view(self):
        node = self.head
        if node is None:
            return "LinkedList is Empty"
        result = ""
        while node:
            result += f"{node.__str__()} "
            node = node.next_node
        return result



ll = LinkedList()
ll.add(5)
ll.add(22)
ll.add(33)
ll.add(44)
print(ll.view())
ll = ll.reverse()
print(ll.view())