"""
Complete implementation of Breadth-First Search (BFS).
This class provides a reference solution for the BFS blueprint.
You can use this as a guide if you get stuck with your implementation.
"""
from collections import deque
from BFS.Python.node import Node

class BFSSolution:
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
        if start_node is None:
            return []
        
        result = []
        queue = deque([start_node])
        start_node.set_visited(True)
        
        while queue:
            current = queue.popleft()
            result.append(current.get_value())
            
            for neighbor in current.get_neighbors():
                if not neighbor.is_visited():
                    queue.append(neighbor)
                    neighbor.set_visited(True)
        
        return result
    
    def find_path(self, start_node, end_node):
        """
        Find a path between start_node and end_node using BFS.
        
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
        
        # Use a queue for BFS
        queue = deque([(start_node, [start_node])])
        start_node.set_visited(True)
        
        while queue:
            current, path = queue.popleft()
            
            if current == end_node:
                return [node.get_value() for node in path]
            
            for neighbor in current.get_neighbors():
                if not neighbor.is_visited():
                    neighbor.set_visited(True)
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append((neighbor, new_path))
        
        return []  # No path found
    
    def find_level(self, start_node, target_value):
        """
        Find the level (distance) of a node with target_value from start_node.
        
        Args:
            start_node: Starting node
            target_value: Value to search for
            
        Returns:
            Level of the target node, or -1 if not found
        """
        if start_node is None:
            return -1
        
        # Reset visited status
        self.reset_visited()
        
        # Use a queue for BFS
        queue = deque([(start_node, 0)])  # (node, level)
        start_node.set_visited(True)
        
        while queue:
            current, level = queue.popleft()
            
            if current.get_value() == target_value:
                return level
            
            for neighbor in current.get_neighbors():
                if not neighbor.is_visited():
                    neighbor.set_visited(True)
                    queue.append((neighbor, level + 1))
        
        return -1  # Value not found
    
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
                self.bfs_traversal(node)  # This will mark all nodes in the component as visited
                count += 1
        
        return count
    
    def is_bipartite(self, start_node):
        """
        Check if the graph is bipartite (can be colored with two colors).
        
        Args:
            start_node: Starting node for the check
            
        Returns:
            True if the graph is bipartite, False otherwise
        """
        if start_node is None:
            return True
        
        # Reset visited status
        self.reset_visited()
        
        # Use a dictionary to store colors (True/False)
        colors = {start_node: True}
        queue = deque([start_node])
        start_node.set_visited(True)
        
        while queue:
            current = queue.popleft()
            current_color = colors[current]
            
            for neighbor in current.get_neighbors():
                if neighbor not in colors:
                    colors[neighbor] = not current_color
                    queue.append(neighbor)
                    neighbor.set_visited(True)
                elif colors[neighbor] == current_color:
                    return False
        
        return True
