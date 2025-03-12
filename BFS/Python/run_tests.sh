#!/bin/bash

# Script to run the BFS tests in Python

echo "Running Python BFS tests..."

# Try to run from current directory first, then try with full path
if [ -d "Python" ]; then
    # We're in the BFS directory
    cd Python
    python3 -m bfs_test
elif [ -d "BFS/Python" ]; then
    # We're in the root directory
    cd BFS/Python
    python3 -m bfs_test
else
    # We're somewhere else, use absolute path
    python3 -m BFS.Python.bfs_test
fi

if [ $? -eq 0 ]; then
    echo "Tests completed successfully."
else
    echo "Tests failed. Please check the output for errors."
fi

echo ""
echo "To use your own implementation, edit bfs_test.py and:"
echo "1. Uncomment the line: # BFS = BFSTemplate"
echo "2. Comment the line: BFS = BFSSolution"
