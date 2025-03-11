#!/bin/bash

# Script to compile and run the Sliding Window tests

echo "Compiling Java files..."
# Try current directory first, then the full path
if [ -d "Java" ]; then
    find Java -name "*.java" -type f | xargs javac
    if [ $? -eq 0 ]; then
        echo "Compilation successful. Running tests..."
        java SlidingWindow.Java.SlidingWindowTest
    else
        echo "Compilation failed. Please fix the errors and try again."
    fi
else
    find SlidingWindow/Java -name "*.java" -type f | xargs javac
    if [ $? -eq 0 ]; then
        echo "Compilation successful. Running tests..."
        java SlidingWindow.Java.SlidingWindowTest
    else
        echo "Compilation failed. Please fix the errors and try again."
    fi
fi
