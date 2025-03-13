"""
LinkedList implementation.
This class provides a blueprint for implementing a singly linked list with
various operations like insert, delete, search, and traversal.
"""
from node import Node
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
        # TODO: Implement this method
        # Create a new node with the given value
        # Set the new node's next to the current head
        # Update the head to the new node
        # Increment the size
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
    
    def insert_at_end(self, value):
        """
        Insert a new value at the end of the list.
        
        Args:
            value: The value to be inserted
        """
        # TODO: Implement this method
        # Create a new node with the given value
        # If the list is empty, set the head to the new node
        # Otherwise, traverse to the end of the list and set the last node's next to the new node
        # Increment the size
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.size += 1
            return

        current = self.head
        while current.next != None:
            current = current.next

        current.next = newNode
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
        # TODO: Implement this method
        # Check if the position is valid (0 <= position <= size)
        # If position is 0, call insert_at_beginning
        # If position is size, call insert_at_end
        # Otherwise, traverse to the node at position-1 and insert the new node after it
        # Increment the size
        # Return True if the insertion was successful, False otherwise
        if position < 0 or position > self.size:
            return False
        if position == 0:
            self.insert_at_beginning(value)
            return True

        if position == self.size:
            self.insert_at_end(value)
            return True

        position_counter = 0
        newNode = Node(value)
        current = self.head
        prev = None
        while current != None:
            if position_counter == position:
                newNode.next = current
                prev.next = newNode
                self.size += 1
                return True
            prev = current
            current = current.next
            position_counter += 1

        return False

    def delete(self, value):
        """
        Delete the first occurrence of the specified value from the list.
        
        Args:
            value: The value to be deleted
            
        Returns:
            True if the value was found and deleted, False otherwise
        """
        # TODO: Implement this method
        # If the list is empty, return False
        # If the head node has the value, update the head to the next node
        # Otherwise, traverse the list to find the node with the value and remove it
        # Decrement the size if a node was deleted
        # Return True if the value was found and deleted, False otherwise
        if self.head == None:
            return False
        
        current = self.head
        prev = None

        while current != None:
            if current.value == value:
                if prev == None:
                    self.head = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return True
            prev = current
            current = current.next
        return False
    
    def delete_at_position(self, position):
        """
        Delete the node at the specified position in the list.
        
        Args:
            position: The position of the node to be deleted (0-based index)
            
        Returns:
            True if the deletion was successful, False otherwise
        """
        # TODO: Implement this method
        # Check if the position is valid (0 <= position < size)
        # If position is 0, update the head to the next node
        # Otherwise, traverse to the node at position-1 and update its next pointer
        # Decrement the size
        # Return True if the deletion was successful, False otherwise
        if position < 0 or position >= self.size:
            return False


            
        current = self.head
        position_counter = 0
        prev = None

        while current != None:
            if position_counter == position:
                if prev == None:
                    self.head = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return True
            prev = current
            current = current.next
            position_counter += 1
        return False
    
    def search(self, value):
        """
        Search for a value in the list.
        
        Args:
            value: The value to search for
            
        Returns:
            True if the value is found, False otherwise
        """
        # TODO: Implement this method
        # Traverse the list and check if any node has the specified value
        # Return True if the value is found, False otherwise
        if self.head == None:
            return False

        current = self.head

        while current != None:
            if current.value == value:
                return True
            current = current.next

        return False
    
    def get_value_at_position(self, position):
        """
        Get the value at the specified position in the list.
        
        Args:
            position: The position of the node (0-based index)
            
        Returns:
            The value at the specified position, or sys.maxsize * -1 if the position is invalid
        """
        # TODO: Implement this method
        # Check if the position is valid (0 <= position < size)
        # Traverse to the node at the specified position and return its value
        # Return sys.maxsize * -1 if the position is invalid
        if position < 0 or position >= self.size:
            return sys.maxsize * -1  # Python's equivalent of Integer.MIN_VALUE

        position_counter = 0
        current = self.head

        while current != None:
            if position == position_counter:
                return current.value
            current = current.next
            position_counter += 1

        return sys.maxsize * -1
    
    def reverse(self):
        """
        Reverse the list.
        """
        # TODO: Implement this method
        # Reverse the list by changing the next pointers of each node
        prev = None
        current = self.head

        while current != None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def has_cycle(self):
        """
        Check if the list has a cycle.
        
        Returns:
            True if the list has a cycle, False otherwise
        """
        # TODO: Implement this method
        # Use Floyd's Cycle-Finding Algorithm (Tortoise and Hare)
        # Return True if a cycle is detected, False otherwise
        visited = [];

        if self.head == None:
            return False

        current = self.head
        while current != None:
            if current in visited:
                return True
            visited.append(current)
            current = current.next
        return False
    
    def find_middle(self):
        """
        Find the middle node of the list.
        
        Returns:
            The middle node, or None if the list is empty
        """
        # TODO: Implement this method
        # Use the slow and fast pointer technique to find the middle node
        # Return the middle node, or None if the list is empty
        #
        if self.head == None:
            return None

        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
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
