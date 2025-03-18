"""
Test class for the DFS implementation.
This class provides methods to test various operations of the DFS algorithm.
"""
from dfs_template import DFSTemplate
from dfs_solution import DFSSolution
from dfs import DFS
from dfs_v2 import DFSV2

# Uncomment the line below to use your implementation
# DFS = DFSTemplate
# Comment the line below to use your implementation
DFS = DFSV2

def test_dfs_traversal():
    """
    Test the DFS traversal operation.
    """
    print("\n=== Testing DFS Traversal ===")
    dfs = DFS()
    
    # Create a simple graph
    # 1 -- 2 -- 5
    # |    |
    # 3 -- 4
    node1 = dfs.add_node(1)
    node2 = dfs.add_node(2)
    node3 = dfs.add_node(3)
    node4 = dfs.add_node(4)
    node5 = dfs.add_node(5)
    
    dfs.add_edge(node1, node2)
    dfs.add_edge(node1, node3)
    dfs.add_edge(node2, node4)
    dfs.add_edge(node2, node5)
    dfs.add_edge(node3, node4)
    
    # Test DFS traversal starting from node1
    result = dfs.dfs_traversal(node1)
    
    # Since DFS can have multiple valid orders depending on how neighbors are processed,
    # we'll check if all nodes are visited and the first node is correct
    if len(result) == 5 and result[0] == 1:
        print("PASS: DFS traversal visits all nodes and starts with the correct node")
        print("Traversal order:", result)
    else:
        print("FAIL: DFS traversal does not visit all nodes or does not start with the correct node")
        print("Got:", result)
    
    # Reset visited status
    dfs.reset_visited()
    
    # Test DFS traversal starting from node3
    result = dfs.dfs_traversal(node3)
    if len(result) == 5 and result[0] == 3:
        print("PASS: DFS traversal from node3 visits all nodes and starts with the correct node")
        print("Traversal order:", result)
    else:
        print("FAIL: DFS traversal from node3 does not visit all nodes or does not start with the correct node")
        print("Got:", result)
    
    # Test DFS traversal with null start node
    result = dfs.dfs_traversal(None)
    if len(result) == 0:
        print("PASS: DFS traversal with null start node returns empty list")
    else:
        print("FAIL: DFS traversal with null start node does not return empty list")
        print("Got:", result)

def test_dfs_iterative():
    """
    Test the iterative DFS traversal operation.
    """
    print("\n=== Testing Iterative DFS Traversal ===")
    dfs = DFS()
    
    # Create a simple graph
    # 1 -- 2 -- 5
    # |    |
    # 3 -- 4
    node1 = dfs.add_node(1)
    node2 = dfs.add_node(2)
    node3 = dfs.add_node(3)
    node4 = dfs.add_node(4)
    node5 = dfs.add_node(5)
    
    dfs.add_edge(node1, node2)
    dfs.add_edge(node1, node3)
    dfs.add_edge(node2, node4)
    dfs.add_edge(node2, node5)
    dfs.add_edge(node3, node4)
    
    # Test iterative DFS traversal starting from node1
    result = dfs.dfs_iterative(node1)
    
    if len(result) == 5 and result[0] == 1:
        print("PASS: Iterative DFS traversal visits all nodes and starts with the correct node")
        print("Traversal order:", result)
    else:
        print("FAIL: Iterative DFS traversal does not visit all nodes or does not start with the correct node")
        print("Got:", result)
    
    # Test iterative DFS traversal with null start node
    result = dfs.dfs_iterative(None)
    if len(result) == 0:
        print("PASS: Iterative DFS traversal with null start node returns empty list")
    else:
        print("FAIL: Iterative DFS traversal with null start node does not return empty list")
        print("Got:", result)

def test_find_path():
    """
    Test the find path operation.
    """
    print("\n=== Testing Find Path ===")
    dfs = DFS()
    
    # Create a simple graph
    # 1 -- 2 -- 5
    # |    |
    # 3 -- 4
    node1 = dfs.add_node(1)
    node2 = dfs.add_node(2)
    node3 = dfs.add_node(3)
    node4 = dfs.add_node(4)
    node5 = dfs.add_node(5)
    
    dfs.add_edge(node1, node2)
    dfs.add_edge(node1, node3)
    dfs.add_edge(node2, node4)
    dfs.add_edge(node2, node5)
    dfs.add_edge(node3, node4)
    
    # Test finding path from node1 to node5
    path = dfs.find_path(node1, node5)
    if len(path) > 0 and path[0] == 1 and path[-1] == 5:
        print("PASS: Path from node1 to node5 found")
        print("Path:", path)
    else:
        print("FAIL: Path from node1 to node5 not found correctly")
        print("Got:", path)
    
    # Test finding path from node3 to node5
    path = dfs.find_path(node3, node5)
    if len(path) > 0 and path[0] == 3 and path[-1] == 5:
        print("PASS: Path from node3 to node5 found")
        print("Path:", path)
    else:
        print("FAIL: Path from node3 to node5 not found correctly")
        print("Got:", path)
    
    # Test finding path with disconnected nodes
    node6 = dfs.add_node(6)  # Disconnected node
    path = dfs.find_path(node1, node6)
    if len(path) == 0:
        print("PASS: No path found to disconnected node")
    else:
        print("FAIL: Path found to disconnected node, but should not exist")
        print("Got:", path)
    
    # Test finding path with null nodes
    path = dfs.find_path(None, node5)
    if len(path) == 0:
        print("PASS: No path found with null start node")
    else:
        print("FAIL: Path found with null start node, but should not exist")
        print("Got:", path)

