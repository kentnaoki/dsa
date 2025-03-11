package DFS.Java;

/**
 * Test class for the Depth-First Search implementation.
 * This class provides methods to test various operations of the DFS algorithm.
 */
public class DFSTest {
    
    /**
     * Main method to run the tests.
     * 
     * @param args Command line arguments (not used)
     */
    public static void main(String[] args) {
        System.out.println("Running Depth-First Search Tests...");
        
        testTraversal();
        testFindPath();
        testHasPath();
        testHasCycle();
        testTopologicalSort();
        testStronglyConnectedComponents();
        testArticulationPoints();
        
        System.out.println("All tests completed.");
    }
    
    /**
     * Test the DFS traversal operation.
     */
    private static void testTraversal() {
        System.out.println("\n=== Testing DFS Traversal ===");
        
        // Create a simple graph
        Node node1 = new Node(1);
        Node node2 = new Node(2);
        Node node3 = new Node(3);
        Node node4 = new Node(4);
        Node node5 = new Node(5);
        
        node1.addNeighbor(node2);
        node1.addNeighbor(node3);
        node2.addNeighbor(node4);
        node3.addNeighbor(node5);
        
        DFS dfs = new DFS(node1);
        
        // Test traversal
        System.out.println("DFS Traversal (expected: 1, 2, 4, 3, 5 or 1, 3, 5, 2, 4):");
        Node[] traversalResult = dfs.traverse();
        
        if (traversalResult.length == 0) {
            System.out.println("FAIL: Traversal returned empty array");
        } else {
            System.out.print("Traversal result: ");
            for (Node node : traversalResult) {
                System.out.print(node.getValue() + " ");
            }
            System.out.println();
            
            // Check if the first node is the start node
            if (traversalResult[0].getValue() == 1) {
                System.out.println("PASS: First node is the start node (1)");
            } else {
                System.out.println("FAIL: First node is not the start node");
            }
            
            // Check if all nodes are visited
            if (traversalResult.length == 5) {
                System.out.println("PASS: All nodes are visited");
            } else {
                System.out.println("FAIL: Not all nodes are visited");
            }
        }
    }
    
    /**
     * Test the findPath operation.
     */
    private static void testFindPath() {
        System.out.println("\n=== Testing Find Path ===");
        
        // Create a graph
        Node node1 = new Node(1);
        Node node2 = new Node(2);
        Node node3 = new Node(3);
        Node node4 = new Node(4);
        Node node5 = new Node(5);
        
        node1.addNeighbor(node2);
        node1.addNeighbor(node3);
        node2.addNeighbor(node4);
        node3.addNeighbor(node5);
        
        DFS dfs = new DFS(node1);
        
        // Test finding path to node 5
        System.out.println("Path from 1 to 5 (expected: 1, 3, 5):");
        Node[] pathResult = dfs.findPath(5);
        
        if (pathResult.length == 0) {
            System.out.println("FAIL: Path returned empty array");
        } else {
            System.out.print("Path result: ");
            for (Node node : pathResult) {
                System.out.print(node.getValue() + " ");
            }
            System.out.println();
            
            // Check if the path starts with the start node and ends with the target node
            if (pathResult[0].getValue() == 1 && pathResult[pathResult.length - 1].getValue() == 5) {
                System.out.println("PASS: Path starts with 1 and ends with 5");
            } else {
                System.out.println("FAIL: Path does not start with 1 or does not end with 5");
            }
            
            // Check if the path is valid (each node is a neighbor of the previous node)
            boolean validPath = true;
            for (int i = 0; i < pathResult.length - 1; i++) {
                boolean isNeighbor = false;
                for (Node neighbor : pathResult[i].getNeighbors()) {
                    if (neighbor == pathResult[i + 1]) {
                        isNeighbor = true;
                        break;
                    }
                }
                if (!isNeighbor) {
                    validPath = false;
                    break;
                }
            }
            
            if (validPath) {
                System.out.println("PASS: Path is valid");
            } else {
                System.out.println("FAIL: Path is not valid");
            }
        }
        
        // Test finding path to a non-existent node
        System.out.println("\nPath from 1 to 6 (expected: empty path):");
        Node[] nonExistentPath = dfs.findPath(6);
        
        if (nonExistentPath.length == 0) {
            System.out.println("PASS: Path to non-existent node returned empty array");
        } else {
            System.out.println("FAIL: Path to non-existent node did not return empty array");
        }
    }
    
