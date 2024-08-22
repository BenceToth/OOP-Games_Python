from node import Node


class LinkedList:

    def __init__(self):
        self.head = None
        
    def insert_node(self, value):
        new_node = Node(value)
        
        # if the LinkedList is empty
        if self.head is None:
            self.head = new_node
        # keeping ascending order
        elif value <= self.head.value:
            # change pointer
            new_node.next = self.head
            self.head = new_node