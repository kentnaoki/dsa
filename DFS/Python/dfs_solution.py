"""
Complete implementation of Depth-First Search (DFS).
This class provides a reference solution for the DFS blueprint.
You can use this as a guide if you get stuck with your implementation.
"""
from DFS.Python.node import Node

class DFSSolution:
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
        if start_node is None:
            return []
        
        result = []
        self._dfs_recursive(start_node, result)
        return result
    
    def _dfs_recursive(self, node, result):
        """
        Helper method for recursive DFS traversal.
        
        Args:
            node: Current node being visited
            result: List to store the traversal order
        """
        if node is None or node.is_visited():
            return
        
        node.set_visited(True)
        result.append(node.get_value())
        
        for neighbor in node.get_neighbors():
            self._dfs_recursive(neighbor, result)
    
    def dfs_iterative(self, start_node):
        """
        Perform iterative DFS traversal starting from the given node.
        
        Args:
            start_node: The node to start DFS from
            
        Returns:
            List of values in DFS order
        """
        if start_node is None:
            return []
        
        result = []
        stack = [start_node]
        
        # Reset visited status
        self.reset_visited()
        
        while stack:
            current = stack.pop()
            
            if not current.is_visited():
                current.set_visited(True)
                result.append(current.get_value())
                
                # Add neighbors in reverse order to maintain similar traversal to recursive
                for neighbor in reversed(current.get_neighbors()):
                    if not neighbor.is_visited():
                        stack.append(neighbor)
        
        return result
    
    def find_path(self, start_node, end_node):
        """
        Find a path between start_node and end_node using DFS.
        
        Args:
            start_node: Starting node
            end_node: Target node
            
        Returns:
            List of nodes representing the path, or empty list if no path exists
        """
        if start_node is None or end_node is None:
            return []
        
        # Reset visited status
        self.reset_visited()
        
        path = []
        if self._find_path_recursive(start_node, end_node, path):
            return [node.get_value() for node in path]
        
        return []
    
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
        current.set_visited(True)
        path.append(current)
        
        if current == end:
            return True
        
        for neighbor in current.get_neighbors():
            if not neighbor.is_visited():
                if self._find_path_recursive(neighbor, end, path):
                    return True
        
        # Backtrack if no path is found through this node
        path.pop()
        return False
    
    def detect_cycle(self):
        """
        Detect if the graph contains a cycle.
        
        Returns:
            True if a cycle is detected, False otherwise
        """
        # Reset visited status
        self.reset_visited()
        
        for node in self.nodes:
            if not node.is_visited():
                if self._detect_cycle_recursive(node, None):
                    return True
        
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
        current.set_visited(True)
        
        for neighbor in current.get_neighbors():
            # If neighbor is not visited, recursively check for cycle
            if not neighbor.is_visited():
                if self._detect_cycle_recursive(neighbor, current):
                    return True
            # If neighbor is visited and not the parent, a cycle is detected
            elif neighbor != parent:
                return True
        
        return False
    
    def topological_sort(self):
        """
        Perform topological sort on a directed acyclic graph (DAG).
        
        Returns:
            List of values in topological order, or empty list if the graph is not a DAG
        """
        # Check if the graph has a cycle (not a DAG)
        if self.detect_cycle():
            return []
        
        # Reset visited status
        self.reset_visited()
        
        stack = []
        for node in self.nodes:
            if not node.is_visited():
                self._topological_sort_recursive(node, stack)
        
        # Reverse the stack to get the topological order
        stack.reverse()
        return [node.get_value() for node in stack]
    
    def _topological_sort_recursive(self, node, stack):
        """
        Helper method for recursive topological sort.
        
        Args:
            node: Current node being visited
            stack: Stack to store the topological order
        """
        node.set_visited(True)
        
        for neighbor in node.get_neighbors():
            if not neighbor.is_visited():
                self._topological_sort_recursive(neighbor, stack)
        
        stack.append(node)
    
    def count_connected_components(self):
        """
        Count the number of connected components in the graph.
        
        Returns:
            Number of connected components
        """
        if not self.nodes:
            return 0
        
        # Reset visited status
        self.reset_visited()
        
        count = 0
        for node in self.nodes:
            if not node.is_visited():
                self.dfs_traversal(node)  # This will mark all nodes in the component as visited
                count += 1
        
        return count
