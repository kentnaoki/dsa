"""
Breadth-First Search (BFS) implementation.
This class provides a blueprint for implementing BFS on a graph.
"""
from collections import deque
from BFS.Python.node import Node

class BFSTemplate:
    def __init__(self):
        """
        Constructor to create a new BFS instance.
        """
        self.nodes = []  # List of all nodes in the graph
    
    def add_node(self, value):
        """
        Add a new node to the graph.
        
        Args:
            value: The value to be stored in the new node
            
        Returns:
            The newly created node
        """
        node = Node(value)
        self.nodes.append(node)
        return node
    
    def add_edge(self, node1, node2):
        """
        Add an edge between two nodes in the graph.
        
        Args:
            node1: First node
            node2: Second node
        """
        node1.add_neighbor(node2)
        node2.add_neighbor(node1)  # For undirected graph
    
    def get_nodes(self):
        """
        Get all nodes in the graph.
        
        Returns:
            List of all nodes
        """
        return self.nodes
    
    def clear(self):
        """
        Clear all nodes from the graph.
        """
        self.nodes.clear()
    
    def reset_visited(self):
        """
        Reset visited status of all nodes.
        """
        for node in self.nodes:
            node.reset_visited()
    
    def bfs_traversal(self, start_node):
        """
        Perform BFS traversal starting from the given node.
        
        Args:
            start_node: The node to start BFS from
            
        Returns:
            List of values in BFS order
        """
        # TODO: Implement this method
        # 1. Check if start_node is None, return empty list if it is
        # 2. Create a result list to store the traversal order
        # 3. Create a queue and add the start_node to it
        # 4. Mark the start_node as visited
        # 5. While the queue is not empty:
        #    a. Dequeue a node
        #    b. Add its value to the result list
        #    c. For each unvisited neighbor:
        #       i. Mark it as visited
        #       ii. Enqueue it
        # 6. Return the result list
        return []
    
    def find_path(self, start_node, end_node):
        """
        Find a path between start_node and end_node using BFS.
        
        Args:
            start_node: Starting node
            end_node: Target node
            
        Returns:
            List of nodes representing the path, or empty list if no path exists
        """
        # TODO: Implement this method
        # 1. Check if start_node or end_node is None, return empty list if either is
        # 2. Reset visited status of all nodes
        # 3. Create a queue and add a tuple of (start_node, [start_node]) to it
        #    (the second element is the path so far)
        # 4. Mark the start_node as visited
        # 5. While the queue is not empty:
        #    a. Dequeue a tuple (current_node, path)
        #    b. If current_node is the end_node, return the path (convert nodes to values)
        #    c. For each unvisited neighbor:
        #       i. Mark it as visited
        #       ii. Create a new path by appending the neighbor to the current path
        #       iii. Enqueue a tuple of (neighbor, new_path)
        # 6. Return an empty list if no path is found
        return []
    
    def find_level(self, start_node, target_value):
        """
        Find the level (distance) of a node with target_value from start_node.
        
        Args:
            start_node: Starting node
            target_value: Value to search for
            
        Returns:
            Level of the target node, or -1 if not found
        """
        # TODO: Implement this method
        # 1. Check if start_node is None, return -1 if it is
        # 2. Reset visited status of all nodes
        # 3. Create a queue and add a tuple of (start_node, 0) to it
        #    (the second element is the level)
        # 4. Mark the start_node as visited
        # 5. While the queue is not empty:
        #    a. Dequeue a tuple (current_node, level)
        #    b. If current_node's value is the target_value, return the level
        #    c. For each unvisited neighbor:
        #       i. Mark it as visited
        #       ii. Enqueue a tuple of (neighbor, level + 1)
        # 6. Return -1 if the target_value is not found
        return -1
    
    def count_connected_components(self):
        """
        Count the number of connected components in the graph.
        
        Returns:
            Number of connected components
        """
        # TODO: Implement this method
        # 1. Check if there are no nodes, return 0 if there aren't
        # 2. Reset visited status of all nodes
        # 3. Initialize a count to 0
        # 4. For each node in the graph:
        #    a. If the node is not visited:
        #       i. Perform BFS traversal starting from this node
        #          (this will mark all nodes in the component as visited)
        #       ii. Increment the count
        # 5. Return the count
        return 0
    
    def is_bipartite(self, start_node):
        """
        Check if the graph is bipartite (can be colored with two colors).
        
        Args:
            start_node: Starting node for the check
            
        Returns:
            True if the graph is bipartite, False otherwise
        """
        # TODO: Implement this method
        # 1. Check if start_node is None, return True if it is
        # 2. Reset visited status of all nodes
        # 3. Create a dictionary to store colors (True/False) for each node
        # 4. Assign a color (True) to the start_node
        # 5. Create a queue and add the start_node to it
        # 6. Mark the start_node as visited
        # 7. While the queue is not empty:
        #    a. Dequeue a node
        #    b. Get the color of the current node
        #    c. For each neighbor:
        #       i. If the neighbor is not colored:
        #          - Assign the opposite color to the neighbor
        #          - Mark it as visited
        #          - Enqueue it
        #       ii. If the neighbor is already colored with the same color as the current node:
        #           - Return False (not bipartite)
        # 8. Return True if all checks pass
        return True
