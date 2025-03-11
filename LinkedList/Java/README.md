# LinkedList Implementation

This directory contains a blueprint for implementing a singly LinkedList in Java. The implementation includes:

- `Node.java`: A complete implementation of the Node class for the LinkedList
- `LinkedList.java`: A blueprint with method stubs for the LinkedList operations
- `LinkedListTest.java`: A test class to verify the implementation
- `LinkedListSolution.java`: A complete reference implementation that you can use if you get stuck

## Task

Your task is to implement the methods in the `LinkedList.java` file. The methods are already defined with appropriate comments explaining what each method should do. Look for the `TODO` comments in the file to see what needs to be implemented.

## Key Operations to Implement

1. **insertAtBeginning(int value)**: Insert a new value at the beginning of the list
2. **insertAtEnd(int value)**: Insert a new value at the end of the list
3. **insertAtPosition(int value, int position)**: Insert a new value at the specified position in the list
4. **delete(int value)**: Delete the first occurrence of the specified value from the list
5. **deleteAtPosition(int position)**: Delete the node at the specified position in the list
6. **search(int value)**: Search for a value in the list
7. **getValueAtPosition(int position)**: Get the value at the specified position in the list
8. **reverse()**: Reverse the list
9. **hasCycle()**: Check if the list has a cycle
10. **findMiddle()**: Find the middle node of the list

## Running the Tests

You can run the tests in two ways:

### Option 1: Using the provided script

From the root directory, run:

```bash
./LinkedList/Java/run_tests.sh
```

This script will compile all the Java files and run the tests for you.

### Option 2: Manual compilation and execution

Alternatively, you can compile and run the tests manually with the following commands from the root directory:

```bash
# Compile the Java files
javac LinkedList/Java/*.java

# Run the tests
java LinkedList.Java.LinkedListTest
```

The test class will run various tests on your implementation and print the results to the console. Each test will indicate whether it passed or failed, helping you identify any issues with your implementation.

## LinkedList Properties

Remember these key properties of a LinkedList:

1. A LinkedList is a linear data structure where each element (node) contains a value and a reference to the next node
2. The first node is called the head, and the last node's next reference is null
3. Operations like insertion and deletion can be performed in constant time at the beginning of the list
4. Operations at the end or middle of the list require traversal from the head, resulting in linear time complexity
5. LinkedLists are dynamic and can grow or shrink as needed

## Implementation Tips

- For the `insertAtBeginning` method, create a new node, set its next to the current head, and update the head to the new node
- For the `insertAtEnd` method, traverse to the end of the list and set the last node's next to the new node
- For the `insertAtPosition` method, traverse to the node at position-1 and insert the new node after it
- For the `delete` method, handle the special case where the head node has the value to be deleted
- For the `deleteAtPosition` method, handle the special case where position is 0 (deleting the head)
- For the `search` method, traverse the list and check if any node has the specified value
- For the `getValueAtPosition` method, traverse to the node at the specified position and return its value
- For the `reverse` method, use three pointers (prev, current, next) to reverse the next pointers of each node
- For the `hasCycle` method, use Floyd's Cycle-Finding Algorithm (Tortoise and Hare)
- For the `findMiddle` method, use the slow and fast pointer technique

Good luck with your implementation!
