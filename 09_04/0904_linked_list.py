"""
연결 리스트
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def find(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    linked_list.display()  # 출력: 1 -> 2 -> 3 -> None

    print(linked_list.find(2))  # 출력: True
    print(linked_list.find(4))  # 출력: False
