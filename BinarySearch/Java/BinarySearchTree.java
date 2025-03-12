package BinarySearch.Java;

/**
 * Binary Search Tree implementation.
 * This class provides a blueprint for implementing a Binary Search Tree with
 * various operations like insert, delete, search, and traversal.
 */
public class BinarySearchTree {
    private Node root;

    /**
     * Constructor to create an empty Binary Search Tree.
     */
    public BinarySearchTree() {
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
        // TODO: Implement this method
        // If the tree is empty, create a new node as root
        // Otherwise, find the correct position to insert the new node
        Node newNode = new Node(value);
        if (root == null) {
            root = newNode;
            return;
        }
        Node current = root;
        Node prev = null;
        while (current != null) {
              if (value <= current.getValue()) {
                prev = current;
                current = current.getLeft();
              } else {
                prev = current;
                current = current.getRight();
              }
        }
        
        

        if (value <= prev.getValue()) {
            prev.setLeft(newNode);
        } else {
            prev.setRight(newNode);
        }
    }

    /**
     * Search for a value in the Binary Search Tree.
     * 
     * @param value The value to search for
     * @return true if the value is found, false otherwise
     */
    public boolean search(int value) {
        // TODO: Implement this method
        // Start from the root and traverse the tree
        // Return true if the value is found, false otherwise
        
        return dfs(root, value);
    }

    private boolean dfs(Node node, int value) {
        if (node == null) {
            return false;
        }

        if (node.getValue() == value) {
            return true;
        }

        return dfs(node.getLeft(), value) || dfs(node.getRight(), value);
    }

    /**
     * Delete a value from the Binary Search Tree.
     * 
     * @param value The value to be deleted
     * @return true if the value was found and deleted, false otherwise
     */
    public boolean delete(int value) {
        // TODO: Implement this method
        // Find the node to delete
        // Handle different cases: node with no children, one child, or two children
        // Return true if the value was found and deleted, false otherwise

        if (!search(value)) {
            return false;
        }

        Node current = root;
        Node prev = null;
        while (current != null && current.getValue() != value) {
            prev = current;
            if (value <= current.getValue()) {
                current = current.getLeft();
            } else {
                current = current.getRight();
            }
        }

        if (prev == null) {
            root = deleteNode(root);
            return true;
        }

        if (prev.getLeft() == current) {
            prev.setLeft(deleteNode(current));
        } else {
            prev.setRight(deleteNode(current));
        }
        return true;
    }

    private Node deleteNode(Node node) {
        // 1. no children
        
        if (node.getLeft() == null && node.getRight() == null) {
            return null;
        }
        
        // 2. one child
        if (node.getLeft() == null) {
            return node.getRight();
        }
        if (node.getRight() == null) {
            return node.getLeft();
        }

        // 3. two children
        Node successor = findMinNode(node.getRight());
        node.setValue(successor.getValue());
        node.setRight(deleteMinNode(node.getRight()));
        return node;
    }

    private Node findMinNode(Node node) {
        while (node.getLeft() != null) {
            node = node.getLeft();
        }

        return node;
    }

    private Node deleteMinNode(Node node) {
        if (node.getLeft() == null) {
            return node.getRight();
        }

        node.setLeft(deleteMinNode(node.getLeft()));
        return node;
    }

    private Node getSmallestNode(Node node) {
        Node prev = null;
        while (node.getLeft() != null) {
            prev = node;
            node = node.getLeft();
        }
        if (prev != null) {
            prev.setLeft(null);
        }
        return node;
    }

    /**
     * Perform an in-order traversal of the Binary Search Tree.
     * In-order traversal visits the left subtree, then the root, then the right subtree.
     */
    public void inOrderTraversal() {
        // TODO: Implement this method
        // Use a helper method to perform the traversal recursively
        inOrderTraversal(root);
    }

    /**
     * Helper method for in-order traversal.
     * 
     * @param node The current node being visited
     */
    private void inOrderTraversal(Node node) {
        // TODO: Implement this method
        // If the node is null, return
        // Otherwise, traverse left subtree, visit the node, traverse right subtree
        if (node == null) {
            return;
        }

        inOrderTraversal(node.getLeft());
        System.out.println(node.getValue());
        inOrderTraversal(node.getRight());
    }

    /**
     * Perform a pre-order traversal of the Binary Search Tree.
     * Pre-order traversal visits the root, then the left subtree, then the right subtree.
     */
    public void preOrderTraversal() {
        // TODO: Implement this method
        // Use a helper method to perform the traversal recursively
        preOrderTraversal(root);
    }

    /**
     * Helper method for pre-order traversal.
     * 
     * @param node The current node being visited
     */
    private void preOrderTraversal(Node node) {
        // TODO: Implement this method
        // If the node is null, return
        // Otherwise, visit the node, traverse left subtree, traverse right subtree
        if (node == null) {
            return;
        }

        System.out.println(node.getValue());
        preOrderTraversal(node.getLeft());
        preOrderTraversal(node.getRight());
    }

    /**
     * Perform a post-order traversal of the Binary Search Tree.
     * Post-order traversal visits the left subtree, then the right subtree, then the root.
     */
    public void postOrderTraversal() {
        // TODO: Implement this method
        // Use a helper method to perform the traversal recursively
        postOrderTraversal(root);
    }

    /**
     * Helper method for post-order traversal.
     * 
     * @param node The current node being visited
     */
    private void postOrderTraversal(Node node) {
        // TODO: Implement this method
        // If the node is null, return
        // Otherwise, traverse left subtree, traverse right subtree, visit the node
        if (node == null) {
            return;
        }

        postOrderTraversal(node.getLeft());
        postOrderTraversal(node.getRight());
        System.out.println(node.getValue());
    }

    /**
     * Find the minimum value in the Binary Search Tree.
     * 
     * @return The minimum value, or Integer.MIN_VALUE if the tree is empty
     */
    public int findMin() {
        // TODO: Implement this method
        // The minimum value is the leftmost node in the tree
        if (root == null) {
            return Integer.MIN_VALUE;
        }

        Node current = root;
    
        if (current.getLeft() == null) {
            return root.getValue();
        }

        while (current.getLeft() != null) {
            current = current.getLeft();
        }

        return current.getValue();
    }

    /**
     * Find the maximum value in the Binary Search Tree.
     * 
     * @return The maximum value, or Integer.MAX_VALUE if the tree is empty
     */
    public int findMax() {
        // TODO: Implement this method
        // The maximum value is the rightmost node in the tree
        if (root == null) return Integer.MAX_VALUE;

        Node current = root;

        if (current.getRight() == null) return root.getValue();
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
        // TODO: Implement this method
        // Use a helper method to calculate the height recursively
        return getHeight(root);
    }

    /**
     * Helper method to calculate the height of a subtree.
     * 
     * @param node The root of the subtree
     * @return The height of the subtree, or -1 if the subtree is empty
     */
    private int getHeight(Node node) {
        // TODO: Implement this method
        // If the node is null, return -1
        // Otherwise, return 1 + the maximum of the heights of the left and right subtrees
        if (node == null) {
            return -1;
        }
        return 1 + Math.max(getHeight(node.getLeft()), getHeight(node.getRight()));
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
