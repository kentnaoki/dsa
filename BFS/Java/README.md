# Breadth-First Search Implementation

This directory contains a blueprint for implementing Breadth-First Search (BFS) in Java. The implementation includes:

- `Node.java`: A complete implementation of the Node class for the graph
- `BFS.java`: A blueprint with method stubs for the BFS operations
- `BFSTest.java`: A test class to verify the implementation
- `BFSSolution.java`: A complete reference implementation that you can use if you get stuck

## Task

Your task is to implement the methods in the `BFS.java` file. The methods are already defined with appropriate comments explaining what each method should do. Look for the `TODO` comments in the file to see what needs to be implemented.

## Key Operations to Implement

1. **traverse()**: Perform a BFS traversal starting from the start node
2. **findShortestPath(int targetValue)**: Find the shortest path from the start node to a node with the target value
3. **hasPath(int targetValue)**: Check if there is a path from the start node to a node with the target value
4. **findConnectedComponents(Node[] allNodes)**: Find all connected components in the graph
5. **findLevels()**: Find the level (distance) of each node from the start node
6. **isBipartite(Node[] allNodes)**: Check if the graph is bipartite

## Running the Tests

You can run the tests in two ways:

### Option 1: Using the provided script

From the root directory, run:

```bash
./BFS/Java/run_tests.sh
```

This script will compile all the Java files and run the tests for you.

### Option 2: Manual compilation and execution

Alternatively, you can compile and run the tests manually with the following commands from the root directory:

```bash
# Compile the Java files
javac BFS/Java/*.java

# Run the tests
java BFS.Java.BFSTest
```

The test class will run various tests on your implementation and print the results to the console. Each test will indicate whether it passed or failed, helping you identify any issues with your implementation.

## Breadth-First Search Properties

Remember these key properties of Breadth-First Search:

1. BFS explores all neighbors at the present depth before moving on to nodes at the next depth level
2. BFS uses a queue data structure to keep track of nodes to visit next
3. BFS is optimal for finding the shortest path in an unweighted graph
4. BFS can be used to find connected components in a graph
5. BFS can be used to check if a graph is bipartite

## Implementation Tips

- For the `traverse` method, use a queue to perform the BFS traversal and a set to keep track of visited nodes
- For the `findShortestPath` method, use BFS and keep track of the parent of each node to reconstruct the path
- For the `hasPath` method, use BFS to check if there is a path to the target node
- For the `findConnectedComponents` method, run BFS from each unvisited node to find all connected components
- For the `findLevels` method, use BFS and keep track of the level of each node
- For the `isBipartite` method, use BFS to color the nodes and check if there are any conflicts

Good luck with your implementation!
