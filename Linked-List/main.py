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
print(string_linked_list.head.next.next.next.value, end=" ")