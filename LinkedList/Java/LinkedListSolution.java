package LinkedList.Java;

/**
 * Complete implementation of a LinkedList.
 * This class provides a reference solution for the LinkedList blueprint.
 * You can use this as a guide if you get stuck with your implementation.
 */
public class LinkedListSolution {
    private Node head;
    private int size;

    /**
     * Constructor to create an empty LinkedList.
     */
    public LinkedListSolution() {
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
        Node newNode = new Node(value);
        newNode.setNext(head);
        head = newNode;
        size++;
    }

    /**
     * Insert a new value at the end of the list.
     * 
     * @param value The value to be inserted
     */
    public void insertAtEnd(int value) {
        Node newNode = new Node(value);
        
        if (isEmpty()) {
            head = newNode;
        } else {
            Node current = head;
            while (current.getNext() != null) {
                current = current.getNext();
            }
            current.setNext(newNode);
        }
        
        size++;
    }

    /**
     * Insert a new value at the specified position in the list.
     * 
     * @param value The value to be inserted
     * @param position The position at which to insert the value (0-based index)
     * @return true if the insertion was successful, false otherwise
     */
    public boolean insertAtPosition(int value, int position) {
        if (position < 0 || position > size) {
            return false;
        }
        
        if (position == 0) {
            insertAtBeginning(value);
            return true;
        }
        
        if (position == size) {
            insertAtEnd(value);
            return true;
        }
        
        Node newNode = new Node(value);
        Node current = head;
        
        for (int i = 0; i < position - 1; i++) {
            current = current.getNext();
        }
        
        newNode.setNext(current.getNext());
        current.setNext(newNode);
        size++;
        
        return true;
    }

    /**
     * Delete the first occurrence of the specified value from the list.
     * 
     * @param value The value to be deleted
     * @return true if the value was found and deleted, false otherwise
     */
    public boolean delete(int value) {
        if (isEmpty()) {
            return false;
        }
        
        if (head.getValue() == value) {
            head = head.getNext();
            size--;
            return true;
        }
        
        Node current = head;
        while (current.getNext() != null && current.getNext().getValue() != value) {
            current = current.getNext();
        }
        
        if (current.getNext() != null) {
            current.setNext(current.getNext().getNext());
            size--;
            return true;
        }
        
        return false;
    }

    /**
     * Delete the node at the specified position in the list.
     * 
     * @param position The position of the node to be deleted (0-based index)
     * @return true if the deletion was successful, false otherwise
     */
    public boolean deleteAtPosition(int position) {
        if (position < 0 || position >= size || isEmpty()) {
            return false;
        }
        
        if (position == 0) {
            head = head.getNext();
            size--;
            return true;
        }
        
        Node current = head;
        for (int i = 0; i < position - 1; i++) {
            current = current.getNext();
        }
        
        current.setNext(current.getNext().getNext());
        size--;
        
        return true;
    }

    /**
     * Search for a value in the list.
     * 
     * @param value The value to search for
     * @return true if the value is found, false otherwise
     */
    public boolean search(int value) {
        Node current = head;
        
        while (current != null) {
            if (current.getValue() == value) {
                return true;
            }
            current = current.getNext();
        }
        
        return false;
    }

    /**
     * Get the value at the specified position in the list.
     * 
     * @param position The position of the node (0-based index)
     * @return The value at the specified position, or Integer.MIN_VALUE if the position is invalid
     */
    public int getValueAtPosition(int position) {
        if (position < 0 || position >= size || isEmpty()) {
            return Integer.MIN_VALUE;
        }
        
        Node current = head;
        for (int i = 0; i < position; i++) {
            current = current.getNext();
        }
        
        return current.getValue();
    }

    /**
     * Reverse the list.
     */
    public void reverse() {
        if (isEmpty() || size == 1) {
            return;
        }
        
        Node prev = null;
        Node current = head;
        Node next = null;
        
        while (current != null) {
            next = current.getNext();
            current.setNext(prev);
            prev = current;
            current = next;
        }
        
        head = prev;
    }

    /**
     * Check if the list has a cycle.
     * 
     * @return true if the list has a cycle, false otherwise
     */
    public boolean hasCycle() {
        if (isEmpty() || size == 1) {
            return false;
        }
        
        Node slow = head;
        Node fast = head;
        
        while (fast != null && fast.getNext() != null) {
            slow = slow.getNext();
            fast = fast.getNext().getNext();
            
            if (slow == fast) {
                return true;
            }
        }
        
        return false;
    }

    /**
     * Find the middle node of the list.
     * 
     * @return The middle node, or null if the list is empty
     */
    public Node findMiddle() {
        if (isEmpty()) {
            return null;
        }
        
        Node slow = head;
        Node fast = head;
        
        while (fast != null && fast.getNext() != null) {
            slow = slow.getNext();
            fast = fast.getNext().getNext();
        }
        
        return slow;
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
