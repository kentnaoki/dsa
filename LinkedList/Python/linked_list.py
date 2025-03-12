"""
LinkedList implementation.
This class provides a blueprint for implementing a singly linked list with
various operations like insert, delete, search, and traversal.
"""
from LinkedList.Python.node import Node
import sys

class LinkedList:
    def __init__(self):
        """
        Constructor to create an empty LinkedList.
        """
        self.head = None
        self.size = 0
    
    def get_head(self):
        """
        Get the head node of the list.
        
        Returns:
            The head node
        """
        return self.head
    
    def get_size(self):
        """
        Get the size of the list.
        
        Returns:
            The number of nodes in the list
        """
        return self.size
    
    def is_empty(self):
        """
        Check if the list is empty.
        
        Returns:
            True if the list is empty, False otherwise
        """
        return self.head is None
    
    def insert_at_beginning(self, value):
        """
        Insert a new value at the beginning of the list.
        
        Args:
            value: The value to be inserted
        """
        new_node = Node(value)
        new_node.set_next(self.head)
        self.head = new_node
        self.size += 1
    
    def insert_at_end(self, value):
        """
        Insert a new value at the end of the list.
        
        Args:
            value: The value to be inserted
        """
        new_node = Node(value)
        
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)
        
        self.size += 1
    
    def insert_at_position(self, value, position):
        """
        Insert a new value at the specified position in the list.
        
        Args:
            value: The value to be inserted
            position: The position at which to insert the value (0-based index)
            
        Returns:
            True if the insertion was successful, False otherwise
        """
        if position < 0 or position > self.size:
            return False
        
        if position == 0:
            self.insert_at_beginning(value)
            return True
        
        if position == self.size:
            self.insert_at_end(value)
            return True
        
        new_node = Node(value)
        current = self.head
        for i in range(position - 1):
            current = current.get_next()
        
        new_node.set_next(current.get_next())
        current.set_next(new_node)
        self.size += 1
        return True
    
    def delete(self, value):
        """
        Delete the first occurrence of the specified value from the list.
        
        Args:
            value: The value to be deleted
            
        Returns:
            True if the value was found and deleted, False otherwise
        """
        if self.is_empty():
            return False
        
        if self.head.get_value() == value:
            self.head = self.head.get_next()
            self.size -= 1
            return True
        
        current = self.head
        while current.get_next() is not None and current.get_next().get_value() != value:
            current = current.get_next()
        
        if current.get_next() is None:
            return False
        
        current.set_next(current.get_next().get_next())
        self.size -= 1
        return True
    
    def delete_at_position(self, position):
        """
        Delete the node at the specified position in the list.
        
        Args:
            position: The position of the node to be deleted (0-based index)
            
        Returns:
            True if the deletion was successful, False otherwise
        """
        if position < 0 or position >= self.size:
            return False
        
        if position == 0:
            self.head = self.head.get_next()
            self.size -= 1
            return True
        
        current = self.head
        for i in range(position - 1):
            current = current.get_next()
        
        current.set_next(current.get_next().get_next())
        self.size -= 1
        return True
    
    def search(self, value):
        """
        Search for a value in the list.
        
        Args:
            value: The value to search for
            
        Returns:
            True if the value is found, False otherwise
        """
        current = self.head
        while current is not None:
            if current.get_value() == value:
                return True
            current = current.get_next()
        
        return False
    
    def get_value_at_position(self, position):
        """
        Get the value at the specified position in the list.
        
        Args:
            position: The position of the node (0-based index)
            
        Returns:
            The value at the specified position, or sys.maxsize * -1 if the position is invalid
        """
        if position < 0 or position >= self.size:
            return sys.maxsize * -1  # Python's equivalent of Integer.MIN_VALUE
        
        current = self.head
        for i in range(position):
            current = current.get_next()
        
        return current.get_value()
    
    def reverse(self):
        """
        Reverse the list.
        """
        if self.is_empty() or self.size == 1:
            return
        
        prev = None
        current = self.head
        next_node = None
        
        while current is not None:
            next_node = current.get_next()
            current.set_next(prev)
            prev = current
            current = next_node
        
        self.head = prev
    
    def has_cycle(self):
        """
        Check if the list has a cycle.
        
        Returns:
            True if the list has a cycle, False otherwise
        """
        if self.is_empty() or self.size == 1:
            return False
        
        slow = self.head
        fast = self.head
        
        while fast is not None and fast.get_next() is not None:
            slow = slow.get_next()
            fast = fast.get_next().get_next()
            
            if slow == fast:
                return True
        
        return False
    
    def find_middle(self):
        """
        Find the middle node of the list.
        
        Returns:
            The middle node, or None if the list is empty
        """
        if self.is_empty():
            return None
        
        slow = self.head
        fast = self.head
        
        while fast is not None and fast.get_next() is not None:
            slow = slow.get_next()
            fast = fast.get_next().get_next()
        
        return slow
    
    def print_list(self):
        """
        Print the list.
        """
        current = self.head
        print("List:", end=" ")
        while current is not None:
            print(current.get_value(), end=" ")
            current = current.get_next()
        print()
