package BFS.Java;

import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

/**
 * Breadth-First Search implementation.
 * This class provides a blueprint for implementing BFS with
 * various operations like traversal, path finding, and connected components.
 */
public class BFS {
    private Node startNode;

    /**
     * Constructor to create a BFS instance with a start node.
     * 
     * @param startNode The starting node for BFS traversal
     */
    public BFS(Node startNode) {
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
        // TODO: Implement this method
        // Use a queue to perform BFS traversal
        // Return an array of nodes in BFS traversal order
        Queue<Node> queue = new LinkedList<>();
        List<Node> visited = new ArrayList<>();

        if (startNode == null) {
            return new Node[0];
        }
        queue.offer(startNode);
        visited.add(startNode);
        while (!queue.isEmpty()) {
            Node node = queue.poll();

            for (Node neighbor : node.getNeighbors()) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    queue.offer(neighbor);
                }
            }
        }
        
        return visited.toArray(new Node[0]);
    }


    /**
     * Find the shortest path from the start node to the target node.
     * 
     * @param targetValue The value of the target node
     * @return An array of nodes representing the shortest path, or an empty array if no path exists
     */
    public Node[] findShortestPath(int targetValue) {
        // TODO: Implement this method
        // Use BFS to find the shortest path
        // Return an array of nodes representing the path
        if (startNode == null) {
            return new Node[0];
        }
        
        Queue<Node> queue = new LinkedList<>();
        List<Node> visited = new ArrayList<>();
        Map<Node, Node> parentsMap = new HashMap<>();
        
        queue.offer(startNode);
        visited.add(startNode);
        parentsMap.put(startNode, null);

        Node targetNode = null;
        boolean found = false;

        while (!queue.isEmpty()) {
            Node current = queue.poll();

            if (current.getValue() == targetValue) {
                targetNode = current;
                found = true;
                break;
            }

            for (Node neighborNode : current.getNeighbors()) {
                if (!visited.contains(neighborNode)) {
                    queue.offer(neighborNode);
                    visited.add(neighborNode);
                    parentsMap.put(neighborNode, current);
                }
            }
        }

        if (!found) {
            return new Node[0];
        }

        List<Node> path = new ArrayList<>();

        Node current = targetNode;
        while (current != null) {
            path.add(0, current);
            current = parentsMap.get(current);
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
        // TODO: Implement this method
        // Use BFS to check if there is a path to the target
        Queue<Node> queue = new LinkedList<>();
        List<Node> visited = new ArrayList<>();

        queue.offer(startNode);
        visited.add(startNode);

        while (!queue.isEmpty()) {
            Node current = queue.poll();

            if (current.getValue() == targetValue) {
                return true;
            }

            for (Node neighborNode : current.getNeighbors()) {
                if (!visited.contains(neighborNode)) {
                    queue.offer(neighborNode);
                    visited.add(neighborNode);
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
        // TODO: Implement this method
        // Use BFS to find all connected components
        // Return an array of arrays, where each inner array represents a connected component
        return new Node[0][0];
    }

    /**
     * Find the level (distance) of each node from the start node.
     * 
     * @return An array of integers representing the level of each node
     */
    public int[] findLevels() {
        // TODO: Implement this method
        // Use BFS to find the level of each node
        // Return an array of integers representing the level of each node
        if (startNode == null) {
            return new int[0];
        }

        Queue<Node> queue = new LinkedList<>();
        List<Node> visited = new ArrayList<>();
        List<Integer> levels = new ArrayList<>();

        queue.offer(startNode);
        visited.add(startNode);
        int level = 0;

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            for (int i = 0; i < levelSize; i++) {

                Node current = queue.poll();
                levels.add(level);
                for (Node neighborNode : current.getNeighbors()) {
                    if (!visited.contains(neighborNode)) {
                        queue.offer(neighborNode);
                        visited.add(neighborNode);
                    }
                }
                
            } 
            level++;
        }

        return levels.stream().mapToInt(Integer::valueOf).toArray();
    }

    /**
     * Check if the graph is bipartite (can be divided into two sets
     * such that no two nodes within the same set are adjacent).
     * 
     * @param allNodes An array of all nodes in the graph
     * @return true if the graph is bipartite, false otherwise
     */
    public boolean isBipartite(Node[] allNodes) {
        // TODO: Implement this method
        // Use BFS to check if the graph is bipartite
        return false;
    }
}
