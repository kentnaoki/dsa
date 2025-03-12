#!/bin/bash

# Script to run the DFS tests in Python

echo "Running Python DFS tests..."

# Try to run from current directory first, then try with full path
if [ -d "Python" ]; then
    # We're in the DFS directory
    cd Python
    python3 -m dfs_test
elif [ -d "DFS/Python" ]; then
    # We're in the root directory
    cd DFS/Python
    python3 -m dfs_test
else
    # We're somewhere else, use absolute path
    python3 -m DFS.Python.dfs_test
fi

if [ $? -eq 0 ]; then
    echo "Tests completed successfully."
else
    echo "Tests failed. Please check the output for errors."
fi

echo ""
echo "To use your own implementation, edit dfs_test.py and:"
echo "1. Uncomment the line: # DFS = DFSTemplate"
echo "2. Comment the line: DFS = DFSSolution"
