"""
Binary Search Tree implementation.
This class provides a blueprint for implementing a Binary Search Tree with
various operations like insert, delete, search, and traversal.
"""
from BinarySearch.Python.node import Node
import sys

class BinarySearchTreeV2:
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
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
            return

        current = self.root
        prev = None
        while current != None:
            prev = current
            if current.value > value:
                current = current.left
            else:
                current = current.right

        if value <= prev.value:
            prev.left = newNode
        else:
            prev.right = newNode


    
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

        if self.root == None:
            return False

        current = self.root

        while current != None:
            if value == current.value:
                return True
            if value < current.value:
                current = current.left
            else:
                current = current.right

        
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
        if self.root == None:
            return False

        if self.search(value) == False:
            return False

        current = self.root
        parent = None
        while current != None:
            if value == current.value:
                break

            parent = current

            if value < current.value:
                current = current.left
            else:
                current = current.right

        new_subtree = self._delete_node(current)
        if parent == None:
            self.root = new_subtree
            return True

        if parent.left == current:
            parent.left = new_subtree
        else:
            parent.right = new_subtree


        return True

    def _delete_node(self, node):
        # 1. no children
        if node.left == None and node.right == None:
            return None
        # 2. one child
        if node.left == None:
            return node.right
        if node.right == None:
            return node.left
        # 3. two children
        newNode = self._find_min_node(node.right)
        node.value = newNode.value
        node.right = self._delete_min_node(node.right)
        return node
        

    def _find_min_node(self, node) -> Node:
        while node.left != None:
            node = node.left
        return node

    def _delete_min_node(self, node) -> Node:
        if node.left == None:
            return node.right

        node.left = self._delete_min_node(node.left)
        return node
    
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
        if node == None:
            return
        
        self._in_order_traversal(node.left)
        print(node.value, end=", ")
        self._in_order_traversal(node.right)
    
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
        if node == None:
            return
        
        print(node.value, end=", ")
        self._pre_order_traversal(node.left)
        self._pre_order_traversal(node.right)
    
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
        if node == None:
            return
        
        self._post_order_traversal(node.left)
        self._post_order_traversal(node.right)
        print(node.value, end=", ")
    
    def find_min(self):
        """
        Find the minimum value in the Binary Search Tree.
        
        Returns:
            The minimum value, or sys.maxsize * -1 if the tree is empty
        """
        # TODO: Implement this method
        # The minimum value is the leftmost node in the tree
        if self.root == None:
            return sys.maxsize * -1  # Python's equivalent of Integer.MIN_VALUE

        current = self.root
        while current.left != None:
            current = current.left

        return current.value
    
    def find_max(self):
        """
        Find the maximum value in the Binary Search Tree.
        
        Returns:
            The maximum value, or sys.maxsize if the tree is empty
        """
        # TODO: Implement this method
        # The maximum value is the rightmost node in the tree
        if self.root == None:
            return sys.maxsize  # Python's equivalent of Integer.MAX_VALUE

        current = self.root
        while current.right != None:
            current = current.right
        return current.value
    
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
        if node == None:
            return -1
        
        return max(self._get_height(node.left), self._get_height(node.right)) + 1
    
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
