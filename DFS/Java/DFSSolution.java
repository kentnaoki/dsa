package DFS.Java;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.Stack;

/**
 * Complete implementation of Depth-First Search.
 * This class provides a reference solution for the DFS blueprint.
 * You can use this as a guide if you get stuck with your implementation.
 */
public class DFSSolution {
    private Node startNode;

    /**
     * Constructor to create a DFS instance with a start node.
     * 
     * @param startNode The starting node for DFS traversal
     */
    public DFSSolution(Node startNode) {
        this.startNode = startNode;
    }

    /**
     * Get the start node.
     * 
     * @return The start node
     */
    public Node getStartNode() {
        return startNode;
    }

    /**
     * Set the start node.
     * 
     * @param startNode The new start node
     */
    public void setStartNode(Node startNode) {
        this.startNode = startNode;
    }

    /**
     * Perform a DFS traversal starting from the start node.
     * 
     * @return An array of nodes in DFS traversal order
     */
    public Node[] traverse() {
        if (startNode == null) {
            return new Node[0];
        }

        List<Node> result = new ArrayList<>();
        Set<Node> visited = new HashSet<>();
        
        // Call recursive helper function
        dfsTraversal(startNode, visited, result);
        
        return result.toArray(new Node[0]);
    }
    
    /**
     * Helper method for recursive DFS traversal.
     * 
     * @param node The current node
     * @param visited Set of visited nodes
     * @param result List to store the traversal result
     */
    private void dfsTraversal(Node node, Set<Node> visited, List<Node> result) {
        // Mark the current node as visited and add to result
        visited.add(node);
        result.add(node);
        
        // Recur for all the neighbors
        for (Node neighbor : node.getNeighbors()) {
            if (!visited.contains(neighbor)) {
                dfsTraversal(neighbor, visited, result);
            }
        }
    }

    /**
     * Find a path from the start node to the target node.
     * 
     * @param targetValue The value of the target node
     * @return An array of nodes representing a path, or an empty array if no path exists
     */
    public Node[] findPath(int targetValue) {
        if (startNode == null) {
            return new Node[0];
        }

        Set<Node> visited = new HashSet<>();
        List<Node> path = new ArrayList<>();
        
        if (dfsPath(startNode, targetValue, visited, path)) {
            return path.toArray(new Node[0]);
        }
        
        return new Node[0];
    }
    
    /**
     * Helper method for recursive DFS path finding.
     * 
     * @param node The current node
     * @param targetValue The value to search for
     * @param visited Set of visited nodes
     * @param path List to store the path
     * @return true if a path is found, false otherwise
     */
    private boolean dfsPath(Node node, int targetValue, Set<Node> visited, List<Node> path) {
        // Mark the current node as visited and add to path
        visited.add(node);
        path.add(node);
        
        // If current node has the target value, return true
        if (node.getValue() == targetValue) {
            return true;
        }
        
        // Recur for all the neighbors
        for (Node neighbor : node.getNeighbors()) {
            if (!visited.contains(neighbor)) {
                if (dfsPath(neighbor, targetValue, visited, path)) {
                    return true;
                }
            }
        }
        
        // If no path is found, remove the current node from path
        path.remove(path.size() - 1);
        return false;
    }

    /**
     * Check if there is a path from the start node to a node with the target value.
     * 
     * @param targetValue The value to search for
     * @return true if a path exists, false otherwise
     */
    public boolean hasPath(int targetValue) {
        if (startNode == null) {
            return false;
        }

        Set<Node> visited = new HashSet<>();
        return dfsHasPath(startNode, targetValue, visited);
    }
    
    /**
     * Helper method for recursive DFS path checking.
     * 
     * @param node The current node
     * @param targetValue The value to search for
     * @param visited Set of visited nodes
     * @return true if a path is found, false otherwise
     */
    private boolean dfsHasPath(Node node, int targetValue, Set<Node> visited) {
        // Mark the current node as visited
        visited.add(node);
        
        // If current node has the target value, return true
        if (node.getValue() == targetValue) {
            return true;
        }
        
        // Recur for all the neighbors
        for (Node neighbor : node.getNeighbors()) {
            if (!visited.contains(neighbor)) {
                if (dfsHasPath(neighbor, targetValue, visited)) {
                    return true;
                }
            }
        }
        
        return false;
    }

