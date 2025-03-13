#!/bin/bash

# Script to run the LinkedList tests in Python

echo "Running Python LinkedList tests..."

# Try to run from current directory first, then try with full path
if [ -d "Python" ]; then
    # We're in the LinkedList directory
    cd Python
    python3 -m linked_list_test
elif [ -d "LinkedList/Python" ]; then
    # We're in the root directory
    cd LinkedList/Python
    python3 -m linked_list_test
else
    # We're somewhere else, use absolute path
    cd "$(dirname "$0")"
    python3 -m linked_list_test
fi

if [ $? -eq 0 ]; then
    echo "Tests completed successfully."
else
    echo "Tests failed. Please check the output for errors."
fi

echo ""
echo "To use your own implementation, edit linked_list_test.py and:"
echo "1. Uncomment the line: # LinkedList = LinkedListTemplate"
echo "2. Comment the line: LinkedList = LinkedListSolution"
