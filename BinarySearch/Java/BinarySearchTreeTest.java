package BinarySearch.Java;

/**
 * Test class for the Binary Search Tree implementation.
 * This class provides methods to test various operations of the Binary Search Tree.
 */
public class BinarySearchTreeTest {
    
    /**
     * Main method to run the tests.
     * 
     * @param args Command line arguments (not used)
     */
    public static void main(String[] args) {
        System.out.println("Running Binary Search Tree Tests...");
        
        testInsert();
        testSearch();
        testDelete();
        testTraversals();
        testMinMax();
        testHeight();
        
        System.out.println("All tests completed.");
    }
    
    /**
     * Test the insert operation.
     */
    private static void testInsert() {
        System.out.println("\n=== Testing Insert ===");
        BinarySearchTree bst = new BinarySearchTree();
        
        // Insert some values
        bst.insert(50);
        bst.insert(30);
        bst.insert(70);
        bst.insert(20);
        bst.insert(40);
        bst.insert(60);
        bst.insert(80);
        
        // Check if the tree structure is correct
        Node root = bst.getRoot();
        if (root == null) {
            System.out.println("FAIL: Root is null after insertions");
            return;
        }
        
        if (root.getValue() != 50) {
            System.out.println("FAIL: Root value is not 50");
        } else {
            System.out.println("PASS: Root value is 50");
        }
        
        // Check left subtree
        Node left = root.getLeft();
        if (left == null || left.getValue() != 30) {
            System.out.println("FAIL: Left child of root is not 30");
        } else {
            System.out.println("PASS: Left child of root is 30");
            
            Node leftLeft = left.getLeft();
            if (leftLeft == null || leftLeft.getValue() != 20) {
                System.out.println("FAIL: Left child of 30 is not 20");
            } else {
                System.out.println("PASS: Left child of 30 is 20");
            }
            
            Node leftRight = left.getRight();
            if (leftRight == null || leftRight.getValue() != 40) {
                System.out.println("FAIL: Right child of 30 is not 40");
            } else {
                System.out.println("PASS: Right child of 30 is 40");
            }
        }
        
        // Check right subtree
        Node right = root.getRight();
        if (right == null || right.getValue() != 70) {
            System.out.println("FAIL: Right child of root is not 70");
        } else {
            System.out.println("PASS: Right child of root is 70");
            
            Node rightLeft = right.getLeft();
            if (rightLeft == null || rightLeft.getValue() != 60) {
                System.out.println("FAIL: Left child of 70 is not 60");
            } else {
                System.out.println("PASS: Left child of 70 is 60");
            }
            
            Node rightRight = right.getRight();
            if (rightRight == null || rightRight.getValue() != 80) {
                System.out.println("FAIL: Right child of 70 is not 80");
            } else {
                System.out.println("PASS: Right child of 70 is 80");
            }
        }
    }
    
    /**
     * Test the search operation.
     */
    private static void testSearch() {
        System.out.println("\n=== Testing Search ===");
        BinarySearchTree bst = new BinarySearchTree();
        
        // Insert some values
        bst.insert(50);
        bst.insert(30);
        bst.insert(70);
        bst.insert(20);
        bst.insert(40);
        bst.insert(60);
        bst.insert(80);
        
        // Search for existing values
        if (bst.search(50)) {
            System.out.println("PASS: Found 50 in the tree");
        } else {
            System.out.println("FAIL: Could not find 50 in the tree");
        }
        
        if (bst.search(20)) {
            System.out.println("PASS: Found 20 in the tree");
        } else {
            System.out.println("FAIL: Could not find 20 in the tree");
        }
        
        if (bst.search(80)) {
            System.out.println("PASS: Found 80 in the tree");
        } else {
            System.out.println("FAIL: Could not find 80 in the tree");
        }
        
        // Search for non-existing values
        if (!bst.search(10)) {
            System.out.println("PASS: Did not find 10 in the tree");
        } else {
            System.out.println("FAIL: Found 10 in the tree, but it should not be there");
        }
        
        if (!bst.search(90)) {
            System.out.println("PASS: Did not find 90 in the tree");
        } else {
            System.out.println("FAIL: Found 90 in the tree, but it should not be there");
        }
    }
    
