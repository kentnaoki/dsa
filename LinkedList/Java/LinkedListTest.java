package LinkedList.Java;

/**
 * Test class for the LinkedList implementation.
 * This class provides methods to test various operations of the LinkedList.
 */
public class LinkedListTest {
    
    /**
     * Main method to run the tests.
     * 
     * @param args Command line arguments (not used)
     */
    public static void main(String[] args) {
        System.out.println("Running LinkedList Tests...");
        
        testInsertAtBeginning();
        testInsertAtEnd();
        testInsertAtPosition();
        testDelete();
        testDeleteAtPosition();
        testSearch();
        testGetValueAtPosition();
        testReverse();
        testHasCycle();
        testFindMiddle();
        
        System.out.println("All tests completed.");
    }
    
    /**
     * Test the insertAtBeginning operation.
     */
    private static void testInsertAtBeginning() {
        System.out.println("\n=== Testing Insert at Beginning ===");
        LinkedList list = new LinkedList();
        
        // Insert some values at the beginning
        list.insertAtBeginning(30);
        list.insertAtBeginning(20);
        list.insertAtBeginning(10);
        
        // Print the list
        list.printList();
        
        // Check if the head node has the correct value
        if (list.getHead() != null && list.getHead().getValue() == 10) {
            System.out.println("PASS: Head node has the correct value (10)");
        } else {
            System.out.println("FAIL: Head node does not have the correct value");
        }
        
        // Check if the size is correct
        if (list.getSize() == 3) {
            System.out.println("PASS: List size is correct (3)");
        } else {
            System.out.println("FAIL: List size is not correct");
        }
    }
    
    /**
     * Test the insertAtEnd operation.
     */
    private static void testInsertAtEnd() {
        System.out.println("\n=== Testing Insert at End ===");
        LinkedList list = new LinkedList();
        
        // Insert some values at the end
        list.insertAtEnd(10);
        list.insertAtEnd(20);
        list.insertAtEnd(30);
        
        // Print the list
        list.printList();
        
        // Check if the head node has the correct value
        if (list.getHead() != null && list.getHead().getValue() == 10) {
            System.out.println("PASS: Head node has the correct value (10)");
        } else {
            System.out.println("FAIL: Head node does not have the correct value");
        }
        
        // Check if the last node has the correct value
        Node current = list.getHead();
        while (current != null && current.getNext() != null) {
            current = current.getNext();
        }
        
        if (current != null && current.getValue() == 30) {
            System.out.println("PASS: Last node has the correct value (30)");
        } else {
            System.out.println("FAIL: Last node does not have the correct value");
        }
        
        // Check if the size is correct
        if (list.getSize() == 3) {
            System.out.println("PASS: List size is correct (3)");
        } else {
            System.out.println("FAIL: List size is not correct");
        }
    }
    
    /**
     * Test the insertAtPosition operation.
     */
    private static void testInsertAtPosition() {
        System.out.println("\n=== Testing Insert at Position ===");
        LinkedList list = new LinkedList();
        
        // Insert some values
        list.insertAtEnd(10);
        list.insertAtEnd(30);
        list.insertAtEnd(40);
        
        // Insert at position 1 (between 10 and 30)
        boolean result = list.insertAtPosition(20, 1);
        
        // Print the list
        list.printList();
        
        // Check if the insertion was successful
        if (result) {
            System.out.println("PASS: Insertion at position 1 was successful");
        } else {
            System.out.println("FAIL: Insertion at position 1 was not successful");
        }
        
        // Check if the node at position 1 has the correct value
        if (list.getValueAtPosition(1) == 20) {
            System.out.println("PASS: Node at position 1 has the correct value (20)");
        } else {
            System.out.println("FAIL: Node at position 1 does not have the correct value");
        }
        
        // Check if the size is correct
        if (list.getSize() == 4) {
            System.out.println("PASS: List size is correct (4)");
        } else {
            System.out.println("FAIL: List size is not correct");
        }
        
        // Test insertion at an invalid position
        boolean invalidResult = list.insertAtPosition(50, 10);
        
        if (!invalidResult) {
            System.out.println("PASS: Insertion at invalid position was rejected");
        } else {
            System.out.println("FAIL: Insertion at invalid position was not rejected");
        }
    }
    
