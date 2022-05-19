#!/usr/bin/python3
"""Class Node"""


class Node:
    """Node of a singly linked list.
    Private instance attribute: data:
        - property def data(self)
        - property setter def data(self, value)
    Private instance attribute: next_node:
        - property def next_node(self)
        - property setter def next_node(self, value)
    Instantiation with data and next_node.
    """

    def __init__(self, data, next_node=None):
        """Initializes the data of the node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        "Data must be an integer"
        return self.__data

    @data.setter
    def data(self, value):
        if (type(value) != int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if (type(value) != Node) and (value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """"Singly linked list defines a single linked list
    Private instance attribute: head.
    Simple instantiation.
    Public instance method: def sorted_insert(self, value).
    """

    def __init__(self):
        """Initializes the linked list."""
        self.__head = None

    def __str__(self):
        """For the print statement in the main file."""
        my_str = ""
        node = self.__head
        while node:
            my_str += str(node.data)
            my_str += '\n'
            node = node.next_node
        return my_str[:-1]

    def sorted_insert(self, value):
        """Inserts a node in a sorted linked list."""
        new_node = Node(value)
        new_node.data = value
        new_node.next_node = None

        if (self.__head is None):
            self.__head = new_node
            return
        if (value < self.__head.data):
            new_node.next_node = self.__head
            self.__head = new_node
            return
        node = self.__head
        while node.next_node and node.next_node.data < value:
            node = node.next_node
        new_node.next_node = node.next_node
        node.next_node = new_node
