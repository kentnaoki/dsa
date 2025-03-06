package BinarySearch.Java;

/**
 * Complete implementation of a Binary Search Tree.
 * This class provides a reference solution for the BinarySearchTree blueprint.
 * You can use this as a guide if you get stuck with your implementation.
 */
public class BinarySearchTreeSolution {
    private Node root;

    /**
     * Constructor to create an empty Binary Search Tree.
     */
    public BinarySearchTreeSolution() {
        this.root = null;
    }

    /**
     * Get the root node of the tree.
     * 
     * @return The root node
     */
    public Node getRoot() {
        return root;
    }

    /**
     * Insert a new value into the Binary Search Tree.
     * 
     * @param value The value to be inserted
     */
    public void insert(int value) {
        root = insertRec(root, value);
    }

    /**
     * Helper method for recursive insertion.
     * 
     * @param node The current node
     * @param value The value to be inserted
     * @return The updated node
     */
    private Node insertRec(Node node, int value) {
        // If the tree is empty, create a new node as root
        if (node == null) {
            return new Node(value);
        }

        // Otherwise, find the correct position to insert the new node
        if (value < node.getValue()) {
            node.setLeft(insertRec(node.getLeft(), value));
        } else if (value > node.getValue()) {
            node.setRight(insertRec(node.getRight(), value));
        }

        // Return the unchanged node pointer
        return node;
    }

    /**
     * Search for a value in the Binary Search Tree.
     * 
     * @param value The value to search for
     * @return true if the value is found, false otherwise
     */
    public boolean search(int value) {
        return searchRec(root, value);
    }

    /**
     * Helper method for recursive search.
     * 
     * @param node The current node
     * @param value The value to search for
     * @return true if the value is found, false otherwise
     */
    private boolean searchRec(Node node, int value) {
        // Base case: if the node is null, the value is not found
        if (node == null) {
            return false;
        }

        // If the value is found at the current node
        if (node.getValue() == value) {
            return true;
        }

        // If the value is less than the current node's value, search in the left subtree
        if (value < node.getValue()) {
            return searchRec(node.getLeft(), value);
        }

        // If the value is greater than the current node's value, search in the right subtree
        return searchRec(node.getRight(), value);
    }

    /**
     * Delete a value from the Binary Search Tree.
     * 
     * @param value The value to be deleted
     * @return true if the value was found and deleted, false otherwise
     */
    public boolean delete(int value) {
        // Check if the value exists in the tree
        if (!search(value)) {
            return false;
        }

        // Delete the value
        root = deleteRec(root, value);
        return true;
    }

    /**
     * Helper method for recursive deletion.
     * 
     * @param node The current node
     * @param value The value to be deleted
     * @return The updated node
     */
    private Node deleteRec(Node node, int value) {
        // Base case: if the node is null, the value is not found
        if (node == null) {
            return null;
        }

        // Find the node to delete
        if (value < node.getValue()) {
            node.setLeft(deleteRec(node.getLeft(), value));
        } else if (value > node.getValue()) {
            node.setRight(deleteRec(node.getRight(), value));
        } else {
            // Node with the value to be deleted is found

            // Case 1: Node with no children (leaf node)
            if (node.getLeft() == null && node.getRight() == null) {
                return null;
            }

            // Case 2: Node with one child
            if (node.getLeft() == null) {
                return node.getRight();
            }
            if (node.getRight() == null) {
                return node.getLeft();
            }

            // Case 3: Node with two children
            // Find the in-order successor (smallest value in the right subtree)
            node.setValue(findMin(node.getRight()));

            // Delete the in-order successor
            node.setRight(deleteRec(node.getRight(), node.getValue()));
        }

        return node;
    }

    /**
     * Perform an in-order traversal of the Binary Search Tree.
     * In-order traversal visits the left subtree, then the root, then the right subtree.
     */
    public void inOrderTraversal() {
        inOrderTraversal(root);
    }

    /**
     * Helper method for in-order traversal.
     * 
     * @param node The current node being visited
     */
    private void inOrderTraversal(Node node) {
        if (node == null) {
            return;
        }

        // Traverse left subtree
        inOrderTraversal(node.getLeft());

        // Visit the node
        System.out.print(node.getValue() + " ");

        // Traverse right subtree
        inOrderTraversal(node.getRight());
    }

    /**
     * Perform a pre-order traversal of the Binary Search Tree.
     * Pre-order traversal visits the root, then the left subtree, then the right subtree.
     */
    public void preOrderTraversal() {
        preOrderTraversal(root);
    }

    /**
     * Helper method for pre-order traversal.
     * 
     * @param node The current node being visited
     */
    private void preOrderTraversal(Node node) {
        if (node == null) {
            return;
        }

        // Visit the node
        System.out.print(node.getValue() + " ");

        // Traverse left subtree
        preOrderTraversal(node.getLeft());

        // Traverse right subtree
        preOrderTraversal(node.getRight());
    }

    /**
     * Perform a post-order traversal of the Binary Search Tree.
     * Post-order traversal visits the left subtree, then the right subtree, then the root.
     */
    public void postOrderTraversal() {
        postOrderTraversal(root);
    }

    /**
     * Helper method for post-order traversal.
     * 
     * @param node The current node being visited
     */
    private void postOrderTraversal(Node node) {
        if (node == null) {
            return;
        }

        // Traverse left subtree
        postOrderTraversal(node.getLeft());

        // Traverse right subtree
        postOrderTraversal(node.getRight());

        // Visit the node
        System.out.print(node.getValue() + " ");
    }

    /**
     * Find the minimum value in the Binary Search Tree.
     * 
     * @return The minimum value, or Integer.MIN_VALUE if the tree is empty
     */
    public int findMin() {
        if (root == null) {
            return Integer.MIN_VALUE;
        }

        Node current = root;
        while (current.getLeft() != null) {
            current = current.getLeft();
        }

        return current.getValue();
    }

    /**
     * Find the minimum value in a subtree.
     * 
     * @param node The root of the subtree
     * @return The minimum value in the subtree
     */
    private int findMin(Node node) {
        int minValue = node.getValue();
        while (node.getLeft() != null) {
            minValue = node.getLeft().getValue();
            node = node.getLeft();
        }
        return minValue;
    }

    /**
     * Find the maximum value in the Binary Search Tree.
     * 
     * @return The maximum value, or Integer.MAX_VALUE if the tree is empty
     */
    public int findMax() {
        if (root == null) {
            return Integer.MAX_VALUE;
        }

        Node current = root;
        while (current.getRight() != null) {
            current = current.getRight();
        }

        return current.getValue();
    }

    /**
     * Get the height of the Binary Search Tree.
     * 
     * @return The height of the tree, or -1 if the tree is empty
     */
    public int getHeight() {
        return getHeight(root);
    }

    /**
     * Helper method to calculate the height of a subtree.
     * 
     * @param node The root of the subtree
     * @return The height of the subtree, or -1 if the subtree is empty
     */
    private int getHeight(Node node) {
        if (node == null) {
            return -1;
        }

        int leftHeight = getHeight(node.getLeft());
        int rightHeight = getHeight(node.getRight());

        return 1 + Math.max(leftHeight, rightHeight);
    }

    /**
     * Check if the Binary Search Tree is empty.
     * 
     * @return true if the tree is empty, false otherwise
     */
    public boolean isEmpty() {
        return root == null;
    }

    /**
     * Clear the Binary Search Tree.
     */
    public void clear() {
        root = null;
    }
}
