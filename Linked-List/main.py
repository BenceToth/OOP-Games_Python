from linked_list import LinkedList

my_linked_list = LinkedList()
print(my_linked_list.head)  # None

# 3 -> 9
my_linked_list.insert_node(9)
print(my_linked_list.head.value)  # 9
my_linked_list.insert_node(3)
print(my_linked_list.head.value)  # 3

# 1st: 9
# 2nd: 3 -> 9
# 3rd: 3 -> 6 -> 9
my_linked_list.insert_node(6)
print(((my_linked_list.head).next).value)  # value after head: 6

# 4th: 3 -> 6 -> 9 -> 15
my_linked_list.insert_node(15)
print(my_linked_list.head.next.next.next.value)  # 4th value: 15

# Testing with strings
string_linked_list = LinkedList()
string_linked_list.insert_node("Python")
string_linked_list.insert_node("World")
string_linked_list.insert_node("Hello")
string_linked_list.insert_node("Code")

# Code -> Hello -> Python -> World
print(string_linked_list.head.value, end=" ")
print(string_linked_list.head.next.value, end=" ")
print(string_linked_list.head.next.next.value, end=" ")
print(string_linked_list.head.next.next.next.value)

my_empty_linked_list = LinkedList()

# test print_nodes() method
my_linked_list.print_nodes()  # 3, 6, 9, 15

# test count_nodes() method
print(my_linked_list.count_nodes())  # 4
my_linked_list.insert_node(0)
print(my_linked_list.count_nodes())  # 5
print(my_empty_linked_list.count_nodes())  # 0

# test find_node() method
print(my_linked_list.find_node(3))  # True
print(my_linked_list.find_node(100))  # False
print(my_empty_linked_list.find_node(3))  # False

# test delete_node() method
## beginning of chain
my_linked_list.print_nodes()  # 0 3 6 9 15
print(my_linked_list.delete_node(0))  # True
my_linked_list.print_nodes()  # 3 6 9 15

my_empty_linked_list.print_nodes()  # Empty
print(my_empty_linked_list.delete_node(0))  # False
my_empty_linked_list.print_nodes()  # Empty

## middle of chain
my_linked_list.print_nodes()  # 3 6 9 15
print(my_linked_list.delete_node(9))  # True
my_linked_list.print_nodes()  # 3 6 15
print(my_linked_list.delete_node(100))  # False