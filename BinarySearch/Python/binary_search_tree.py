"""
Binary Search Tree implementation.
This class provides a blueprint for implementing a Binary Search Tree with
various operations like insert, delete, search, and traversal.
"""
from BinarySearch.Python.node import Node
import sys

class BinarySearchTree:
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
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        prev = None
        while current is not None:
            if value <= current.get_value():
                prev = current
                current = current.get_left()
            else:
                prev = current
                current = current.get_right()
        
        if value <= prev.get_value():
            prev.set_left(new_node)
        else:
            prev.set_right(new_node)
    
    def search(self, value):
        """
        Search for a value in the Binary Search Tree.
        
        Args:
            value: The value to search for
            
        Returns:
            True if the value is found, False otherwise
        """
        return self._dfs(self.root, value)
    
    def _dfs(self, node, value):
        """
        Helper method for search using depth-first search.
        
        Args:
            node: The current node being visited
            value: The value to search for
            
        Returns:
            True if the value is found, False otherwise
        """
        if node is None:
            return False
        
        if node.get_value() == value:
            return True
        
        return self._dfs(node.get_left(), value) or self._dfs(node.get_right(), value)
    
    def delete(self, value):
        """
        Delete a value from the Binary Search Tree.
        
        Args:
            value: The value to be deleted
            
        Returns:
            True if the value was found and deleted, False otherwise
        """
        if not self.search(value):
            return False
        
        # Special case for root
        if self.root.get_value() == value:
            if self.root.get_left() is None and self.root.get_right() is None:
                self.root = None
            elif self.root.get_left() is None:
                self.root = self.root.get_right()
            elif self.root.get_right() is None:
                self.root = self.root.get_left()
            else:
                # Find the smallest node in the right subtree
                smallest = self._get_smallest_node(self.root.get_right())
                # Remove the smallest node from its original position
                self._remove_node(self.root.get_right(), smallest.get_value())
                # Replace the root with the smallest node
                smallest.set_left(self.root.get_left())
                smallest.set_right(self.root.get_right())
                self.root = smallest
            return True
        
        # Find the node to delete and its parent
        parent = None
        current = self.root
        is_left_child = False
        
        while current is not None and current.get_value() != value:
            parent = current
            if value < current.get_value():
                current = current.get_left()
                is_left_child = True
            else:
                current = current.get_right()
                is_left_child = False
        
        # Case 1: Node has no children
        if current.get_left() is None and current.get_right() is None:
            if is_left_child:
                parent.set_left(None)
            else:
                parent.set_right(None)
        
        # Case 2: Node has one child
        elif current.get_left() is None:
            if is_left_child:
                parent.set_left(current.get_right())
            else:
                parent.set_right(current.get_right())
        elif current.get_right() is None:
            if is_left_child:
                parent.set_left(current.get_left())
            else:
                parent.set_right(current.get_left())
        
        # Case 3: Node has two children
        else:
            # Find the smallest node in the right subtree
            smallest = self._get_smallest_node(current.get_right())
            # Remove the smallest node from its original position
            self._remove_node(current.get_right(), smallest.get_value())
            # Replace the current node with the smallest node
            smallest.set_left(current.get_left())
            smallest.set_right(current.get_right())
            if is_left_child:
                parent.set_left(smallest)
            else:
                parent.set_right(smallest)
        
        return True
    
    def _get_smallest_node(self, node):
        """
        Helper method to find the smallest node in a subtree.
        
        Args:
            node: The root of the subtree
            
        Returns:
            The node with the smallest value
        """
        current = node
        while current.get_left() is not None:
            current = current.get_left()
        return current
    
    def _remove_node(self, root, value):
        """
        Helper method to remove a node from a subtree.
        
        Args:
            root: The root of the subtree
            value: The value to be removed
        """
        if root is None:
            return None
        
        if root.get_value() == value:
            if root.get_left() is None:
                return root.get_right()
            elif root.get_right() is None:
                return root.get_left()
            else:
                smallest = self._get_smallest_node(root.get_right())
                root.set_value(smallest.get_value())
                root.set_right(self._remove_node(root.get_right(), smallest.get_value()))
                return root
        elif value < root.get_value():
            root.set_left(self._remove_node(root.get_left(), value))
        else:
            root.set_right(self._remove_node(root.get_right(), value))
        return root
    
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
            The minimum value, or sys.maxsize if the tree is empty
        """
        if self.root is None:
            return sys.maxsize * -1  # Python's equivalent of Integer.MIN_VALUE
        
        current = self.root
        while current.get_left() is not None:
            current = current.get_left()
        
        return current.get_value()
    
    def find_max(self):
        """
        Find the maximum value in the Binary Search Tree.
        
        Returns:
            The maximum value, or -sys.maxsize if the tree is empty
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
