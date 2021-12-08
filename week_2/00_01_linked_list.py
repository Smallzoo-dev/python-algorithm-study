class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = None
        if index == 0:
            return self.head
        while index > 0:
            cur = self.head
            cur = cur.next
            index -= 1
        return cur

    def add_node(self, index, data):
        cur = self.head
        insert_node = Node(data)
        if index == 0:
            self.head = insert_node
            insert_node.next = cur
        while index - 1 > 0:
            cur = cur.next
            index -= 1
        next_node = cur.next
        cur.next = insert_node
        insert_node.next = next_node

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
        node = self.get_node(index - 1)
        delete_node = node.next
        node.next = delete_node.next




linked_list = LinkedList(5)
linked_list.append(12)
linked_list.get_node(0) # -> 5를 들고 있는 노드를 반환해야 합니다!