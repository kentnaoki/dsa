#!/bin/bash

# Script to run the Binary Search Tree tests in Python

echo "Running Python Binary Search Tree tests..."

# Add the current directory to PYTHONPATH
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Try to run from current directory first, then try with full path
if [ -d "Python" ]; then
    # We're in the BinarySearch directory
    cd Python
    python3 -m binary_search_tree_test
elif [ -d "BinarySearch/Python" ]; then
    # We're in the root directory
    cd BinarySearch/Python
    python3 -m binary_search_tree_test
else
    # We're somewhere else, use absolute path
    python3 -m BinarySearch.Python.binary_search_tree_test
fi

if [ $? -eq 0 ]; then
    echo "Tests completed successfully."
else
    echo "Tests failed. Please check the output for errors."
fi

echo ""
echo "To use your own implementation, edit binary_search_tree_test.py and:"
echo "1. Uncomment the line: # BST = BinarySearchTreeTemplate"
echo "2. Comment the line: BST = BinarySearchTreeSolution"
