package BFS.Java;

import java.util.LinkedList;
import java.util.Queue;
import java.util.HashSet;
import java.util.Set;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Complete implementation of Breadth-First Search.
 * This class provides a reference solution for the BFS blueprint.
 * You can use this as a guide if you get stuck with your implementation.
 */
public class BFSSolution {
    private Node startNode;

    /**
     * Constructor to create a BFS instance with a start node.
     * 
     * @param startNode The starting node for BFS traversal
     */
    public BFSSolution(Node startNode) {
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
     * Perform a BFS traversal starting from the start node.
     * 
     * @return An array of nodes in BFS traversal order
     */
    public Node[] traverse() {
        if (startNode == null) {
            return new Node[0];
        }

        List<Node> result = new ArrayList<>();
        Queue<Node> queue = new LinkedList<>();
        Set<Node> visited = new HashSet<>();

        queue.add(startNode);
        visited.add(startNode);

        while (!queue.isEmpty()) {
            Node current = queue.poll();
            result.add(current);

            for (Node neighbor : current.getNeighbors()) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    queue.add(neighbor);
                }
            }
        }

        return result.toArray(new Node[0]);
    }

    /**
     * Find the shortest path from the start node to the target node.
     * 
     * @param targetValue The value of the target node
     * @return An array of nodes representing the shortest path, or an empty array if no path exists
     */
    public Node[] findShortestPath(int targetValue) {
        if (startNode == null) {
            return new Node[0];
        }

        Queue<Node> queue = new LinkedList<>();
        Map<Node, Node> parentMap = new HashMap<>();
        Set<Node> visited = new HashSet<>();

        queue.add(startNode);
        visited.add(startNode);
        parentMap.put(startNode, null);

        Node targetNode = null;
        boolean found = false;

        while (!queue.isEmpty() && !found) {
            Node current = queue.poll();

            if (current.getValue() == targetValue) {
                targetNode = current;
                found = true;
                break;
            }

            for (Node neighbor : current.getNeighbors()) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    queue.add(neighbor);
                    parentMap.put(neighbor, current);
                }
            }
        }

        if (!found) {
            return new Node[0];
        }

        // Reconstruct the path
        List<Node> path = new ArrayList<>();
        Node current = targetNode;
        while (current != null) {
            path.add(0, current);
            current = parentMap.get(current);
        }

        return path.toArray(new Node[0]);
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

        Queue<Node> queue = new LinkedList<>();
        Set<Node> visited = new HashSet<>();

        queue.add(startNode);
        visited.add(startNode);

        while (!queue.isEmpty()) {
            Node current = queue.poll();

            if (current.getValue() == targetValue) {
                return true;
            }

            for (Node neighbor : current.getNeighbors()) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    queue.add(neighbor);
                }
            }
        }

        return false;
    }

    /**
     * Find all connected components in the graph.
     * 
     * @param allNodes An array of all nodes in the graph
     * @return An array of arrays, where each inner array represents a connected component
     */
    public Node[][] findConnectedComponents(Node[] allNodes) {
        if (allNodes == null || allNodes.length == 0) {
            return new Node[0][0];
        }

        List<List<Node>> components = new ArrayList<>();
        Set<Node> visited = new HashSet<>();

        for (Node node : allNodes) {
            if (!visited.contains(node)) {
                List<Node> component = new ArrayList<>();
                Queue<Node> queue = new LinkedList<>();

                queue.add(node);
                visited.add(node);

                while (!queue.isEmpty()) {
                    Node current = queue.poll();
                    component.add(current);

                    for (Node neighbor : current.getNeighbors()) {
                        if (!visited.contains(neighbor)) {
                            visited.add(neighbor);
                            queue.add(neighbor);
                        }
                    }
                }

                components.add(component);
            }
        }

        Node[][] result = new Node[components.size()][];
        for (int i = 0; i < components.size(); i++) {
            result[i] = components.get(i).toArray(new Node[0]);
        }

        return result;
    }

    /**
     * Find the level (distance) of each node from the start node.
     * 
     * @return A map of nodes to their levels
     */
    public int[] findLevels() {
        if (startNode == null) {
            return new int[0];
        }

        Map<Node, Integer> levelMap = new HashMap<>();
        Queue<Node> queue = new LinkedList<>();
        Set<Node> visited = new HashSet<>();

        queue.add(startNode);
        visited.add(startNode);
        levelMap.put(startNode, 0);

        while (!queue.isEmpty()) {
            Node current = queue.poll();
            int currentLevel = levelMap.get(current);

            for (Node neighbor : current.getNeighbors()) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    queue.add(neighbor);
                    levelMap.put(neighbor, currentLevel + 1);
                }
            }
        }

        // Convert map to array
        int[] levels = new int[visited.size()];
        int i = 0;
        for (Node node : visited) {
            levels[i++] = levelMap.get(node);
        }

        return levels;
    }

    /**
     * Check if the graph is bipartite (can be divided into two sets
     * such that no two nodes within the same set are adjacent).
     * 
     * @param allNodes An array of all nodes in the graph
     * @return true if the graph is bipartite, false otherwise
     */
    public boolean isBipartite(Node[] allNodes) {
        if (allNodes == null || allNodes.length == 0) {
            return true;
        }

        Map<Node, Integer> colorMap = new HashMap<>();
        
        for (Node node : allNodes) {
            if (!colorMap.containsKey(node)) {
                Queue<Node> queue = new LinkedList<>();
                queue.add(node);
                colorMap.put(node, 0); // Color the first node with 0

                while (!queue.isEmpty()) {
                    Node current = queue.poll();
                    int currentColor = colorMap.get(current);
                    int neighborColor = 1 - currentColor; // Flip between 0 and 1

                    for (Node neighbor : current.getNeighbors()) {
                        if (!colorMap.containsKey(neighbor)) {
                            colorMap.put(neighbor, neighborColor);
                            queue.add(neighbor);
                        } else if (colorMap.get(neighbor) != neighborColor) {
                            return false; // Not bipartite
                        }
                    }
                }
            }
        }

        return true;
    }
}
