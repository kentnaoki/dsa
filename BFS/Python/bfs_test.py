"""
Test class for the BFS implementation.
This class provides methods to test various operations of the BFS algorithm.
"""
from bfs_template import BFSTemplate
from bfs_solution import BFSSolution
from bfs import BFS

# Uncomment the line below to use your implementation
# BFS = BFSTemplate
# Comment the line below to use your implementation
BFS = BFS

def test_bfs_traversal():
    """
    Test the BFS traversal operation.
    """
    print("\n=== Testing BFS Traversal ===")
    bfs = BFS()
    
    # Create a simple graph
    # 1 -- 2 -- 5
    # |    |
    # 3 -- 4
    node1 = bfs.add_node(1)
    node2 = bfs.add_node(2)
    node3 = bfs.add_node(3)
    node4 = bfs.add_node(4)
    node5 = bfs.add_node(5)
    
    bfs.add_edge(node1, node2)
    bfs.add_edge(node1, node3)
    bfs.add_edge(node2, node4)
    bfs.add_edge(node2, node5)
    bfs.add_edge(node3, node4)
    
    # Test BFS traversal starting from node1
    result = bfs.bfs_traversal(node1)
    expected = [1, 2, 3, 4, 5]  # One possible BFS order
    
    # Since BFS can have multiple valid orders depending on how neighbors are processed,
    # we'll check if all nodes are visited and the first node is correct
    if len(result) == len(expected) and result[0] == 1:
        print("PASS: BFS traversal visits all nodes and starts with the correct node")
    else:
        print("FAIL: BFS traversal does not visit all nodes or does not start with the correct node")
        print("Expected:", expected)
        print("Got:", result)
    
    # Reset visited status
    bfs.reset_visited()
    
    # Test BFS traversal starting from node3
    result = bfs.bfs_traversal(node3)
    if len(result) == len(expected) and result[0] == 3:
        print("PASS: BFS traversal from node3 visits all nodes and starts with the correct node")
    else:
        print("FAIL: BFS traversal from node3 does not visit all nodes or does not start with the correct node")
    
    # Test BFS traversal with null start node
    result = bfs.bfs_traversal(None)
    if len(result) == 0:
        print("PASS: BFS traversal with null start node returns empty list")
    else:
        print("FAIL: BFS traversal with null start node does not return empty list")

def test_find_path():
    """
    Test the find path operation.
    """
    print("\n=== Testing Find Path ===")
    bfs = BFS()
    
    # Create a simple graph
    # 1 -- 2 -- 5
    # |    |
    # 3 -- 4
    node1 = bfs.add_node(1)
    node2 = bfs.add_node(2)
    node3 = bfs.add_node(3)
    node4 = bfs.add_node(4)
    node5 = bfs.add_node(5)
    
    bfs.add_edge(node1, node2)
    bfs.add_edge(node1, node3)
    bfs.add_edge(node2, node4)
    bfs.add_edge(node2, node5)
    bfs.add_edge(node3, node4)
    
    # Test finding path from node1 to node5
    path = bfs.find_path(node1, node5)
    if len(path) > 0 and path[0] == 1 and path[-1] == 5:
        print("PASS: Path from node1 to node5 found")
        print("Path:", path)
    else:
        print("FAIL: Path from node1 to node5 not found correctly")
    
    # Test finding path from node3 to node5
    path = bfs.find_path(node3, node5)
    if len(path) > 0 and path[0] == 3 and path[-1] == 5:
        print("PASS: Path from node3 to node5 found")
        print("Path:", path)
    else:
        print("FAIL: Path from node3 to node5 not found correctly")
    
    # Test finding path with disconnected nodes
    node6 = bfs.add_node(6)  # Disconnected node
    path = bfs.find_path(node1, node6)
    if len(path) == 0:
        print("PASS: No path found to disconnected node")
    else:
        print("FAIL: Path found to disconnected node, but should not exist")
    
    # Test finding path with null nodes
    path = bfs.find_path(None, node5)
    if len(path) == 0:
        print("PASS: No path found with null start node")
    else:
        print("FAIL: Path found with null start node, but should not exist")

