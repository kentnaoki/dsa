#!/bin/bash

# Script to compile and run the Depth-First Search tests

echo "Compiling Java files..."
# Try current directory first, then the full path
if [ -d "Java" ]; then
    find Java -name "*.java" -type f | xargs javac
    if [ $? -eq 0 ]; then
        echo "Compilation successful. Running tests..."
        java DFS.Java.DFSTest
    else
        echo "Compilation failed. Please fix the errors and try again."
    fi
else
    find DFS/Java -name "*.java" -type f | xargs javac
    if [ $? -eq 0 ]; then
        echo "Compilation successful. Running tests..."
        java DFS.Java.DFSTest
    else
        echo "Compilation failed. Please fix the errors and try again."
    fi
fi
