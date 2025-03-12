"""
Node class for BFS implementation.
This class represents a node in a graph or tree structure.
"""

class Node:
    def __init__(self, value):
        """
        Constructor to create a new node.
        
        Args:
            value: The value to be stored in the node
        """
        self.value = value
        self.neighbors = []  # List of neighboring nodes
        self.visited = False  # Flag to track if node has been visited during traversal
    
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
    
    def get_neighbors(self):
        """
        Get the list of neighboring nodes.
        
        Returns:
            List of neighboring nodes
        """
        return self.neighbors
    
    def add_neighbor(self, neighbor):
        """
        Add a neighbor to this node.
        
        Args:
            neighbor: The node to be added as a neighbor
        """
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)
    
    def remove_neighbor(self, neighbor):
        """
        Remove a neighbor from this node.
        
        Args:
            neighbor: The node to be removed from neighbors
        """
        if neighbor in self.neighbors:
            self.neighbors.remove(neighbor)
    
    def is_visited(self):
        """
        Check if the node has been visited.
        
        Returns:
            True if the node has been visited, False otherwise
        """
        return self.visited
    
    def set_visited(self, visited):
        """
        Set the visited status of the node.
        
        Args:
            visited: Boolean indicating whether the node has been visited
        """
        self.visited = visited
    
    def reset_visited(self):
        """
        Reset the visited status to False.
        """
        self.visited = False
