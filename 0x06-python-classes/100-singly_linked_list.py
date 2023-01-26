#!/usr/bin/python3
"""class Node that defines a node of a sll"""


class Node:
    def __init__(self, data, next_node=None):
        """Initialize a new Node
        Args:
            data (int): The data of the new Node
            next_node (Node): The next node of the newNode
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node"""
        return (self.__next_node)

    def next_node(self, value):
        if value is not None and not isinstance(Value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """a class SinglyLinkedList that defines a singlly linked list"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """insert a new node into the correct sorted position in the list.
        It creates a new node object with the given value.
        If the head is None or the head's data is greater than the value,
        it updates the head and the next node of new node to be
        the current head."""
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        """Otherwise, it sets the current node to be the head of the list,
        and iterates trough the list, until it finds the
        correct position
        for the new node (the next node's data is greater than the value).
        When it finds the correct position,
        it sets the new node's next node
        to be the current node's next node,
        and sets the current node's next node to be the new node."""
        current = self.__head
        while (current.next_node and current.next_node.data < value):
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return ("\n".join(result))
