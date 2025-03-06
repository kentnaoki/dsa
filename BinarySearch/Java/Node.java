package BinarySearch.Java;

/**
 * Node class for the Binary Search Tree.
 * Each node contains a value and references to left and right child nodes.
 */
public class Node {
    private int value;
    private Node left;
    private Node right;

    /**
     * Constructor to create a new node with the given value.
     * 
     * @param value The value to be stored in the node
     */
    public Node(int value) {
        this.value = value;
        this.left = null;
        this.right = null;
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
     * Get the left child of this node.
     * 
     * @return The left child node
     */
    public Node getLeft() {
        return left;
    }

    /**
     * Set the left child of this node.
     * 
     * @param left The new left child node
     */
    public void setLeft(Node left) {
        this.left = left;
    }

    /**
     * Get the right child of this node.
     * 
     * @return The right child node
     */
    public Node getRight() {
        return right;
    }

    /**
     * Set the right child of this node.
     * 
     * @param right The new right child node
     */
    public void setRight(Node right) {
        this.right = right;
    }
}