def test_find_level():
    """
    Test the find level operation.
    """
    print("\n=== Testing Find Level ===")
    bfs = BFS()
    
    # Create a simple graph
    # 1 -- 2 -- 5
    # |    |
    # 3 -- 4
    node1 = bfs.add_node(1)
    node2 = bfs.add_node(2)
    node3 = bfs.add_node(3)
    node4 = bfs.add_node(4)
    node5 = bfs.add_node(5)
    
    bfs.add_edge(node1, node2)
    bfs.add_edge(node1, node3)
    bfs.add_edge(node2, node4)
    bfs.add_edge(node2, node5)
    bfs.add_edge(node3, node4)
    
    # Test finding level of node5 from node1
    level = bfs.find_level(node1, 5)
    if level == 2:
        print("PASS: Level of node5 from node1 is 2")
    else:
        print("FAIL: Level of node5 from node1 is not 2, got", level)
    
    # Test finding level of node4 from node1
    level = bfs.find_level(node1, 4)
    if level == 2:
        print("PASS: Level of node4 from node1 is 2")
    else:
        print("FAIL: Level of node4 from node1 is not 2, got", level)
    
    # Test finding level of node3 from node1
    level = bfs.find_level(node1, 3)
    if level == 1:
        print("PASS: Level of node3 from node1 is 1")
    else:
        print("FAIL: Level of node3 from node1 is not 1, got", level)
    
    # Test finding level of non-existent value
    level = bfs.find_level(node1, 6)
    if level == -1:
        print("PASS: Level of non-existent value is -1")
    else:
        print("FAIL: Level of non-existent value is not -1, got", level)
    
    # Test finding level with null start node
    level = bfs.find_level(None, 5)
    if level == -1:
        print("PASS: Level with null start node is -1")
    else:
        print("FAIL: Level with null start node is not -1, got", level)

def test_connected_components():
    """
    Test the count connected components operation.
    """
    print("\n=== Testing Connected Components ===")
    bfs = BFS()
    
    # Test empty graph
    count = bfs.count_connected_components()
    if count == 0:
        print("PASS: Empty graph has 0 connected components")
    else:
        print("FAIL: Empty graph does not have 0 connected components, got", count)
    
    # Create a graph with two connected components
    # Component 1: 1 -- 2 -- 3
    # Component 2: 4 -- 5
    node1 = bfs.add_node(1)
    node2 = bfs.add_node(2)
    node3 = bfs.add_node(3)
    node4 = bfs.add_node(4)
    node5 = bfs.add_node(5)
    
    bfs.add_edge(node1, node2)
    bfs.add_edge(node2, node3)
    bfs.add_edge(node4, node5)
    
    count = bfs.count_connected_components()
    if count == 2:
        print("PASS: Graph has 2 connected components")
    else:
        print("FAIL: Graph does not have 2 connected components, got", count)
    
    # Add a third component (isolated node)
    node6 = bfs.add_node(6)
    
    count = bfs.count_connected_components()
    if count == 3:
        print("PASS: Graph has 3 connected components after adding isolated node")
    else:
        print("FAIL: Graph does not have 3 connected components after adding isolated node, got", count)
    
    # Connect the components
    bfs.add_edge(node3, node4)
    
    count = bfs.count_connected_components()
    if count == 2:
        print("PASS: Graph has 2 connected components after connecting two components")
    else:
        print("FAIL: Graph does not have 2 connected components after connecting two components, got", count)

def test_bipartite():
    """
    Test the is bipartite operation.
    """
    print("\n=== Testing Bipartite ===")
    bfs = BFS()
    
    # Test empty graph
    if bfs.is_bipartite(None):
        print("PASS: Empty graph is bipartite")
    else:
        print("FAIL: Empty graph is not considered bipartite")
    
    # Create a bipartite graph
    # 1 -- 2
    # |    |
    # 3 -- 4
    node1 = bfs.add_node(1)
    node2 = bfs.add_node(2)
    node3 = bfs.add_node(3)
    node4 = bfs.add_node(4)
    
    bfs.add_edge(node1, node2)
    bfs.add_edge(node2, node3)
    bfs.add_edge(node3, node4)
    bfs.add_edge(node4, node1)
    
    if bfs.is_bipartite(node1):
        print("PASS: Square graph is bipartite")
    else:
        print("FAIL: Square graph is not considered bipartite")
    
    # Create a non-bipartite graph (odd cycle)
    # 1 -- 2
    # |   /
    # 3 -
    bfs.clear()
    node1 = bfs.add_node(1)
    node2 = bfs.add_node(2)
    node3 = bfs.add_node(3)
    
    bfs.add_edge(node1, node2)
    bfs.add_edge(node2, node3)
    bfs.add_edge(node3, node1)
    
    if not bfs.is_bipartite(node1):
        print("PASS: Triangle graph is not bipartite")
    else:
        print("FAIL: Triangle graph is considered bipartite, but should not be")

def main():
    """
    Main method to run the tests.
    """
    print("Running BFS Tests...")
    print("Using implementation:", "BFSSolution" if BFS == BFSSolution else "BFSTemplate")
    
    test_bfs_traversal()
    test_find_path()
    test_find_level()
    test_connected_components()
    test_bipartite()
    
    print("All tests completed.")

if __name__ == "__main__":
    main()
