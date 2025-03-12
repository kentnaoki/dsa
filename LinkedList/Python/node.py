"""
Node class for LinkedList implementation.
This class represents a node in a singly linked list.
"""

class Node:
    def __init__(self, value):
        """
        Constructor to create a new node.
        
        Args:
            value: The value to be stored in the node
        """
        self.value = value
        self.next = None
    
    def get_value(self):
        """
        Get the value stored in the node.
        
        Returns:
            The value stored in the node
        """
        return self.value
    
    def set_value(self, value):
        """
        Set the value stored in the node.
        
        Args:
            value: The new value to be stored
        """
        self.value = value
    
    def get_next(self):
        """
        Get the next node.
        
        Returns:
            The next node, or None if there is no next node
        """
        return self.next
    
    def set_next(self, next_node):
        """
        Set the next node.
        
        Args:
            next_node: The node to be set as the next node
        """
        self.next = next_node
