"""
Binary Search Tree implementation.
This class provides a blueprint for implementing a Binary Search Tree with
various operations like insert, delete, search, and traversal.
"""
from BinarySearch.Python.node import Node
import sys

class BinarySearchTreeTemplate:
    def __init__(self):
        """
        Constructor to create an empty Binary Search Tree.
        """
        self.root = None
    
    def get_root(self):
        """
        Get the root node of the tree.
        
        Returns:
            The root node
        """
        return self.root
    
    def insert(self, value):
        """
        Insert a new value into the Binary Search Tree.
        
        Args:
            value: The value to be inserted
        """
        # TODO: Implement this method
        # If the tree is empty, create a new node as root
        # Otherwise, find the correct position to insert the new node
        pass
    
    def search(self, value):
        """
        Search for a value in the Binary Search Tree.
        
        Args:
            value: The value to search for
            
        Returns:
            True if the value is found, False otherwise
        """
        # TODO: Implement this method
        # Start from the root and traverse the tree
        # Return True if the value is found, False otherwise
        return False
    
    def delete(self, value):
        """
        Delete a value from the Binary Search Tree.
        
        Args:
            value: The value to be deleted
            
        Returns:
            True if the value was found and deleted, False otherwise
        """
        # TODO: Implement this method
        # Find the node to delete
        # Handle different cases: node with no children, one child, or two children
        # Return True if the value was found and deleted, False otherwise
        return False
    
    def in_order_traversal(self):
        """
        Perform an in-order traversal of the Binary Search Tree.
        In-order traversal visits the left subtree, then the root, then the right subtree.
        """
        # TODO: Implement this method
        # Use a helper method to perform the traversal recursively
        self._in_order_traversal(self.root)
    
    def _in_order_traversal(self, node):
        """
        Helper method for in-order traversal.
        
        Args:
            node: The current node being visited
        """
        # TODO: Implement this method
        # If the node is None, return
        # Otherwise, traverse left subtree, visit the node, traverse right subtree
        pass
    
    def pre_order_traversal(self):
        """
        Perform a pre-order traversal of the Binary Search Tree.
        Pre-order traversal visits the root, then the left subtree, then the right subtree.
        """
        # TODO: Implement this method
        # Use a helper method to perform the traversal recursively
        self._pre_order_traversal(self.root)
    
    def _pre_order_traversal(self, node):
        """
        Helper method for pre-order traversal.
        
        Args:
            node: The current node being visited
        """
        # TODO: Implement this method
        # If the node is None, return
        # Otherwise, visit the node, traverse left subtree, traverse right subtree
        pass
    
    def post_order_traversal(self):
        """
        Perform a post-order traversal of the Binary Search Tree.
        Post-order traversal visits the left subtree, then the right subtree, then the root.
        """
        # TODO: Implement this method
        # Use a helper method to perform the traversal recursively
        self._post_order_traversal(self.root)
    
    def _post_order_traversal(self, node):
        """
        Helper method for post-order traversal.
        
        Args:
            node: The current node being visited
        """
        # TODO: Implement this method
        # If the node is None, return
        # Otherwise, traverse left subtree, traverse right subtree, visit the node
        pass
    
    def find_min(self):
        """
        Find the minimum value in the Binary Search Tree.
        
        Returns:
            The minimum value, or sys.maxsize * -1 if the tree is empty
        """
        # TODO: Implement this method
        # The minimum value is the leftmost node in the tree
        return sys.maxsize * -1  # Python's equivalent of Integer.MIN_VALUE
    
    def find_max(self):
        """
        Find the maximum value in the Binary Search Tree.
        
        Returns:
            The maximum value, or sys.maxsize if the tree is empty
        """
        # TODO: Implement this method
        # The maximum value is the rightmost node in the tree
        return sys.maxsize  # Python's equivalent of Integer.MAX_VALUE
    
    def get_height(self):
        """
        Get the height of the Binary Search Tree.
        
        Returns:
            The height of the tree, or -1 if the tree is empty
        """
        # TODO: Implement this method
        # Use a helper method to calculate the height recursively
        return self._get_height(self.root)
    
    def _get_height(self, node):
        """
        Helper method to calculate the height of a subtree.
        
        Args:
            node: The root of the subtree
            
        Returns:
            The height of the subtree, or -1 if the subtree is empty
        """
        # TODO: Implement this method
        # If the node is None, return -1
        # Otherwise, return 1 + the maximum of the heights of the left and right subtrees
        return -1
    
    def is_empty(self):
        """
        Check if the Binary Search Tree is empty.
        
        Returns:
            True if the tree is empty, False otherwise
        """
        return self.root is None
    
    def clear(self):
        """
        Clear the Binary Search Tree.
        """
        self.root = None
