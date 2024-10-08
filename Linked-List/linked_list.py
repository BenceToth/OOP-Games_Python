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
        else:
            previous = self.head
            runner = self.head.next
            
            # Insertion spot not found, Tail not reached
            while (runner is not None) \
              and (value > runner.value):
                    # moving right
                    previous = runner
                    runner = runner.next
            
            # update pointers
            new_node.next = runner
            previous.next = new_node
            
    def print_nodes(self):
        # if list is empty
        if self.head is None:
            print("Empty")
        else:
            runner = self.head
            # until Trail is reached (included)
            while runner is not None:
                print(runner.value, end=" ")
                # jump to next node
                runner = runner.next
            print()
            
    # print in reverse: wrapper method
    def print_reversed(self):
        self.print_reversed_recursive(self.head)
    
    # print in reverse: recursive method
    def print_reversed_recursive(self, node):
        if node is not None:
            self.print_reversed_recursive(node.next)
            print(node.value, end=" ")
          
    # Counting nodes: recursive implementation
    def count_nodes(self):
          return self.count_nodes_recursive(self.head)
          
    def count_nodes_recursive(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.count_nodes_recursive(node.next)
        
    # check if value in list
    def find_node(self, target_value):
        runner = self.head
        
        while runner is not None:
            if runner.value == target_value:
                return True
            runner = runner.next
        
        return False
    
    def delete_node(self, target_value):
        # empty list
        if self.head is None:
            return False
        # if target is the HEAD node
        elif self.head.value == target_value:
            # move HEAD to 2nd node
            self.head = self.head.next
            return True
        else:
            previous = self.head
            runner = self.head.next
            
            # move through nodes
            while (runner is not None) \
              and (target_value > runner.value):
                previous = runner
                runner = runner.next
                
            # target is found
            if (runner is not None) \
           and (runner.value == target_value):
               # update pointers
               previous.next = runner.next  # Bridge
               return True
            else:
                return False