    /**
     * Test the delete operation.
     */
    private static void testDelete() {
        System.out.println("\n=== Testing Delete ===");
        LinkedList list = new LinkedList();
        
        // Insert some values
        list.insertAtEnd(10);
        list.insertAtEnd(20);
        list.insertAtEnd(30);
        list.insertAtEnd(40);
        
        // Print the list before deletion
        System.out.println("List before deletion:");
        list.printList();
        
        // Delete a value
        boolean result = list.delete(20);
        
        // Print the list after deletion
        System.out.println("List after deletion of 20:");
        list.printList();
        
        // Check if the deletion was successful
        if (result) {
            System.out.println("PASS: Deletion of 20 was successful");
        } else {
            System.out.println("FAIL: Deletion of 20 was not successful");
        }
        
        // Check if the size is correct
        if (list.getSize() == 3) {
            System.out.println("PASS: List size is correct (3)");
        } else {
            System.out.println("FAIL: List size is not correct");
        }
        
        // Test deletion of a non-existent value
        boolean nonExistentResult = list.delete(50);
        
        if (!nonExistentResult) {
            System.out.println("PASS: Deletion of non-existent value was rejected");
        } else {
            System.out.println("FAIL: Deletion of non-existent value was not rejected");
        }
    }
    
    /**
     * Test the deleteAtPosition operation.
     */
    private static void testDeleteAtPosition() {
        System.out.println("\n=== Testing Delete at Position ===");
        LinkedList list = new LinkedList();
        
        // Insert some values
        list.insertAtEnd(10);
        list.insertAtEnd(20);
        list.insertAtEnd(30);
        list.insertAtEnd(40);
        
        // Print the list before deletion
        System.out.println("List before deletion:");
        list.printList();
        
        // Delete at position 1
        boolean result = list.deleteAtPosition(1);
        
        // Print the list after deletion
        System.out.println("List after deletion at position 1:");
        list.printList();
        
        // Check if the deletion was successful
        if (result) {
            System.out.println("PASS: Deletion at position 1 was successful");
        } else {
            System.out.println("FAIL: Deletion at position 1 was not successful");
        }
        
        // Check if the node at position 1 has the correct value
        if (list.getValueAtPosition(1) == 30) {
            System.out.println("PASS: Node at position 1 has the correct value (30)");
        } else {
            System.out.println("FAIL: Node at position 1 does not have the correct value");
        }
        
        // Check if the size is correct
        if (list.getSize() == 3) {
            System.out.println("PASS: List size is correct (3)");
        } else {
            System.out.println("FAIL: List size is not correct");
        }
        
        // Test deletion at an invalid position
        boolean invalidResult = list.deleteAtPosition(10);
        
        if (!invalidResult) {
            System.out.println("PASS: Deletion at invalid position was rejected");
        } else {
            System.out.println("FAIL: Deletion at invalid position was not rejected");
        }
    }
    
    /**
     * Test the search operation.
     */
    private static void testSearch() {
        System.out.println("\n=== Testing Search ===");
        LinkedList list = new LinkedList();
        
        // Insert some values
        list.insertAtEnd(10);
        list.insertAtEnd(20);
        list.insertAtEnd(30);
        list.insertAtEnd(40);
        
        // Print the list
        list.printList();
        
        // Search for an existing value
        boolean result = list.search(30);
        
        if (result) {
            System.out.println("PASS: Found value 30 in the list");
        } else {
            System.out.println("FAIL: Could not find value 30 in the list");
        }
        
        // Search for a non-existent value
        boolean nonExistentResult = list.search(50);
        
        if (!nonExistentResult) {
            System.out.println("PASS: Did not find value 50 in the list");
        } else {
            System.out.println("FAIL: Found value 50 in the list, but it should not be there");
        }
    }
    
