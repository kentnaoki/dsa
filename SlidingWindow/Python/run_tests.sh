#!/bin/bash

# Script to run the Sliding Window tests in Python

echo "Running Python Sliding Window tests..."

# Try to run from current directory first, then try with full path
if [ -d "Python" ]; then
    # We're in the SlidingWindow directory
    cd Python
    python3 -m sliding_window_test
elif [ -d "SlidingWindow/Python" ]; then
    # We're in the root directory
    cd SlidingWindow/Python
    python3 -m sliding_window_test
else
    # We're somewhere else, use absolute path
    python3 -m SlidingWindow.Python.sliding_window_test
fi

if [ $? -eq 0 ]; then
    echo "Tests completed successfully."
else
    echo "Tests failed. Please check the output for errors."
fi

echo ""
echo "To use your own implementation, edit sliding_window_test.py and:"
echo "1. Uncomment the line: # SlidingWindow = SlidingWindowTemplate"
echo "2. Comment the line: SlidingWindow = SlidingWindowSolution"
