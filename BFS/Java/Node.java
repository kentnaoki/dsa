package BFS.Java;

/**
 * Node class for the BFS implementation.
 * Each node contains a value and references to its neighbors.
 */
public class Node {
    private int value;
    private Node[] neighbors;

    /**
     * Constructor to create a new node with the given value.
     * 
     * @param value The value to be stored in the node
     */
    public Node(int value) {
        this.value = value;
        this.neighbors = new Node[0];
    }

    /**
     * Get the value stored in this node.
     * 
     * @return The value stored in this node
     */
    public int getValue() {
        return value;
    }

    /**
     * Set the value for this node.
     * 
     * @param value The new value to be stored
     */
    public void setValue(int value) {
        this.value = value;
    }

    /**
     * Get the neighbors of this node.
     * 
     * @return Array of neighbor nodes
     */
    public Node[] getNeighbors() {
        return neighbors;
    }

    /**
     * Set the neighbors of this node.
     * 
     * @param neighbors Array of neighbor nodes
     */
    public void setNeighbors(Node[] neighbors) {
        this.neighbors = neighbors;
    }

    /**
     * Add a neighbor to this node.
     * 
     * @param neighbor The neighbor node to add
     */
    public void addNeighbor(Node neighbor) {
        Node[] newNeighbors = new Node[neighbors.length + 1];
        System.arraycopy(neighbors, 0, newNeighbors, 0, neighbors.length);
        newNeighbors[neighbors.length] = neighbor;
        this.neighbors = newNeighbors;
    }
}
