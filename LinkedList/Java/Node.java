package LinkedList.Java;

/**
 * Node class for the LinkedList implementation.
 * Each node contains a value and a reference to the next node.
 */
public class Node {
    private int value;
    private Node next;

    /**
     * Constructor to create a new node with the given value.
     * 
     * @param value The value to be stored in the node
     */
    public Node(int value) {
        this.value = value;
        this.next = null;
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
     * Get the next node.
     * 
     * @return The next node
     */
    public Node getNext() {
        return next;
    }

    /**
     * Set the next node.
     * 
     * @param next The new next node
     */
    public void setNext(Node next) {
        this.next = next;
    }
}