    /**
     * Detect if there is a cycle in the graph.
     * 
     * @param allNodes An array of all nodes in the graph
     * @return true if a cycle is detected, false otherwise
     */
    public boolean hasCycle(Node[] allNodes) {
        if (allNodes == null || allNodes.length == 0) {
            return false;
        }

        Set<Node> visited = new HashSet<>();
        Set<Node> recursionStack = new HashSet<>();
        
        for (Node node : allNodes) {
            if (!visited.contains(node)) {
                if (dfsHasCycle(node, visited, recursionStack)) {
                    return true;
                }
            }
        }
        
        return false;
    }
    
    /**
     * Helper method for recursive DFS cycle detection.
     * 
     * @param node The current node
     * @param visited Set of visited nodes
     * @param recursionStack Set of nodes in the current recursion stack
     * @return true if a cycle is detected, false otherwise
     */
    private boolean dfsHasCycle(Node node, Set<Node> visited, Set<Node> recursionStack) {
        // Mark the current node as visited and add to recursion stack
        visited.add(node);
        recursionStack.add(node);
        
        // Recur for all the neighbors
        for (Node neighbor : node.getNeighbors()) {
            // If the neighbor is not visited, recur for it
            if (!visited.contains(neighbor)) {
                if (dfsHasCycle(neighbor, visited, recursionStack)) {
                    return true;
                }
            }
            // If the neighbor is in the recursion stack, there is a cycle
            else if (recursionStack.contains(neighbor)) {
                return true;
            }
        }
        
        // Remove the current node from recursion stack
        recursionStack.remove(node);
        return false;
    }

    /**
     * Perform a topological sort of the graph.
     * 
     * @param allNodes An array of all nodes in the graph
     * @return An array of nodes in topological order, or an empty array if a cycle is detected
     */
    public Node[] topologicalSort(Node[] allNodes) {
        if (allNodes == null || allNodes.length == 0) {
            return new Node[0];
        }

        // Check if the graph has a cycle
        if (hasCycle(allNodes)) {
            return new Node[0];
        }

        Stack<Node> stack = new Stack<>();
        Set<Node> visited = new HashSet<>();
        
        // Call the recursive helper function to store topological sort
        for (Node node : allNodes) {
            if (!visited.contains(node)) {
                dfsTopologicalSort(node, visited, stack);
            }
        }
        
        // Convert stack to array
        Node[] result = new Node[stack.size()];
        for (int i = 0; i < result.length; i++) {
            result[i] = stack.pop();
        }
        
        return result;
    }
    
    /**
     * Helper method for recursive DFS topological sort.
     * 
     * @param node The current node
     * @param visited Set of visited nodes
     * @param stack Stack to store the topological sort
     */
    private void dfsTopologicalSort(Node node, Set<Node> visited, Stack<Node> stack) {
        // Mark the current node as visited
        visited.add(node);
        
        // Recur for all the neighbors
        for (Node neighbor : node.getNeighbors()) {
            if (!visited.contains(neighbor)) {
                dfsTopologicalSort(neighbor, visited, stack);
            }
        }
        
        // Push current node to stack
        stack.push(node);
    }

    /**
     * Find all strongly connected components in the graph.
     * 
     * @param allNodes An array of all nodes in the graph
     * @return An array of arrays, where each inner array represents a strongly connected component
     */
    public Node[][] findStronglyConnectedComponents(Node[] allNodes) {
        if (allNodes == null || allNodes.length == 0) {
            return new Node[0][0];
        }

        // Step 1: Perform DFS and store nodes in order of finishing time
        Stack<Node> stack = new Stack<>();
        Set<Node> visited = new HashSet<>();
        
        for (Node node : allNodes) {
            if (!visited.contains(node)) {
                fillOrder(node, visited, stack);
            }
        }
        
        // Step 2: Create a transpose graph (reverse all edges)
        Map<Node, List<Node>> transpose = new HashMap<>();
        for (Node node : allNodes) {
            transpose.put(node, new ArrayList<>());
        }
        
        for (Node node : allNodes) {
            for (Node neighbor : node.getNeighbors()) {
                transpose.get(neighbor).add(node);
            }
        }
        
        // Step 3: Process nodes in order of finishing time
        visited.clear();
        List<List<Node>> components = new ArrayList<>();
        
        while (!stack.isEmpty()) {
            Node node = stack.pop();
            
            if (!visited.contains(node)) {
                List<Node> component = new ArrayList<>();
                dfsUtil(node, visited, component, transpose);
                components.add(component);
            }
        }
        
        // Convert list of lists to array of arrays
        Node[][] result = new Node[components.size()][];
        for (int i = 0; i < components.size(); i++) {
            result[i] = components.get(i).toArray(new Node[0]);
        }
        
        return result;
    }
    
