"""
Breadth-First Search implementation.
This class provides a blueprint for implementing BFS with
various operations like traversal, path finding, and connected components.
"""
from BFS.Python.node import Node
from collections import deque

class BFS:
    def __init__(self, start_node):
        """
        Constructor to create a BFS instance with a start node.
        
        Args:
            start_node: The starting node for BFS traversal
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
        Perform a BFS traversal starting from the start node.
        
        Returns:
            A list of nodes in BFS traversal order
        """
        if self.start_node is None:
            return []
        
        result = []
        visited = set()
        queue = deque([self.start_node])
        visited.add(self.start_node)
        
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for neighbor in node.get_neighbors():
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def find_shortest_path(self, target_value):
        """
        Find the shortest path from the start node to the target node.
        
        Args:
            target_value: The value of the target node
            
        Returns:
            A list of nodes representing the shortest path, or an empty list if no path exists
        """
        if self.start_node is None:
            return []
        
        visited = set()
        queue = deque([(self.start_node, [self.start_node])])
        visited.add(self.start_node)
        
        while queue:
            node, path = queue.popleft()
            
            if node.get_value() == target_value:
                return path
            
            for neighbor in node.get_neighbors():
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = path.copy()
                    new_path.append(neighbor)
                    queue.append((neighbor, new_path))
        
        return []  # No path found
    
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
        queue = deque([self.start_node])
        visited.add(self.start_node)
        
        while queue:
            node = queue.popleft()
            
            if node.get_value() == target_value:
                return True
            
            for neighbor in node.get_neighbors():
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return False
    
    def find_connected_components(self, all_nodes):
        """
        Find all connected components in the graph.
        
        Args:
            all_nodes: A list of all nodes in the graph
            
        Returns:
            A list of lists, where each inner list represents a connected component
        """
        if not all_nodes:
            return []
        
        components = []
        visited = set()
        
        for node in all_nodes:
            if node not in visited:
                component = []
                queue = deque([node])
                visited.add(node)
                
                while queue:
                    current = queue.popleft()
                    component.append(current)
                    
                    for neighbor in current.get_neighbors():
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                
                components.append(component)
        
        return components
    
    def find_levels(self):
        """
        Find the level (distance) of each node from the start node.
        
        Returns:
            A dictionary mapping nodes to their levels
        """
        if self.start_node is None:
            return {}
        
        levels = {}
        visited = set()
        queue = deque([(self.start_node, 0)])
        visited.add(self.start_node)
        
        while queue:
            node, level = queue.popleft()
            levels[node] = level
            
            for neighbor in node.get_neighbors():
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))
        
        return levels
    
    def is_bipartite(self, all_nodes):
        """
        Check if the graph is bipartite (can be divided into two sets
        such that no two nodes within the same set are adjacent).
        
        Args:
            all_nodes: A list of all nodes in the graph
            
        Returns:
            True if the graph is bipartite, False otherwise
        """
        if not all_nodes:
            return True
        
        # Use 0 and 1 to represent the two sets
        colors = {}
        
        for node in all_nodes:
            if node not in colors:
                # Start BFS from this node
                queue = deque([node])
                colors[node] = 0
                
                while queue:
                    current = queue.popleft()
                    current_color = colors[current]
                    
                    for neighbor in current.get_neighbors():
                        if neighbor not in colors:
                            # Assign the opposite color to the neighbor
                            colors[neighbor] = 1 - current_color
                            queue.append(neighbor)
                        elif colors[neighbor] == current_color:
                            # If the neighbor has the same color, the graph is not bipartite
                            return False
        
        return True
