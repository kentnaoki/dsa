"""
Complete implementation of a Binary Search Tree.
This class provides a reference solution for the BinarySearchTree blueprint.
You can use this as a guide if you get stuck with your implementation.
"""
from BinarySearch.Python.node import Node
import sys

class BinarySearchTreeSolution:
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
        self.root = self._insert_rec(self.root, value)
    
    def _insert_rec(self, node, value):
        """
        Helper method for recursive insertion.
        
        Args:
            node: The current node
            value: The value to be inserted
            
        Returns:
            The updated node
        """
        # If the tree is empty, create a new node as root
        if node is None:
            return Node(value)
        
        # Otherwise, find the correct position to insert the new node
        if value < node.get_value():
            node.set_left(self._insert_rec(node.get_left(), value))
        elif value > node.get_value():
            node.set_right(self._insert_rec(node.get_right(), value))
        
        # Return the unchanged node pointer
        return node
    
    def search(self, value):
        """
        Search for a value in the Binary Search Tree.
        
        Args:
            value: The value to search for
            
        Returns:
            True if the value is found, False otherwise
        """
        return self._search_rec(self.root, value)
    
    def _search_rec(self, node, value):
        """
        Helper method for recursive search.
        
        Args:
            node: The current node
            value: The value to search for
            
        Returns:
            True if the value is found, False otherwise
        """
        # Base case: if the node is null, the value is not found
        if node is None:
            return False
        
        # If the value is found at the current node
        if node.get_value() == value:
            return True
        
        # If the value is less than the current node's value, search in the left subtree
        if value < node.get_value():
            return self._search_rec(node.get_left(), value)
        
        # If the value is greater than the current node's value, search in the right subtree
        return self._search_rec(node.get_right(), value)
    
    def delete(self, value):
        """
        Delete a value from the Binary Search Tree.
        
        Args:
            value: The value to be deleted
            
        Returns:
            True if the value was found and deleted, False otherwise
        """
        # Check if the value exists in the tree
        if not self.search(value):
            return False
        
        # Delete the value
        self.root = self._delete_rec(self.root, value)
        return True
    
    def _delete_rec(self, node, value):
        """
        Helper method for recursive deletion.
        
        Args:
            node: The current node
            value: The value to be deleted
            
        Returns:
            The updated node
        """
        # Base case: if the node is null, the value is not found
        if node is None:
            return None
        
        # Find the node to delete
        if value < node.get_value():
            node.set_left(self._delete_rec(node.get_left(), value))
        elif value > node.get_value():
            node.set_right(self._delete_rec(node.get_right(), value))
        else:
            # Node with the value to be deleted is found
            
            # Case 1: Node with no children (leaf node)
            if node.get_left() is None and node.get_right() is None:
                return None
            
            # Case 2: Node with one child
            if node.get_left() is None:
                return node.get_right()
            if node.get_right() is None:
                return node.get_left()
            
            # Case 3: Node with two children
            # Find the in-order successor (smallest value in the right subtree)
            node.set_value(self._find_min(node.get_right()))
            
            # Delete the in-order successor
            node.set_right(self._delete_rec(node.get_right(), node.get_value()))
        
        return node
    
    def in_order_traversal(self):
        """
        Perform an in-order traversal of the Binary Search Tree.
        In-order traversal visits the left subtree, then the root, then the right subtree.
        """
        self._in_order_traversal(self.root)
        print()  # Add a newline at the end
    
    def _in_order_traversal(self, node):
        """
        Helper method for in-order traversal.
        
        Args:
            node: The current node being visited
        """
        if node is None:
            return
        
        self._in_order_traversal(node.get_left())
        print(node.get_value(), end=" ")
        self._in_order_traversal(node.get_right())
    
    def pre_order_traversal(self):
        """
        Perform a pre-order traversal of the Binary Search Tree.
        Pre-order traversal visits the root, then the left subtree, then the right subtree.
        """
        self._pre_order_traversal(self.root)
        print()  # Add a newline at the end
    
    def _pre_order_traversal(self, node):
        """
        Helper method for pre-order traversal.
        
        Args:
            node: The current node being visited
        """
        if node is None:
            return
        
        print(node.get_value(), end=" ")
        self._pre_order_traversal(node.get_left())
        self._pre_order_traversal(node.get_right())
    
    def post_order_traversal(self):
        """
        Perform a post-order traversal of the Binary Search Tree.
        Post-order traversal visits the left subtree, then the right subtree, then the root.
        """
        self._post_order_traversal(self.root)
        print()  # Add a newline at the end
    
    def _post_order_traversal(self, node):
        """
        Helper method for post-order traversal.
        
        Args:
            node: The current node being visited
        """
        if node is None:
            return
        
        self._post_order_traversal(node.get_left())
        self._post_order_traversal(node.get_right())
        print(node.get_value(), end=" ")
    
    def find_min(self):
        """
        Find the minimum value in the Binary Search Tree.
        
        Returns:
            The minimum value, or sys.maxsize * -1 if the tree is empty
        """
        if self.root is None:
            return sys.maxsize * -1  # Python's equivalent of Integer.MIN_VALUE
        
        current = self.root
        while current.get_left() is not None:
            current = current.get_left()
        
        return current.get_value()
    
    def _find_min(self, node):
        """
        Find the minimum value in a subtree.
        
        Args:
            node: The root of the subtree
            
        Returns:
            The minimum value in the subtree
        """
        min_value = node.get_value()
        while node.get_left() is not None:
            min_value = node.get_left().get_value()
            node = node.get_left()
        return min_value
    
    def find_max(self):
        """
        Find the maximum value in the Binary Search Tree.
        
        Returns:
            The maximum value, or sys.maxsize if the tree is empty
        """
        if self.root is None:
            return sys.maxsize  # Python's equivalent of Integer.MAX_VALUE
        
        current = self.root
        while current.get_right() is not None:
            current = current.get_right()
        
        return current.get_value()
    
    def get_height(self):
        """
        Get the height of the Binary Search Tree.
        
        Returns:
            The height of the tree, or -1 if the tree is empty
        """
        return self._get_height(self.root)
    
    def _get_height(self, node):
        """
        Helper method to calculate the height of a subtree.
        
        Args:
            node: The root of the subtree
            
        Returns:
            The height of the subtree, or -1 if the subtree is empty
        """
        if node is None:
            return -1
        
        left_height = self._get_height(node.get_left())
        right_height = self._get_height(node.get_right())
        
        return 1 + max(left_height, right_height)
    
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
