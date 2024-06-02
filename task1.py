class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sort(self):
        self.head = self.sort1(self.head)

    def sort1(self, node):
        # сортування злиттям
        if node.next is None:
            return node
        middle = self._get_middle(node)
        next_to_middle = middle.next
        middle.next = None
        left = self.sort1(node)
        right = self.sort1(next_to_middle)
        sorted_list = self.sorted_merge(left, right)
        return sorted_list

    def _get_middle(self, node):
        # знаходження середини списку
        slow = node
        fast = node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sorted_merge(self, a, b):
        result = None
        if a is None:
            return b
        if b is None:
            return a
        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result

    def merge_sorted_lists(self, llist):
        self.head = self.sorted_merge(self.head, llist.head)

    def display(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        return elements

# Приклад використання
llist1 = LinkedList()
llist1.append(8)
llist1.append(3)
llist1.append(5)
llist1.append(0)
llist1.sort()
print(llist1.display())

llist2 = LinkedList()
llist2.append(2)
llist2.append(4)
llist2.append(6)

llist1.merge_sorted_lists(llist2)
print(llist1.display())
