# Binary Search Tree Implementation

This directory contains a blueprint for implementing a Binary Search Tree (BST) in Java. The implementation includes:

- `Node.java`: A complete implementation of the Node class for the BST
- `BinarySearchTree.java`: A blueprint with method stubs for the BST operations
- `BinarySearchTreeTest.java`: A test class to verify the implementation
- `BinarySearchTreeSolution.java`: A complete reference implementation that you can use if you get stuck

## Task

Your task is to implement the methods in the `BinarySearchTree.java` file. The methods are already defined with appropriate comments explaining what each method should do. Look for the `TODO` comments in the file to see what needs to be implemented.

## Key Operations to Implement

1. **insert(int value)**: Insert a new value into the BST
2. **search(int value)**: Search for a value in the BST
3. **delete(int value)**: Delete a value from the BST
4. **inOrderTraversal()**: Perform an in-order traversal of the BST
5. **preOrderTraversal()**: Perform a pre-order traversal of the BST
6. **postOrderTraversal()**: Perform a post-order traversal of the BST
7. **findMin()**: Find the minimum value in the BST
8. **findMax()**: Find the maximum value in the BST
9. **getHeight()**: Get the height of the BST

## Running the Tests

You can run the tests in two ways:

### Option 1: Using the provided script

From the root directory, run:

```bash
./BinarySearch/Java/run_tests.sh
```

This script will compile all the Java files and run the tests for you.

### Option 2: Manual compilation and execution

Alternatively, you can compile and run the tests manually with the following commands from the root directory:

```bash
# Compile the Java files
javac BinarySearch/Java/*.java

# Run the tests
java BinarySearch.Java.BinarySearchTreeTest
```

The test class will run various tests on your implementation and print the results to the console. Each test will indicate whether it passed or failed, helping you identify any issues with your implementation.

## Binary Search Tree Properties

Remember these key properties of a Binary Search Tree:

1. The left subtree of a node contains only nodes with values less than the node's value
2. The right subtree of a node contains only nodes with values greater than the node's value
3. Both the left and right subtrees must also be binary search trees
4. There are no duplicate values in the tree

## Implementation Tips

- For the `insert` method, you'll need to find the correct position to insert the new node based on the BST properties
- For the `delete` method, you'll need to handle three cases:
  - Node with no children: Simply remove the node
  - Node with one child: Replace the node with its child
  - Node with two children: Find the in-order successor (smallest value in the right subtree) or predecessor (largest value in the left subtree), replace the node's value with the successor/predecessor's value, and then delete the successor/predecessor
- For the traversal methods, you'll need to implement recursive helper methods that visit the nodes in the correct order
- For the `findMin` and `findMax` methods, remember that the minimum value is at the leftmost node and the maximum value is at the rightmost node
- For the `getHeight` method, you'll need to calculate the height recursively

Good luck with your implementation!