    /**
     * Helper method to fill the stack with nodes in order of finishing time.
     * 
     * @param node The current node
     * @param visited Set of visited nodes
     * @param stack Stack to store nodes in order of finishing time
     */
    private void fillOrder(Node node, Set<Node> visited, Stack<Node> stack) {
        visited.add(node);
        
        for (Node neighbor : node.getNeighbors()) {
            if (!visited.contains(neighbor)) {
                fillOrder(neighbor, visited, stack);
            }
        }
        
        stack.push(node);
    }
    
    /**
     * Helper method for DFS on the transpose graph.
     * 
     * @param node The current node
     * @param visited Set of visited nodes
     * @param component List to store the current component
     * @param transpose Map representing the transpose graph
     */
    private void dfsUtil(Node node, Set<Node> visited, List<Node> component, Map<Node, List<Node>> transpose) {
        visited.add(node);
        component.add(node);
        
        for (Node neighbor : transpose.get(node)) {
            if (!visited.contains(neighbor)) {
                dfsUtil(neighbor, visited, component, transpose);
            }
        }
    }

    /**
     * Find the articulation points (cut vertices) in the graph.
     * 
     * @param allNodes An array of all nodes in the graph
     * @return An array of nodes that are articulation points
     */
    public Node[] findArticulationPoints(Node[] allNodes) {
        if (allNodes == null || allNodes.length == 0) {
            return new Node[0];
        }

        Set<Node> articulationPoints = new HashSet<>();
        Set<Node> visited = new HashSet<>();
        Map<Node, Integer> disc = new HashMap<>();
        Map<Node, Integer> low = new HashMap<>();
        Map<Node, Node> parent = new HashMap<>();
        
        int time = 0;
        
        for (Node node : allNodes) {
            if (!visited.contains(node)) {
                dfsArticulationPoints(node, visited, disc, low, parent, articulationPoints, time);
            }
        }
        
        return articulationPoints.toArray(new Node[0]);
    }
    
    /**
     * Helper method for finding articulation points using DFS.
     * 
     * @param node The current node
     * @param visited Set of visited nodes
     * @param disc Map of discovery times
     * @param low Map of lowest discovery times
     * @param parent Map of parent nodes
     * @param articulationPoints Set to store articulation points
     * @param time Current time
     */
    private void dfsArticulationPoints(Node node, Set<Node> visited, Map<Node, Integer> disc, Map<Node, Integer> low, Map<Node, Node> parent, Set<Node> articulationPoints, int time) {
        // Count of children in DFS tree
        int children = 0;
        
        // Mark the current node as visited
        visited.add(node);
        
        // Initialize discovery time and low value
        disc.put(node, time);
        low.put(node, time);
        time++;
        
        // Recur for all the neighbors
        for (Node neighbor : node.getNeighbors()) {
            // If neighbor is not visited yet, then make it a child of node in DFS tree and recur for it
            if (!visited.contains(neighbor)) {
                children++;
                parent.put(neighbor, node);
                
                dfsArticulationPoints(neighbor, visited, disc, low, parent, articulationPoints, time);
                
                // Check if the subtree rooted with neighbor has a connection to one of the ancestors of node
                low.put(node, Math.min(low.get(node), low.get(neighbor)));
                
                // node is an articulation point in following cases:
                
                // (1) node is root of DFS tree and has two or more children
                if (parent.get(node) == null && children > 1) {
                    articulationPoints.add(node);
                }
                
                // (2) If node is not root and low value of one of its children is more than or equal to discovery value of node
                if (parent.get(node) != null && low.get(neighbor) >= disc.get(node)) {
                    articulationPoints.add(node);
                }
            }
            // Update low value of node for parent function calls
            else if (neighbor != parent.get(node)) {
                low.put(node, Math.min(low.get(node), disc.get(neighbor)));
            }
        }
    }
}
