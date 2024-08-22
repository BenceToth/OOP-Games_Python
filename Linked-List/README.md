# Linked List Implementation in Python
This repository contains an implementation of a singly-linked list in Python. The main objective of this code is to provide a basic understanding of how linked lists work as a Data Structure, including common operations like insertion, deletion, and traversal.

## Project Structure
The project consists of three main Python files:

* `node.py`: Defines the `Node` class, representing an element in the linked list.
* `linked_list.py`: Contains the `LinkedList` class, which manages the linked list and provides methods for operations such as insertion, deletion, and searching.
* `main.py`: Demonstrates how to use the `LinkedList` class with various examples and serves as a test log.

## Classes
### Node Class (node.py)
Represents an individual node in the linked list.

**Attributes**:
* _value: Holds the value/data of the node.
* _next: A reference (pointer) to the next node in the list.

**Methods**:
* \__init__(value, next_node=None): Initializes a new node with a given value and an optional reference to the next node.
* @property value: Getter for the _value attribute.
* @value.setter: Setter for the _value attribute.
* @property next: Getter for the _next attribute.
* @next.setter: Setter for the _next attribute.
  
### LinkedList Class (linked_list.py)
Manages a collection of `Node` objects.

**Attributes**:
* head: A reference to the first node in the linked list (initially None).

**Methods**:
* \__init__(): Initializes an empty linked list.
* insert_node(value): Inserts a new node with the given value at the beginning of the linked list.
* print_nodes(): Prints the values of all nodes in the linked list.
* count_nodes(): Returns the number of nodes in the linked list.
* find_node(value): Searches for a node with the given value and returns True if found, False otherwise.
* delete_node(value): Deletes the first node with the specified value and returns True if successful, False otherwise.
* print_reversed(): Prints the values of the nodes in the linked list in reverse order.

## main.py
This is the main script that demonstrates the use of the `LinkedList` class by performing various operations such as inserting, deleting, and searching for nodes. It also shows how to work with both numeric and string data types in the linked list.

## Examples
Here are a few examples of operations you can perform:
* Insert Nodes:
  ```
  my_linked_list.insert_node(9)
  my_linked_list.insert_node(3)
  my_linked_list.insert_node(6)
  my_linked_list.insert_node(15)
  ```
* Print Nodes:
  ```
  my_linked_list.print_nodes()  # Output: 3, 6, 9, 15
  ```
* Count Nodes:
  ```
  print(my_linked_list.count_nodes())  # Output: 4
  ```
* Find a Node:
  ```
  print(my_linked_list.find_node(3))  # Output: True
  print(my_linked_list.find_node(100))  # Output: False
  ```
* Delete a Node:
  ```
  my_linked_list.delete_node(6)
  my_linked_list.print_nodes()  # Output: 3, 9, 15
  ```
* Print Nodes in Reverse:
  ```
  my_linked_list.print_reversed()  # Output: 15, 9, 3
  ```
