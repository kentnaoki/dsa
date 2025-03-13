package DFS.Java;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.Stack;

/**
 * Depth-First Search implementation.
 * This class provides a blueprint for implementing DFS with
 * various operations like traversal, path finding, and cycle detection.
 */
public class DFS {
    private Node startNode;

    /**
     * Constructor to create a DFS instance with a start node.
     * 
     * @param startNode The starting node for DFS traversal
     */
    public DFS(Node startNode) {
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
        // TODO: Implement this method
        // Use a stack or recursion to perform DFS traversal
        // Return an array of nodes in DFS traversal order
        if (startNode == null) {
            return new Node[0];
        }
        List<Node> visited = new ArrayList<>();
        visited.add(startNode);
        return traverse(startNode, visited);
    }

    private Node[] traverse(Node node, List<Node> visited) {
        Node[] neighborNodes = node.getNeighbors();
        for (Node neighborNode : neighborNodes) {
            if (!visited.contains(neighborNode)) {
                visited.add(neighborNode);
                traverse(neighborNode, visited);
            }
        }
        return visited.toArray(new Node[visited.size()]);
    }

    /**
     * Find a path from the start node to the target node.
     * 
     * @param targetValue The value of the target node
     * @return An array of nodes representing a path, or an empty array if no path exists
     */
    public Node[] findPath(int targetValue) {
        // TODO: Implement this method
        // Use DFS to find a path to the target
        // Return an array of nodes representing the path
        Set<Node> visited = new HashSet<>();
        List<Node> path = new ArrayList<>();

        if (startNode != null) {
            visited.add(startNode);
            if (findPath(startNode, visited, path, targetValue)) {
                return path.toArray(new Node[path.size()]);
            }
        }

        return new Node[0];
    }

    private boolean findPath(Node node, Set<Node> visited, List<Node> tempList, int targetValue) {
        tempList.add(node);

        if (node.getValue() == targetValue) {
            return true;
        }

        Node[] neighborNodes = node.getNeighbors();

        for (Node neighborNode : neighborNodes) {
            if (!visited.contains(neighborNode)) {
                visited.add(neighborNode);
                if (findPath(neighborNode, visited, tempList, targetValue)) {
                    return true;
                }
            }
        }

        tempList.remove(node);
        return false;
    }

    /**
     * Check if there is a path from the start node to a node with the target value.
     * 
     * @param targetValue The value to search for
     * @return true if a path exists, false otherwise
     */
    public boolean hasPath(int targetValue) {
        // TODO: Implement this method
        // Use DFS to check if there is a path to the target
        return hasPath(startNode, targetValue);
    }

    private boolean hasPath(Node node, int targetValue) {
        if (node == null) {
            return false;
        }

        if (node.getValue() == targetValue) {
            return true;
        }

        for (Node neighborNode : node.getNeighbors()) {
            return hasPath(neighborNode, targetValue);
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
        // TODO: Implement this method
        // Use DFS to detect cycles in the graph
        Set<Node> visited = new HashSet<>();
        Set<Node> recursionStack = new HashSet<>();

        for (Node node : allNodes) {
            if (!visited.contains(node)) {
                if (hasCycle(node, visited, recursionStack)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean hasCycle(Node node, Set<Node> visited, Set<Node> recursionStack) {
        visited.add(node);
        recursionStack.add(node);

        for (Node neighbor : node.getNeighbors()) {
            if (!visited.contains(neighbor)) {
                if (hasCycle(neighbor, visited, recursionStack)) {
                    return true;
                }
            } else if (recursionStack.contains(neighbor)) {
                return true;
            }
        }

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
        // TODO: Implement this method
        // Use DFS to perform a topological sort
        // Return an array of nodes in topological order
        if (hasCycle(allNodes)) {
            return new Node[0];
        }

        Set<Node> visited = new HashSet<>();
        Stack<Node> stack = new Stack<>();

        for (Node node : allNodes) {
            if (!visited.contains(node)) {
                topologicalSort(node, visited, stack);
            }
        }

        Node[] array = new Node[stack.size()];

        for (int i = 0; i < array.length; i++) {
            array[i] = stack.pop();
        }
        return array;
    }

    private void topologicalSort(Node node, Set<Node> visited, Stack<Node> stack) {
        visited.add(node);

        for (Node neighbor : node.getNeighbors()) {
            if (!visited.contains(neighbor)) {
                topologicalSort(neighbor, visited, stack);
            }
        }
        stack.push(node);

    }

    /**
     * Find all strongly connected components in the graph.
     * 
     * @param allNodes An array of all nodes in the graph
     * @return An array of arrays, where each inner array represents a strongly connected component
     */
    public Node[][] findStronglyConnectedComponents(Node[] allNodes) {
        // TODO: Implement this method
        // Use Kosaraju's algorithm or Tarjan's algorithm to find strongly connected components
        // Return an array of arrays, where each inner array represents a strongly connected component
        return new Node[0][0];
    }

    /**
     * Find the articulation points (cut vertices) in the graph.
     * 
     * @param allNodes An array of all nodes in the graph
     * @return An array of nodes that are articulation points
     */
    public Node[] findArticulationPoints(Node[] allNodes) {
        // TODO: Implement this method
        // Use DFS to find articulation points
        // Return an array of nodes that are articulation points
        return new Node[0];
    }
}