    /**
     * Test the delete operation.
     */
    private static void testDelete() {
        System.out.println("\n=== Testing Delete ===");
        BinarySearchTree bst = new BinarySearchTree();
        
        // Insert some values
        bst.insert(50);
        bst.insert(30);
        bst.insert(70);
        bst.insert(20);
        bst.insert(40);
        bst.insert(60);
        bst.insert(80);
        
        // Delete a leaf node
        if (bst.delete(20)) {
            System.out.println("PASS: Deleted 20 from the tree");
            if (!bst.search(20)) {
                System.out.println("PASS: 20 is no longer in the tree");
            } else {
                System.out.println("FAIL: 20 is still in the tree after deletion");
            }
        } else {
            System.out.println("FAIL: Could not delete 20 from the tree");
        }
        
        // Delete a node with one child
        if (bst.delete(30)) {
            System.out.println("PASS: Deleted 30 from the tree");
            if (!bst.search(30)) {
                System.out.println("PASS: 30 is no longer in the tree");
            } else {
                System.out.println("FAIL: 30 is still in the tree after deletion");
            }
        } else {
            System.out.println("FAIL: Could not delete 30 from the tree");
        }
        
        // Delete a node with two children
        if (bst.delete(70)) {
            System.out.println("PASS: Deleted 70 from the tree");
            if (!bst.search(70)) {
                System.out.println("PASS: 70 is no longer in the tree");
            } else {
                System.out.println("FAIL: 70 is still in the tree after deletion");
            }
        } else {
            System.out.println("FAIL: Could not delete 70 from the tree");
        }
        
        // Delete the root
        if (bst.delete(50)) {
            System.out.println("PASS: Deleted 50 (root) from the tree");
            if (!bst.search(50)) {
                System.out.println("PASS: 50 is no longer in the tree");
            } else {
                System.out.println("FAIL: 50 is still in the tree after deletion");
            }
        } else {
            System.out.println("FAIL: Could not delete 50 (root) from the tree");
        }
        
        // Delete a non-existing value
        if (!bst.delete(100)) {
            System.out.println("PASS: Could not delete 100 as it does not exist in the tree");
        } else {
            System.out.println("FAIL: Deleted 100, but it should not be in the tree");
        }
    }
    
    /**
     * Test the traversal operations.
     */
    private static void testTraversals() {
        System.out.println("\n=== Testing Traversals ===");
        BinarySearchTree bst = new BinarySearchTree();
        
        // Insert some values
        bst.insert(50);
        bst.insert(30);
        bst.insert(70);
        bst.insert(20);
        bst.insert(40);
        bst.insert(60);
        bst.insert(80);
        
        // Test in-order traversal
        System.out.println("In-order traversal (expected: 20, 30, 40, 50, 60, 70, 80):");
        bst.inOrderTraversal();
        
        // Test pre-order traversal
        System.out.println("\nPre-order traversal (expected: 50, 30, 20, 40, 70, 60, 80):");
        bst.preOrderTraversal();
        
        // Test post-order traversal
        System.out.println("\nPost-order traversal (expected: 20, 40, 30, 60, 80, 70, 50):");
        bst.postOrderTraversal();
    }
    
    /**
     * Test the findMin and findMax operations.
     */
    private static void testMinMax() {
        System.out.println("\n=== Testing Min/Max ===");
        BinarySearchTree bst = new BinarySearchTree();
        
        // Test on empty tree
        if (bst.findMin() == Integer.MIN_VALUE) {
            System.out.println("PASS: findMin returns Integer.MIN_VALUE for empty tree");
        } else {
            System.out.println("FAIL: findMin does not return Integer.MIN_VALUE for empty tree");
        }
        
        if (bst.findMax() == Integer.MAX_VALUE) {
            System.out.println("PASS: findMax returns Integer.MAX_VALUE for empty tree");
        } else {
            System.out.println("FAIL: findMax does not return Integer.MAX_VALUE for empty tree");
        }
        
        // Insert some values
        bst.insert(50);
        bst.insert(30);
        bst.insert(70);
        bst.insert(20);
        bst.insert(40);
        bst.insert(60);
        bst.insert(80);
        
        // Test findMin
        if (bst.findMin() == 20) {
            System.out.println("PASS: findMin returns 20");
        } else {
            System.out.println("FAIL: findMin does not return 20");
        }
        
        // Test findMax
        if (bst.findMax() == 80) {
            System.out.println("PASS: findMax returns 80");
        } else {
            System.out.println("FAIL: findMax does not return 80");
        }
    }
    
    /**
     * Test the getHeight operation.
     */
    private static void testHeight() {
        System.out.println("\n=== Testing Height ===");
        BinarySearchTree bst = new BinarySearchTree();
        
        // Test on empty tree
        if (bst.getHeight() == -1) {
            System.out.println("PASS: getHeight returns -1 for empty tree");
        } else {
            System.out.println("FAIL: getHeight does not return -1 for empty tree");
        }
        
        // Insert root only
        bst.insert(50);
        if (bst.getHeight() == 0) {
            System.out.println("PASS: getHeight returns 0 for tree with only root");
        } else {
            System.out.println("FAIL: getHeight does not return 0 for tree with only root");
        }
        
        // Insert more values
        bst.insert(30);
        bst.insert(70);
        if (bst.getHeight() == 1) {
            System.out.println("PASS: getHeight returns 1 for tree with height 1");
        } else {
            System.out.println("FAIL: getHeight does not return 1 for tree with height 1");
        }
        
        bst.insert(20);
        bst.insert(40);
        bst.insert(60);
        bst.insert(80);
        if (bst.getHeight() == 2) {
            System.out.println("PASS: getHeight returns 2 for tree with height 2");
        } else {
            System.out.println("FAIL: getHeight does not return 2 for tree with height 2");
        }
        
        // Insert to create an unbalanced tree
        bst.insert(10);
        if (bst.getHeight() == 3) {
            System.out.println("PASS: getHeight returns 3 for tree with height 3");
        } else {
            System.out.println("FAIL: getHeight does not return 3 for tree with height 3");
        }
    }
}
