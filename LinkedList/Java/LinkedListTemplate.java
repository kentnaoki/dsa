package LinkedList.Java;

/**
 * LinkedList implementation.
 * This class provides a blueprint for implementing a singly linked list with
 * various operations like insert, delete, search, and traversal.
 */
public class LinkedListTemplate {
    private Node head;
    private int size;

    /**
     * Constructor to create an empty LinkedList.
     */
    public LinkedListTemplate() {
        this.head = null;
        this.size = 0;
    }

    /**
     * Get the head node of the list.
     * 
     * @return The head node
     */
    public Node getHead() {
        return head;
    }

    /**
     * Get the size of the list.
     * 
     * @return The number of nodes in the list
     */
    public int getSize() {
        return size;
    }

    /**
     * Check if the list is empty.
     * 
     * @return true if the list is empty, false otherwise
     */
    public boolean isEmpty() {
        return head == null;
    }

    /**
     * Insert a new value at the beginning of the list.
     * 
     * @param value The value to be inserted
     */
    public void insertAtBeginning(int value) {
        // TODO: Implement this method
        // Create a new node with the given value
        // Set the new node's next to the current head
        // Update the head to the new node
        // Increment the size
    }

    /**
     * Insert a new value at the end of the list.
     * 
     * @param value The value to be inserted
     */
    public void insertAtEnd(int value) {
        // TODO: Implement this method
        // Create a new node with the given value
        // If the list is empty, set the head to the new node
        // Otherwise, traverse to the end of the list and set the last node's next to the new node
        // Increment the size
    }

    /**
     * Insert a new value at the specified position in the list.
     * 
     * @param value The value to be inserted
     * @param position The position at which to insert the value (0-based index)
     * @return true if the insertion was successful, false otherwise
     */
    public boolean insertAtPosition(int value, int position) {
        // TODO: Implement this method
        // Check if the position is valid (0 <= position <= size)
        // If position is 0, call insertAtBeginning
        // If position is size, call insertAtEnd
        // Otherwise, traverse to the node at position-1 and insert the new node after it
        // Increment the size
        // Return true if the insertion was successful, false otherwise
        return false;
    }

    /**
     * Delete the first occurrence of the specified value from the list.
     * 
     * @param value The value to be deleted
     * @return true if the value was found and deleted, false otherwise
     */
    public boolean delete(int value) {
        // TODO: Implement this method
        // If the list is empty, return false
        // If the head node has the value, update the head to the next node
        // Otherwise, traverse the list to find the node with the value and remove it
        // Decrement the size if a node was deleted
        // Return true if the value was found and deleted, false otherwise
        return false;
    }

    /**
     * Delete the node at the specified position in the list.
     * 
     * @param position The position of the node to be deleted (0-based index)
     * @return true if the deletion was successful, false otherwise
     */
    public boolean deleteAtPosition(int position) {
        // TODO: Implement this method
        // Check if the position is valid (0 <= position < size)
        // If position is 0, update the head to the next node
        // Otherwise, traverse to the node at position-1 and update its next pointer
        // Decrement the size
        // Return true if the deletion was successful, false otherwise
        return false;
    }

    /**
     * Search for a value in the list.
     * 
     * @param value The value to search for
     * @return true if the value is found, false otherwise
     */
    public boolean search(int value) {
        // TODO: Implement this method
        // Traverse the list and check if any node has the specified value
        // Return true if the value is found, false otherwise
        return false;
    }

    /**
     * Get the value at the specified position in the list.
     * 
     * @param position The position of the node (0-based index)
     * @return The value at the specified position, or Integer.MIN_VALUE if the position is invalid
     */
    public int getValueAtPosition(int position) {
        // TODO: Implement this method
        // Check if the position is valid (0 <= position < size)
        // Traverse to the node at the specified position and return its value
        // Return Integer.MIN_VALUE if the position is invalid
        return Integer.MIN_VALUE;
    }

    /**
     * Reverse the list.
     */
    public void reverse() {
        // TODO: Implement this method
        // Reverse the list by changing the next pointers of each node
    }

    /**
     * Check if the list has a cycle.
     * 
     * @return true if the list has a cycle, false otherwise
     */
    public boolean hasCycle() {
        // TODO: Implement this method
        // Use Floyd's Cycle-Finding Algorithm (Tortoise and Hare)
        // Return true if a cycle is detected, false otherwise
        return false;
    }

    /**
     * Find the middle node of the list.
     * 
     * @return The middle node, or null if the list is empty
     */
    public Node findMiddle() {
        // TODO: Implement this method
        // Use the slow and fast pointer technique to find the middle node
        // Return the middle node, or null if the list is empty
        return null;
    }

    /**
     * Print the list.
     */
    public void printList() {
        Node current = head;
        System.out.print("List: ");
        while (current != null) {
            System.out.print(current.getValue() + " ");
            current = current.getNext();
        }
        System.out.println();
    }
}