    /**
     * Test the hasPath operation.
     */
    private static void testHasPath() {
        System.out.println("\n=== Testing Has Path ===");
        
        // Create a graph
        Node node1 = new Node(1);
        Node node2 = new Node(2);
        Node node3 = new Node(3);
        Node node4 = new Node(4);
        Node node5 = new Node(5);
        
        node1.addNeighbor(node2);
        node1.addNeighbor(node3);
        node2.addNeighbor(node4);
        
        DFS dfs = new DFS(node1);
        
        // Test path to existing nodes
        if (dfs.hasPath(4)) {
            System.out.println("PASS: Found path to node 4");
        } else {
            System.out.println("FAIL: Could not find path to node 4");
        }
        
        // Test path to non-existent node
        if (!dfs.hasPath(5)) {
            System.out.println("PASS: Did not find path to node 5");
        } else {
            System.out.println("FAIL: Found path to node 5, but it should not be reachable");
        }
    }
    
    /**
     * Test the hasCycle operation.
     */
    private static void testHasCycle() {
        System.out.println("\n=== Testing Has Cycle ===");
        
        // Create a graph with a cycle
        Node node1 = new Node(1);
        Node node2 = new Node(2);
        Node node3 = new Node(3);
        
        node1.addNeighbor(node2);
        node2.addNeighbor(node3);
        node3.addNeighbor(node1); // Creates a cycle
        
        Node[] cycleNodes = {node1, node2, node3};
        
        DFS dfs = new DFS(null); // Start node doesn't matter for this test
        
        // Test cycle detection
        if (dfs.hasCycle(cycleNodes)) {
            System.out.println("PASS: Detected cycle in graph with cycle");
        } else {
            System.out.println("FAIL: Did not detect cycle in graph with cycle");
        }
        
        // Create a graph without a cycle
        Node nodeA = new Node(1);
        Node nodeB = new Node(2);
        Node nodeC = new Node(3);
        
        nodeA.addNeighbor(nodeB);
        nodeA.addNeighbor(nodeC);
        
        Node[] noCycleNodes = {nodeA, nodeB, nodeC};
        
        // Test cycle detection
        if (!dfs.hasCycle(noCycleNodes)) {
            System.out.println("PASS: Did not detect cycle in graph without cycle");
        } else {
            System.out.println("FAIL: Detected cycle in graph without cycle");
        }
    }
    
    /**
     * Test the topologicalSort operation.
     */
    private static void testTopologicalSort() {
        System.out.println("\n=== Testing Topological Sort ===");
        
        // Create a directed acyclic graph (DAG)
        Node node1 = new Node(1);
        Node node2 = new Node(2);
        Node node3 = new Node(3);
        Node node4 = new Node(4);
        Node node5 = new Node(5);
        
        node1.addNeighbor(node2);
        node1.addNeighbor(node3);
        node2.addNeighbor(node4);
        node3.addNeighbor(node4);
        node4.addNeighbor(node5);
        
        Node[] dagNodes = {node1, node2, node3, node4, node5};
        
        DFS dfs = new DFS(null); // Start node doesn't matter for this test
        
        // Test topological sort
        System.out.println("Topological sort (expected: 1, 2, 3, 4, 5 or 1, 3, 2, 4, 5):");
        Node[] sortResult = dfs.topologicalSort(dagNodes);
        
        if (sortResult.length == 0) {
            System.out.println("FAIL: Topological sort returned empty array");
        } else {
            System.out.print("Sort result: ");
            for (Node node : sortResult) {
                System.out.print(node.getValue() + " ");
            }
            System.out.println();
            
            // Check if the sort is valid (for each edge u->v, u comes before v in the sort)
            boolean validSort = true;
            for (Node node : dagNodes) {
                int nodeIndex = -1;
                for (int i = 0; i < sortResult.length; i++) {
                    if (sortResult[i] == node) {
                        nodeIndex = i;
                        break;
                    }
                }
                
                for (Node neighbor : node.getNeighbors()) {
                    int neighborIndex = -1;
                    for (int i = 0; i < sortResult.length; i++) {
                        if (sortResult[i] == neighbor) {
                            neighborIndex = i;
                            break;
                        }
                    }
                    
                    if (nodeIndex > neighborIndex) {
                        validSort = false;
                        break;
                    }
                }
                
                if (!validSort) {
                    break;
                }
            }
            
            if (validSort) {
                System.out.println("PASS: Topological sort is valid");
            } else {
                System.out.println("FAIL: Topological sort is not valid");
            }
        }
        
        // Create a graph with a cycle
        Node nodeA = new Node(1);
        Node nodeB = new Node(2);
        Node nodeC = new Node(3);
        
        nodeA.addNeighbor(nodeB);
        nodeB.addNeighbor(nodeC);
        nodeC.addNeighbor(nodeA); // Creates a cycle
        
        Node[] cycleNodes = {nodeA, nodeB, nodeC};
        
        // Test topological sort on a graph with a cycle
        System.out.println("\nTopological sort on a graph with a cycle (expected: empty array):");
        Node[] cycleSortResult = dfs.topologicalSort(cycleNodes);
        
        if (cycleSortResult.length == 0) {
            System.out.println("PASS: Topological sort on a graph with a cycle returned empty array");
        } else {
            System.out.println("FAIL: Topological sort on a graph with a cycle did not return empty array");
        }
    }
    