def test_detect_cycle():
    """
    Test the cycle detection operation.
    """
    print("\n=== Testing Cycle Detection ===")
    dfs = DFS()
    
    # Create a graph without cycles
    # 1 -- 2 -- 3
    #      |
    #      4
    node1 = dfs.add_node(1)
    node2 = dfs.add_node(2)
    node3 = dfs.add_node(3)
    node4 = dfs.add_node(4)
    
    dfs.add_edge(node1, node2)
    dfs.add_edge(node2, node3)
    dfs.add_edge(node2, node4)
    
    if not dfs.detect_cycle():
        print("PASS: No cycle detected in acyclic graph")
    else:
        print("FAIL: Cycle detected in acyclic graph")
    
    # Add an edge to create a cycle
    dfs.add_edge(node1, node4)
    
    if dfs.detect_cycle():
        print("PASS: Cycle detected in cyclic graph")
    else:
        print("FAIL: No cycle detected in cyclic graph")
    
    # Test with empty graph
    dfs.clear()
    if not dfs.detect_cycle():
        print("PASS: No cycle detected in empty graph")
    else:
        print("FAIL: Cycle detected in empty graph")

def test_topological_sort():
    """
    Test the topological sort operation.
    """
    print("\n=== Testing Topological Sort ===")
    dfs = DFS()
    
    # Create a directed acyclic graph (DAG)
    # For this test, we'll treat the edges as directed
    # 1 -> 2 -> 3
    # |    |
    # v    v
    # 4 -> 5
    node1 = dfs.add_node(1)
    node2 = dfs.add_node(2)
    node3 = dfs.add_node(3)
    node4 = dfs.add_node(4)
    node5 = dfs.add_node(5)
    
    # Clear the graph and add directed edges
    dfs.clear()
    dfs.nodes = [node1, node2, node3, node4, node5]
    
    # Add directed edges (not using add_edge to avoid bidirectional edges)
    node1.add_neighbor(node2)
    node1.add_neighbor(node4)
    node2.add_neighbor(node3)
    node2.add_neighbor(node5)
    node4.add_neighbor(node5)
    
    # Test topological sort
    result = dfs.topological_sort()
    
    # Check if the result is a valid topological order
    # In a valid order, for each edge u -> v, u comes before v in the order
    valid = True
    if len(result) != 5:
        valid = False
    else:
        # Check if node1 comes before node2 and node4
        if result.index(1) > result.index(2) or result.index(1) > result.index(4):
            valid = False
        # Check if node2 comes before node3 and node5
        if result.index(2) > result.index(3) or result.index(2) > result.index(5):
            valid = False
        # Check if node4 comes before node5
        if result.index(4) > result.index(5):
            valid = False
    
    if valid:
        print("PASS: Valid topological sort")
        print("Topological order:", result)
    else:
        print("FAIL: Invalid topological sort")
        print("Got:", result)
    
    # Add an edge to create a cycle
    node3.add_neighbor(node1)
    
    # Test topological sort on a graph with a cycle
    result = dfs.topological_sort()
    if len(result) == 0:
        print("PASS: Topological sort returns empty list for graph with cycle")
    else:
        print("FAIL: Topological sort does not return empty list for graph with cycle")
        print("Got:", result)

def test_connected_components():
    """
    Test the count connected components operation.
    """
    print("\n=== Testing Connected Components ===")
    dfs = DFS()
    
    # Test empty graph
    count = dfs.count_connected_components()
    if count == 0:
        print("PASS: Empty graph has 0 connected components")
    else:
        print("FAIL: Empty graph does not have 0 connected components, got", count)
    
    # Create a graph with two connected components
    # Component 1: 1 -- 2 -- 3
    # Component 2: 4 -- 5
    node1 = dfs.add_node(1)
    node2 = dfs.add_node(2)
    node3 = dfs.add_node(3)
    node4 = dfs.add_node(4)
    node5 = dfs.add_node(5)
    
    dfs.add_edge(node1, node2)
    dfs.add_edge(node2, node3)
    dfs.add_edge(node4, node5)
    
    count = dfs.count_connected_components()
    if count == 2:
        print("PASS: Graph has 2 connected components")
    else:
        print("FAIL: Graph does not have 2 connected components, got", count)
    
    # Add a third component (isolated node)
    node6 = dfs.add_node(6)
    
    count = dfs.count_connected_components()
    if count == 3:
        print("PASS: Graph has 3 connected components after adding isolated node")
    else:
        print("FAIL: Graph does not have 3 connected components after adding isolated node, got", count)
    
    # Connect the components
    dfs.add_edge(node3, node4)
    
    count = dfs.count_connected_components()
    if count == 2:
        print("PASS: Graph has 2 connected components after connecting two components")
    else:
        print("FAIL: Graph does not have 2 connected components after connecting two components, got", count)

def main():
    """
    Main method to run the tests.
    """
    print("Running DFS Tests...")
    print("Using implementation:", "DFSSolution" if DFS == DFSSolution else "DFSTemplate")
    
    test_dfs_traversal()
    test_dfs_iterative()
    test_find_path()
    test_detect_cycle()
    test_topological_sort()
    test_connected_components()
    
    print("All tests completed.")

if __name__ == "__main__":
    main()