    /**
     * Test the getValueAtPosition operation.
     */
    private static void testGetValueAtPosition() {
        System.out.println("\n=== Testing Get Value at Position ===");
        LinkedList list = new LinkedList();
        
        // Insert some values
        list.insertAtEnd(10);
        list.insertAtEnd(20);
        list.insertAtEnd(30);
        list.insertAtEnd(40);
        
        // Print the list
        list.printList();
        
        // Get value at position 2
        int value = list.getValueAtPosition(2);
        
        if (value == 30) {
            System.out.println("PASS: Value at position 2 is 30");
        } else {
            System.out.println("FAIL: Value at position 2 is not 30");
        }
        
        // Get value at an invalid position
        int invalidValue = list.getValueAtPosition(10);
        
        if (invalidValue == Integer.MIN_VALUE) {
            System.out.println("PASS: Value at invalid position is Integer.MIN_VALUE");
        } else {
            System.out.println("FAIL: Value at invalid position is not Integer.MIN_VALUE");
        }
    }
    
    /**
     * Test the reverse operation.
     */
    private static void testReverse() {
        System.out.println("\n=== Testing Reverse ===");
        LinkedList list = new LinkedList();
        
        // Insert some values
        list.insertAtEnd(10);
        list.insertAtEnd(20);
        list.insertAtEnd(30);
        list.insertAtEnd(40);
        
        // Print the list before reversal
        System.out.println("List before reversal:");
        list.printList();
        
        // Reverse the list
        list.reverse();
        
        // Print the list after reversal
        System.out.println("List after reversal:");
        list.printList();
        
        // Check if the head node has the correct value
        if (list.getHead() != null && list.getHead().getValue() == 40) {
            System.out.println("PASS: Head node has the correct value (40)");
        } else {
            System.out.println("FAIL: Head node does not have the correct value");
        }
        
        // Check if the last node has the correct value
        Node current = list.getHead();
        while (current != null && current.getNext() != null) {
            current = current.getNext();
        }
        
        if (current != null && current.getValue() == 10) {
            System.out.println("PASS: Last node has the correct value (10)");
        } else {
            System.out.println("FAIL: Last node does not have the correct value");
        }
    }
    
    /**
     * Test the hasCycle operation.
     */
    private static void testHasCycle() {
        System.out.println("\n=== Testing Has Cycle ===");
        LinkedList list = new LinkedList();
        
        // Insert some values
        list.insertAtEnd(10);
        list.insertAtEnd(20);
        list.insertAtEnd(30);
        list.insertAtEnd(40);
        
        // Check if the list has a cycle (should be false)
        boolean result = list.hasCycle();
        
        if (!result) {
            System.out.println("PASS: List does not have a cycle");
        } else {
            System.out.println("FAIL: List has a cycle, but it should not");
        }
        
        // Create a cycle by connecting the last node to the second node
        Node last = list.getHead();
        while (last.getNext() != null) {
            last = last.getNext();
        }
        
        Node second = list.getHead().getNext();
        last.setNext(second);
        
        // Check if the list has a cycle (should be true)
        boolean cycleResult = list.hasCycle();
        
        if (cycleResult) {
            System.out.println("PASS: List has a cycle");
        } else {
            System.out.println("FAIL: List does not have a cycle, but it should");
        }
    }
    
    /**
     * Test the findMiddle operation.
     */
    private static void testFindMiddle() {
        System.out.println("\n=== Testing Find Middle ===");
        LinkedList list = new LinkedList();
        
        // Insert some values
        list.insertAtEnd(10);
        list.insertAtEnd(20);
        list.insertAtEnd(30);
        list.insertAtEnd(40);
        list.insertAtEnd(50);
        
        // Print the list
        list.printList();
        
        // Find the middle node
        Node middle = list.findMiddle();
        
        if (middle != null && middle.getValue() == 30) {
            System.out.println("PASS: Middle node has the correct value (30)");
        } else {
            System.out.println("FAIL: Middle node does not have the correct value");
        }
        
        // Test with even number of nodes
        list.insertAtEnd(60);
        
        // Print the list
        list.printList();
        
        // Find the middle node
        Node evenMiddle = list.findMiddle();
        
        if (evenMiddle != null && evenMiddle.getValue() == 40) {
            System.out.println("PASS: Middle node has the correct value (40)");
        } else {
            System.out.println("FAIL: Middle node does not have the correct value");
        }
    }
}
