package BFS.Java;

/**
 * Test class for the Breadth-First Search implementation.
 * This class provides methods to test various operations of the BFS algorithm.
 */
public class BFSTest {
    
    /**
     * Main method to run the tests.
     * 
     * @param args Command line arguments (not used)
     */
    public static void main(String[] args) {
        System.out.println("Running Breadth-First Search Tests...");
        
        testTraversal();
        testShortestPath();
        testHasPath();
        testConnectedComponents();
        testLevels();
        testBipartite();
        
        System.out.println("All tests completed.");
    }
    
    /**
     * Test the BFS traversal operation.
     */
    private static void testTraversal() {
        System.out.println("\n=== Testing BFS Traversal ===");
        
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
        
        BFS bfs = new BFS(node1);
        
        // Test traversal
        System.out.println("BFS Traversal (expected: 1, 2, 3, 4, 5):");
        Node[] traversalResult = bfs.traverse();
        
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
            
            // Check if the second level nodes (2 and 3) come before the third level nodes (4 and 5)
            boolean level2BeforeLevel3 = false;
            for (int i = 0; i < traversalResult.length; i++) {
                if (traversalResult[i].getValue() == 2 || traversalResult[i].getValue() == 3) {
                    for (int j = i + 1; j < traversalResult.length; j++) {
                        if (traversalResult[j].getValue() == 4 || traversalResult[j].getValue() == 5) {
                            level2BeforeLevel3 = true;
                            break;
                        }
                    }
                    break;
                }
            }
            
            if (level2BeforeLevel3) {
                System.out.println("PASS: Level 2 nodes come before level 3 nodes");
            } else {
                System.out.println("FAIL: Level 2 nodes do not come before level 3 nodes");
            }
        }
    }
    
    /**
     * Test the shortest path operation.
     */
    private static void testShortestPath() {
        System.out.println("\n=== Testing Shortest Path ===");
        
        // Create a graph with multiple paths
        Node node1 = new Node(1);
        Node node2 = new Node(2);
        Node node3 = new Node(3);
        Node node4 = new Node(4);
        Node node5 = new Node(5);
        Node node6 = new Node(6);
        
        node1.addNeighbor(node2);
        node1.addNeighbor(node3);
        node2.addNeighbor(node4);
        node3.addNeighbor(node5);
        node4.addNeighbor(node6);
        node5.addNeighbor(node6);
        
        BFS bfs = new BFS(node1);
        
        // Test shortest path to node 6
        System.out.println("Shortest path from 1 to 6 (expected: 1, 2, 4, 6 or 1, 3, 5, 6):");
        Node[] pathResult = bfs.findShortestPath(6);
        
        if (pathResult.length == 0) {
            System.out.println("FAIL: Shortest path returned empty array");
        } else {
            System.out.print("Path result: ");
            for (Node node : pathResult) {
                System.out.print(node.getValue() + " ");
            }
            System.out.println();
            
            // Check if the path starts with the start node and ends with the target node
            if (pathResult[0].getValue() == 1 && pathResult[pathResult.length - 1].getValue() == 6) {
                System.out.println("PASS: Path starts with 1 and ends with 6");
            } else {
                System.out.println("FAIL: Path does not start with 1 or does not end with 6");
            }
            
            // Check if the path length is correct (should be 4)
            if (pathResult.length == 4) {
                System.out.println("PASS: Path length is 4");
            } else {
                System.out.println("FAIL: Path length is not 4");
            }
        }
        
        // Test shortest path to a non-existent node
        System.out.println("\nShortest path from 1 to 7 (expected: empty path):");
        Node[] nonExistentPath = bfs.findShortestPath(7);
        
        if (nonExistentPath.length == 0) {
            System.out.println("PASS: Shortest path to non-existent node returned empty array");
        } else {
            System.out.println("FAIL: Shortest path to non-existent node did not return empty array");
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
        
        BFS bfs = new BFS(node1);
        
        // Test path to existing nodes
        if (bfs.hasPath(4)) {
            System.out.println("PASS: Found path to node 4");
        } else {
            System.out.println("FAIL: Could not find path to node 4");
        }
        
        // Test path to non-existent node
        if (!bfs.hasPath(5)) {
            System.out.println("PASS: Did not find path to node 5");
        } else {
            System.out.println("FAIL: Found path to node 5, but it should not be reachable");
        }
    }
    
    /**
     * Test the findConnectedComponents operation.
     */
    private static void testConnectedComponents() {
        System.out.println("\n=== Testing Connected Components ===");
        
        // Create a graph with multiple components
        Node node1 = new Node(1);
        Node node2 = new Node(2);
        Node node3 = new Node(3);
        Node node4 = new Node(4);
        Node node5 = new Node(5);
        Node node6 = new Node(6);
        
        node1.addNeighbor(node2);
        node2.addNeighbor(node1);
        
        node3.addNeighbor(node4);
        node4.addNeighbor(node3);
        
        node5.addNeighbor(node6);
        node6.addNeighbor(node5);
        
        Node[] allNodes = {node1, node2, node3, node4, node5, node6};
        
        BFS bfs = new BFS(null); // Start node doesn't matter for this test
        
        // Test finding connected components
        Node[][] components = bfs.findConnectedComponents(allNodes);
        
        if (components.length == 0) {
            System.out.println("FAIL: Connected components returned empty array");
        } else {
            System.out.println("Number of connected components: " + components.length);
            
            // Check if the number of components is correct (should be 3)
            if (components.length == 3) {
                System.out.println("PASS: Found 3 connected components");
            } else {
                System.out.println("FAIL: Did not find 3 connected components");
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
     * Test the findLevels operation.
     */
    private static void testLevels() {
        System.out.println("\n=== Testing Levels ===");
        
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
        
        BFS bfs = new BFS(node1);
        
        // Test finding levels
        int[] levels = bfs.findLevels();
        
        if (levels.length == 0) {
            System.out.println("FAIL: Levels returned empty array");
        } else {
            System.out.println("Levels array length: " + levels.length);
            
            // Check if the number of levels is correct (should be 5 nodes)
            if (levels.length == 5) {
                System.out.println("PASS: Found levels for 5 nodes");
            } else {
                System.out.println("FAIL: Did not find levels for 5 nodes");
            }
            
            // Print the levels
            System.out.print("Levels: ");
            for (int level : levels) {
                System.out.print(level + " ");
            }
            System.out.println();
        }
    }
    
    /**
     * Test the isBipartite operation.
     */
    private static void testBipartite() {
        System.out.println("\n=== Testing Bipartite ===");
        
        // Create a bipartite graph (e.g., a tree)
        Node node1 = new Node(1);
        Node node2 = new Node(2);
        Node node3 = new Node(3);
        Node node4 = new Node(4);
        Node node5 = new Node(5);
        
        node1.addNeighbor(node2);
        node2.addNeighbor(node1);
        
        node1.addNeighbor(node3);
        node3.addNeighbor(node1);
        
        node2.addNeighbor(node4);
        node4.addNeighbor(node2);
        
        node3.addNeighbor(node5);
        node5.addNeighbor(node3);
        
        Node[] bipartiteNodes = {node1, node2, node3, node4, node5};
        
        BFS bfs = new BFS(null); // Start node doesn't matter for this test
        
        // Test if the graph is bipartite
        if (bfs.isBipartite(bipartiteNodes)) {
            System.out.println("PASS: Correctly identified bipartite graph");
        } else {
            System.out.println("FAIL: Did not correctly identify bipartite graph");
        }
        
        // Create a non-bipartite graph (e.g., a triangle)
        Node nodeA = new Node(1);
        Node nodeB = new Node(2);
        Node nodeC = new Node(3);
        
        nodeA.addNeighbor(nodeB);
        nodeB.addNeighbor(nodeA);
        
        nodeB.addNeighbor(nodeC);
        nodeC.addNeighbor(nodeB);
        
        nodeC.addNeighbor(nodeA);
        nodeA.addNeighbor(nodeC);
        
        Node[] nonBipartiteNodes = {nodeA, nodeB, nodeC};
        
        // Test if the graph is bipartite
        if (!bfs.isBipartite(nonBipartiteNodes)) {
            System.out.println("PASS: Correctly identified non-bipartite graph");
        } else {
            System.out.println("FAIL: Did not correctly identify non-bipartite graph");
        }
    }
}
