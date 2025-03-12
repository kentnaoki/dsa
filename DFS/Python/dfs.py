"""
Depth-First Search implementation.
This class provides a blueprint for implementing DFS with
various operations like traversal, path finding, and cycle detection.
"""
from DFS.Python.node import Node
from collections import deque

class DFS:
    def __init__(self, start_node):
        """
        Constructor to create a DFS instance with a start node.
        
        Args:
            start_node: The starting node for DFS traversal
        """
        self.start_node = start_node
    
    def get_start_node(self):
        """
        Get the start node.
        
        Returns:
            The start node
        """
        return self.start_node
    
    def set_start_node(self, start_node):
        """
        Set the start node.
        
        Args:
            start_node: The new start node
        """
        self.start_node = start_node
    
    def traverse(self):
        """
        Perform a DFS traversal starting from the start node.
        
        Returns:
            A list of nodes in DFS traversal order
        """
        if self.start_node is None:
            return []
        
        result = []
        visited = set()
        
        self._dfs_traversal(self.start_node, visited, result)
        
        return result
    
    def _dfs_traversal(self, node, visited, result):
        """
        Helper method for recursive DFS traversal.
        
        Args:
            node: The current node
            visited: Set of visited nodes
            result: List to store the traversal result
        """
        # Mark the current node as visited and add to result
        visited.add(node)
        result.append(node)
        
        # Recur for all the neighbors
        for neighbor in node.get_neighbors():
            if neighbor not in visited:
                self._dfs_traversal(neighbor, visited, result)
    
    def find_path(self, target_value):
        """
        Find a path from the start node to the target node.
        
        Args:
            target_value: The value of the target node
            
        Returns:
            A list of nodes representing a path, or an empty list if no path exists
        """
        if self.start_node is None:
            return []
        
        visited = set()
        path = []
        
        if self._dfs_path(self.start_node, target_value, visited, path):
            return path
        
        return []
    
    def _dfs_path(self, node, target_value, visited, path):
        """
        Helper method for recursive DFS path finding.
        
        Args:
            node: The current node
            target_value: The value to search for
            visited: Set of visited nodes
            path: List to store the path
            
        Returns:
            True if a path is found, False otherwise
        """
        # Mark the current node as visited and add to path
        visited.add(node)
        path.append(node)
        
        # If current node has the target value, return True
        if node.get_value() == target_value:
            return True
        
        # Recur for all the neighbors
        for neighbor in node.get_neighbors():
            if neighbor not in visited:
                if self._dfs_path(neighbor, target_value, visited, path):
                    return True
        
        # If no path is found, remove the current node from path
        path.pop()
        return False
    
    def has_path(self, target_value):
        """
        Check if there is a path from the start node to a node with the target value.
        
        Args:
            target_value: The value to search for
            
        Returns:
            True if a path exists, False otherwise
        """
        if self.start_node is None:
            return False
        
        visited = set()
        return self._dfs_has_path(self.start_node, target_value, visited)
    
    def _dfs_has_path(self, node, target_value, visited):
        """
        Helper method for recursive DFS path checking.
        
        Args:
            node: The current node
            target_value: The value to search for
            visited: Set of visited nodes
            
        Returns:
            True if a path is found, False otherwise
        """
        # Mark the current node as visited
        visited.add(node)
        
        # If current node has the target value, return True
        if node.get_value() == target_value:
            return True
        
        # Recur for all the neighbors
        for neighbor in node.get_neighbors():
            if neighbor not in visited:
                if self._dfs_has_path(neighbor, target_value, visited):
                    return True
        
        return False
    
    def has_cycle(self, all_nodes):
        """
        Detect if there is a cycle in the graph.
        
        Args:
            all_nodes: A list of all nodes in the graph
            
        Returns:
            True if a cycle is detected, False otherwise
        """
        if not all_nodes:
            return False
        
        visited = set()
        recursion_stack = set()
        
        for node in all_nodes:
            if node not in visited:
                if self._dfs_has_cycle(node, visited, recursion_stack):
                    return True
        
        return False
    
    def _dfs_has_cycle(self, node, visited, recursion_stack):
        """
        Helper method for recursive DFS cycle detection.
        
        Args:
            node: The current node
            visited: Set of visited nodes
            recursion_stack: Set of nodes in the current recursion stack
            
        Returns:
            True if a cycle is detected, False otherwise
        """
        # Mark the current node as visited and add to recursion stack
        visited.add(node)
        recursion_stack.add(node)
        
        # Recur for all the neighbors
        for neighbor in node.get_neighbors():
            # If the neighbor is not visited, recur for it
            if neighbor not in visited:
                if self._dfs_has_cycle(neighbor, visited, recursion_stack):
                    return True
            # If the neighbor is in the recursion stack, there is a cycle
            elif neighbor in recursion_stack:
                return True
        
        # Remove the current node from recursion stack
        recursion_stack.remove(node)
        return False
    
    def topological_sort(self, all_nodes):
        """
        Perform a topological sort of the graph.
        
        Args:
            all_nodes: A list of all nodes in the graph
            
        Returns:
            A list of nodes in topological order, or an empty list if a cycle is detected
        """
        if not all_nodes:
            return []
        
        # Check if the graph has a cycle
        if self.has_cycle(all_nodes):
            return []
        
        stack = []
        visited = set()
        
        # Call the recursive helper function to store topological sort
        for node in all_nodes:
            if node not in visited:
                self._dfs_topological_sort(node, visited, stack)
        
        # Reverse the stack to get the topological sort
        return stack[::-1]
    
    def _dfs_topological_sort(self, node, visited, stack):
        """
        Helper method for recursive DFS topological sort.
        
        Args:
            node: The current node
            visited: Set of visited nodes
            stack: List to store the topological sort
        """
        # Mark the current node as visited
        visited.add(node)
        
        # Recur for all the neighbors
        for neighbor in node.get_neighbors():
            if neighbor not in visited:
                self._dfs_topological_sort(neighbor, visited, stack)
        
        # Push current node to stack
        stack.append(node)
    
    def find_strongly_connected_components(self, all_nodes):
        """
        Find all strongly connected components in the graph.
        
        Args:
            all_nodes: A list of all nodes in the graph
            
        Returns:
            A list of lists, where each inner list represents a strongly connected component
        """
        if not all_nodes:
            return []
        
        # Step 1: Perform DFS and store nodes in order of finishing time
        stack = []
        visited = set()
        
        for node in all_nodes:
            if node not in visited:
                self._fill_order(node, visited, stack)
        
        # Step 2: Create a transpose graph (reverse all edges)
        transpose = {node: [] for node in all_nodes}
        
        for node in all_nodes:
            for neighbor in node.get_neighbors():
                transpose[neighbor].append(node)
        
        # Step 3: Process nodes in order of finishing time
        visited.clear()
        components = []
        
        while stack:
            node = stack.pop()
            
            if node not in visited:
                component = []
                self._dfs_util(node, visited, component, transpose)
                components.append(component)
        
        return components
    
    def _fill_order(self, node, visited, stack):
        """
        Helper method to fill the stack with nodes in order of finishing time.
        
        Args:
            node: The current node
            visited: Set of visited nodes
            stack: List to store nodes in order of finishing time
        """
        visited.add(node)
        
        for neighbor in node.get_neighbors():
            if neighbor not in visited:
                self._fill_order(neighbor, visited, stack)
        
        stack.append(node)
    
    def _dfs_util(self, node, visited, component, transpose):
        """
        Helper method for DFS on the transpose graph.
        
        Args:
            node: The current node
            visited: Set of visited nodes
            component: List to store the current component
            transpose: Dictionary representing the transpose graph
        """
        visited.add(node)
        component.append(node)
        
        for neighbor in transpose[node]:
            if neighbor not in visited:
                self._dfs_util(neighbor, visited, component, transpose)
    
    def find_articulation_points(self, all_nodes):
        """
        Find the articulation points (cut vertices) in the graph.
        
        Args:
            all_nodes: A list of all nodes in the graph
            
        Returns:
            A list of nodes that are articulation points
        """
        if not all_nodes:
            return []
        
        articulation_points = set()
        visited = set()
        disc = {}  # Discovery time
        low = {}   # Earliest visited vertex
        parent = {}  # Parent in DFS tree
        time = [0]  # Time counter (as a list to make it mutable)
        
        for node in all_nodes:
            if node not in visited:
                self._dfs_articulation_points(node, visited, disc, low, parent, articulation_points, time)
        
        return list(articulation_points)
    
    def _dfs_articulation_points(self, node, visited, disc, low, parent, articulation_points, time):
        """
        Helper method for finding articulation points using DFS.
        
        Args:
            node: The current node
            visited: Set of visited nodes
            disc: Dictionary of discovery times
            low: Dictionary of lowest discovery times
            parent: Dictionary of parent nodes
            articulation_points: Set to store articulation points
            time: Time counter (as a list to make it mutable)
        """
        # Count of children in DFS tree
        children = 0
        
        # Mark the current node as visited
        visited.add(node)
        
        # Initialize discovery time and low value
        disc[node] = time[0]
        low[node] = time[0]
        time[0] += 1
        
        # Recur for all the neighbors
        for neighbor in node.get_neighbors():
            # If neighbor is not visited yet, then make it a child of node in DFS tree and recur for it
            if neighbor not in visited:
                children += 1
                parent[neighbor] = node
                
                self._dfs_articulation_points(neighbor, visited, disc, low, parent, articulation_points, time)
                
                # Check if the subtree rooted with neighbor has a connection to one of the ancestors of node
                low[node] = min(low[node], low[neighbor])
                
                # node is an articulation point in following cases:
                
                # (1) node is root of DFS tree and has two or more children
                if node not in parent and children > 1:
                    articulation_points.add(node)
                
                # (2) If node is not root and low value of one of its children is more than or equal to discovery value of node
                if node in parent and low[neighbor] >= disc[node]:
                    articulation_points.add(node)
            
            # Update low value of node for parent function calls
            elif neighbor != parent.get(node):
                low[node] = min(low[node], disc[neighbor])
