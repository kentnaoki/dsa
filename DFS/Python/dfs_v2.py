"""
Depth-First Search (DFS) implementation.
This class provides a blueprint for implementing DFS on a graph.
"""
from node import Node
from collections import deque

class DFSV2:
    def __init__(self):
        """
        Constructor to create a new DFS instance.
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
    
    def dfs_traversal(self, start_node):
        """
        Perform DFS traversal starting from the given node.
        
        Args:
            start_node: The node to start DFS from
            
        Returns:
            List of values in DFS order
        """
        # TODO: Implement this method
        # 1. Check if start_node is None, return empty list if it is
        # 2. Create a result list to store the traversal order
        # 3. Call the recursive helper method to perform DFS
        # 4. Return the result list
        if start_node == None:
            return []
        visited = []
        visited.append(start_node.value)
        self._dfs_traverse(start_node, visited)
        return visited

    def _dfs_traverse(self, node, visited):
        if node == None:
            return

        for neighbor in node.neighbors:
            if neighbor.value not in visited:
                visited.append(neighbor.value)
                self._dfs_traverse(neighbor, visited)

    
    def _dfs_recursive(self, node, result):
        """
        Helper method for recursive DFS traversal.
        
        Args:
            node: Current node being visited
            result: List to store the traversal order
        """
        # TODO: Implement this method
        # 1. Check if node is None or already visited, return if it is
        # 2. Mark the node as visited
        # 3. Add the node's value to the result list
        # 4. Recursively visit all unvisited neighbors
        pass
    
    def dfs_iterative(self, start_node):
        """
        Perform iterative DFS traversal starting from the given node.
        
        Args:
            start_node: The node to start DFS from
            
        Returns:
            List of values in DFS order
        """
        # TODO: Implement this method
        # 1. Check if start_node is None, return empty list if it is
        # 2. Create a result list to store the traversal order
        # 3. Create a stack and add the start_node to it
        # 4. Reset visited status of all nodes
        # 5. While the stack is not empty:
        #    a. Pop a node from the stack
        #    b. If the node is not visited:
        #       i. Mark it as visited
        #       ii. Add its value to the result list
        #       iii. Add all unvisited neighbors to the stack (in reverse order)
        # 6. Return the result list
        if start_node == None:
            return []

        visited = []
        stack = deque()

        stack.append(start_node)
        while len(stack) > 0:
            current = stack.pop()
            if current.value not in visited:
                visited.append(current.value)
            for neighbor_node in reversed(current.neighbors):
                if neighbor_node.value not in visited:
                    stack.append(neighbor_node)

        return visited
    
    def find_path(self, start_node, end_node):
        """
        Find a path between start_node and end_node using DFS.
        
        Args:
            start_node: Starting node
            end_node: Target node
            
        Returns:
            List of nodes representing the path, or empty list if no path exists
        """
        # TODO: Implement this method
        # 1. Check if start_node or end_node is None, return empty list if either is
        # 2. Reset visited status of all nodes
        # 3. Create an empty path list
        # 4. Call the recursive helper method to find a path
        # 5. If a path is found, convert the nodes to values and return
        # 6. Otherwise, return an empty list
        if start_node == None or end_node == None:
            return []

        path = []
        self._find_path_recursive(start_node, end_node, path)
        return path
    
    def _find_path_recursive(self, current, end, path):
        """
        Helper method for recursive path finding.
        
        Args:
            current: Current node being visited
            end: Target node
            path: Current path being built
            
        Returns:
            True if a path is found, False otherwise
        """
        # TODO: Implement this method
        # 1. Mark the current node as visited
        # 2. Add the current node to the path
        # 3. If the current node is the end node, return True
        # 4. For each unvisited neighbor:
        #    a. Recursively find a path from the neighbor to the end node
        #    b. If a path is found, return True
        # 5. If no path is found through any neighbor, remove the current node from the path (backtrack)
        # 6. Return False

        return False
    
    def detect_cycle(self):
        """
        Detect if the graph contains a cycle.
        
        Returns:
            True if a cycle is detected, False otherwise
        """
        # TODO: Implement this method
        # 1. Reset visited status of all nodes
        # 2. For each unvisited node in the graph:
        #    a. Call the recursive helper method to detect a cycle
        #    b. If a cycle is detected, return True
        # 3. Return False if no cycle is detected
        return False
    
    def _detect_cycle_recursive(self, current, parent):
        """
        Helper method for recursive cycle detection.
        
        Args:
            current: Current node being visited
            parent: Parent node of the current node
            
        Returns:
            True if a cycle is detected, False otherwise
        """
        # TODO: Implement this method
        # 1. Mark the current node as visited
        # 2. For each neighbor of the current node:
        #    a. If the neighbor is not visited:
        #       i. Recursively check for a cycle from the neighbor
        #       ii. If a cycle is detected, return True
        #    b. If the neighbor is visited and not the parent, a cycle is detected, return True
        # 3. Return False if no cycle is detected
        return False
    
    def topological_sort(self):
        """
        Perform topological sort on a directed acyclic graph (DAG).
        
        Returns:
            List of values in topological order, or empty list if the graph is not a DAG
        """
        # TODO: Implement this method
        # 1. Check if the graph has a cycle (not a DAG), return empty list if it does
        # 2. Reset visited status of all nodes
        # 3. Create a stack to store the topological order
        # 4. For each unvisited node in the graph:
        #    a. Call the recursive helper method to perform topological sort
        # 5. Reverse the stack to get the topological order
        # 6. Convert the nodes to values and return
        return []
    
    def _topological_sort_recursive(self, node, stack):
        """
        Helper method for recursive topological sort.
        
        Args:
            node: Current node being visited
            stack: Stack to store the topological order
        """
        # TODO: Implement this method
        # 1. Mark the node as visited
        # 2. For each unvisited neighbor:
        #    a. Recursively perform topological sort from the neighbor
        # 3. Add the node to the stack
        pass
    
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
        #       i. Perform DFS traversal starting from this node
        #          (this will mark all nodes in the component as visited)
        #       ii. Increment the count
        # 5. Return the count
        return 0
