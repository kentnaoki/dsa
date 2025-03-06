#!/bin/bash

# Script to compile and run the Binary Search Tree tests

echo "Compiling Java files..."
javac BinarySearch/Java/*.java

if [ $? -eq 0 ]; then
    echo "Compilation successful. Running tests..."
    java BinarySearch.Java.BinarySearchTreeTest
else
    echo "Compilation failed. Please fix the errors and try again."
fi