    /**
     * Test the findStronglyConnectedComponents operation.
     */
    private static void testStronglyConnectedComponents() {
        System.out.println("\n=== Testing Strongly Connected Components ===");
        
        // Create a graph with multiple strongly connected components
        Node node1 = new Node(1);
        Node node2 = new Node(2);
        Node node3 = new Node(3);
        Node node4 = new Node(4);
        Node node5 = new Node(5);
        Node node6 = new Node(6);
        Node node7 = new Node(7);
        Node node8 = new Node(8);
        
        // Component 1: 1, 2, 3
        node1.addNeighbor(node2);
        node2.addNeighbor(node3);
        node3.addNeighbor(node1);
        
        // Component 2: 4, 5
        node4.addNeighbor(node5);
        node5.addNeighbor(node4);
        
        // Component 3: 6
        
        // Component 4: 7, 8
        node7.addNeighbor(node8);
        node8.addNeighbor(node7);
        
        // Connect components
        node3.addNeighbor(node4);
        node5.addNeighbor(node6);
        node6.addNeighbor(node7);
        
        Node[] allNodes = {node1, node2, node3, node4, node5, node6, node7, node8};
        
        DFS dfs = new DFS(null); // Start node doesn't matter for this test
        
        // Test finding strongly connected components
        Node[][] components = dfs.findStronglyConnectedComponents(allNodes);
        
        if (components.length == 0) {
            System.out.println("FAIL: Strongly connected components returned empty array");
        } else {
            System.out.println("Number of strongly connected components: " + components.length);
            
            // Check if the number of components is correct (should be 4)
            if (components.length == 4) {
                System.out.println("PASS: Found 4 strongly connected components");
            } else {
                System.out.println("FAIL: Did not find 4 strongly connected components");
            }
            
            // Print the components
            for (int i = 0; i < components.length; i++) {
                System.out.print("Component " + (i + 1) + ": ");
                for (Node node : components[i]) {
                    System.out.print(node.getValue() + " ");
                }
                System.out.println();
            }
        }
    }
    
    /**
     * Test the findArticulationPoints operation.
     */
    private static void testArticulationPoints() {
        System.out.println("\n=== Testing Articulation Points ===");
        
        // Create a graph with articulation points
        Node node1 = new Node(1);
        Node node2 = new Node(2);
        Node node3 = new Node(3);
        Node node4 = new Node(4);
        Node node5 = new Node(5);
        
        node1.addNeighbor(node2);
        node2.addNeighbor(node1);
        
        node2.addNeighbor(node3);
        node3.addNeighbor(node2);
        
        node3.addNeighbor(node4);
        node4.addNeighbor(node3);
        
        node4.addNeighbor(node5);
        node5.addNeighbor(node4);
        
        // Node 2, 3, and 4 are articulation points
        
        Node[] allNodes = {node1, node2, node3, node4, node5};
        
        DFS dfs = new DFS(null); // Start node doesn't matter for this test
        
        // Test finding articulation points
        Node[] articulationPoints = dfs.findArticulationPoints(allNodes);
        
        if (articulationPoints.length == 0) {
            System.out.println("FAIL: Articulation points returned empty array");
        } else {
            System.out.println("Number of articulation points: " + articulationPoints.length);
            
            // Check if the number of articulation points is correct (should be 3)
            if (articulationPoints.length == 3) {
                System.out.println("PASS: Found 3 articulation points");
            } else {
                System.out.println("FAIL: Did not find 3 articulation points");
            }
            
            // Print the articulation points
            System.out.print("Articulation points: ");
            for (Node node : articulationPoints) {
                System.out.print(node.getValue() + " ");
            }
            System.out.println();
            
            // Check if nodes 2, 3, and 4 are articulation points
            boolean found2 = false;
            boolean found3 = false;
            boolean found4 = false;
            
            for (Node node : articulationPoints) {
                if (node.getValue() == 2) found2 = true;
                if (node.getValue() == 3) found3 = true;
                if (node.getValue() == 4) found4 = true;
            }
            
            if (found2 && found3 && found4) {
                System.out.println("PASS: Found nodes 2, 3, and 4 as articulation points");
            } else {
                System.out.println("FAIL: Did not find nodes 2, 3, and 4 as articulation points");
            }
        }
    }
}
