# Depth-First Search Implementation

This directory contains a blueprint for implementing Depth-First Search (DFS) in Java. The implementation includes:

- `Node.java`: A complete implementation of the Node class for the graph
- `DFS.java`: A blueprint with method stubs for the DFS operations
- `DFSTest.java`: A test class to verify the implementation
- `DFSSolution.java`: A complete reference implementation that you can use if you get stuck

## Task

Your task is to implement the methods in the `DFS.java` file. The methods are already defined with appropriate comments explaining what each method should do. Look for the `TODO` comments in the file to see what needs to be implemented.

## Key Operations to Implement

1. **traverse()**: Perform a DFS traversal starting from the start node
2. **findPath(int targetValue)**: Find a path from the start node to a node with the target value
3. **hasPath(int targetValue)**: Check if there is a path from the start node to a node with the target value
4. **hasCycle(Node[] allNodes)**: Detect if there is a cycle in the graph
5. **topologicalSort(Node[] allNodes)**: Perform a topological sort of the graph
6. **findStronglyConnectedComponents(Node[] allNodes)**: Find all strongly connected components in the graph
7. **findArticulationPoints(Node[] allNodes)**: Find the articulation points (cut vertices) in the graph

## Running the Tests

You can run the tests in two ways:

### Option 1: Using the provided script

From the root directory, run:

```bash
./DFS/Java/run_tests.sh
```

This script will compile all the Java files and run the tests for you.

### Option 2: Manual compilation and execution

Alternatively, you can compile and run the tests manually with the following commands from the root directory:

```bash
# Compile the Java files
javac DFS/Java/*.java

# Run the tests
java DFS.Java.DFSTest
```

The test class will run various tests on your implementation and print the results to the console. Each test will indicate whether it passed or failed, helping you identify any issues with your implementation.

## Depth-First Search Properties

Remember these key properties of Depth-First Search:

1. DFS explores as far as possible along each branch before backtracking
2. DFS can be implemented using recursion or a stack
3. DFS is useful for finding paths, detecting cycles, and performing topological sorting
4. DFS can be used to find strongly connected components in a directed graph
5. DFS can be used to find articulation points (cut vertices) in an undirected graph

## Implementation Tips

- For the `traverse` method, use recursion or a stack to perform the DFS traversal and a set to keep track of visited nodes
- For the `findPath` method, use DFS and backtracking to find a path to the target node
- For the `hasPath` method, use DFS to check if there is a path to the target node
- For the `hasCycle` method, use DFS and keep track of nodes in the current recursion stack to detect cycles
- For the `topologicalSort` method, use DFS and a stack to store nodes in order of finishing time
- For the `findStronglyConnectedComponents` method, use Kosaraju's algorithm or Tarjan's algorithm
- For the `findArticulationPoints` method, use DFS and keep track of discovery times and low values

Good luck with your implementation!
