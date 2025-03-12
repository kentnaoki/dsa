"""
Node class for the Binary Search Tree.
Each node contains a value and references to left and right child nodes.
"""
class Node:
    def __init__(self, value):
        """
        Constructor to create a new node with the given value.
        
        Args:
            value: The value to be stored in the node
        """
        self.value = value
        self.left = None
        self.right = None
    
    def get_value(self):
        """
        Get the value stored in this node.
        
        Returns:
            The value stored in this node
        """
        return self.value
    
    def set_value(self, value):
        """
        Set the value for this node.
        
        Args:
            value: The new value to be stored
        """
        self.value = value
    
    def get_left(self):
        """
        Get the left child of this node.
        
        Returns:
            The left child node
        """
        return self.left
    
    def set_left(self, left):
        """
        Set the left child of this node.
        
        Args:
            left: The new left child node
        """
        self.left = left
    
    def get_right(self):
        """
        Get the right child of this node.
        
        Returns:
            The right child node
        """
        return self.right
    
    def set_right(self, right):
        """
        Set the right child of this node.
        
        Args:
            right: The new right child node
        """
        self.right = right
