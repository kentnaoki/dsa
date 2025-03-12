"""
Test class for the Binary Search Tree implementation.
This class provides methods to test various operations of the Binary Search Tree.
"""
from BinarySearch.Python.binary_search_tree_template import BinarySearchTreeTemplate
from BinarySearch.Python.binary_search_tree_solution import BinarySearchTreeSolution
import sys

# Uncomment the line below to use your implementation
# BST = BinarySearchTreeTemplate
# Comment the line below to use your implementation
BST = BinarySearchTreeSolution

def test_insert():
    """
    Test the insert operation.
    """
    print("\n=== Testing Insert ===")
    bst = BST()
    
    # Insert some values
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)
    
    # Check if the tree structure is correct
    root = bst.get_root()
    if root is None:
        print("FAIL: Root is null after insertions")
        return
    
    if root.get_value() != 50:
        print("FAIL: Root value is not 50")
    else:
        print("PASS: Root value is 50")
    
    # Check left subtree
    left = root.get_left()
    if left is None or left.get_value() != 30:
        print("FAIL: Left child of root is not 30")
    else:
        print("PASS: Left child of root is 30")
        
        left_left = left.get_left()
        if left_left is None or left_left.get_value() != 20:
            print("FAIL: Left child of 30 is not 20")
        else:
            print("PASS: Left child of 30 is 20")
        
        left_right = left.get_right()
        if left_right is None or left_right.get_value() != 40:
            print("FAIL: Right child of 30 is not 40")
        else:
            print("PASS: Right child of 30 is 40")
    
    # Check right subtree
    right = root.get_right()
    if right is None or right.get_value() != 70:
        print("FAIL: Right child of root is not 70")
    else:
        print("PASS: Right child of root is 70")
        
        right_left = right.get_left()
        if right_left is None or right_left.get_value() != 60:
            print("FAIL: Left child of 70 is not 60")
        else:
            print("PASS: Left child of 70 is 60")
        
        right_right = right.get_right()
        if right_right is None or right_right.get_value() != 80:
            print("FAIL: Right child of 70 is not 80")
        else:
            print("PASS: Right child of 70 is 80")

def test_search():
    """
    Test the search operation.
    """
    print("\n=== Testing Search ===")
    bst = BST()
    
    # Insert some values
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)
    
    # Search for existing values
    if bst.search(50):
        print("PASS: Found 50 in the tree")
    else:
        print("FAIL: Could not find 50 in the tree")
    
    if bst.search(20):
        print("PASS: Found 20 in the tree")
    else:
        print("FAIL: Could not find 20 in the tree")
    
    if bst.search(80):
        print("PASS: Found 80 in the tree")
    else:
        print("FAIL: Could not find 80 in the tree")
    
    # Search for non-existing values
    if not bst.search(10):
        print("PASS: Did not find 10 in the tree")
    else:
        print("FAIL: Found 10 in the tree, but it should not be there")
    
    if not bst.search(90):
        print("PASS: Did not find 90 in the tree")
    else:
        print("FAIL: Found 90 in the tree, but it should not be there")

def test_delete():
    """
    Test the delete operation.
    """
    print("\n=== Testing Delete ===")
    bst = BST()
    
    # Insert some values
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)
    
    # Delete a leaf node
    if bst.delete(20):
        print("PASS: Deleted 20 from the tree")
        if not bst.search(20):
            print("PASS: 20 is no longer in the tree")
        else:
            print("FAIL: 20 is still in the tree after deletion")
    else:
        print("FAIL: Could not delete 20 from the tree")
    
    # Delete a node with one child
    if bst.delete(30):
        print("PASS: Deleted 30 from the tree")
        if not bst.search(30):
            print("PASS: 30 is no longer in the tree")
        else:
            print("FAIL: 30 is still in the tree after deletion")
    else:
        print("FAIL: Could not delete 30 from the tree")
    
    # Delete a node with two children
    if bst.delete(70):
        print("PASS: Deleted 70 from the tree")
        if not bst.search(70):
            print("PASS: 70 is no longer in the tree")
        else:
            print("FAIL: 70 is still in the tree after deletion")
    else:
        print("FAIL: Could not delete 70 from the tree")
    
    # Delete the root
    if bst.delete(50):
        print("PASS: Deleted 50 (root) from the tree")
        if not bst.search(50):
            print("PASS: 50 is no longer in the tree")
        else:
            print("FAIL: 50 is still in the tree after deletion")
    else:
        print("FAIL: Could not delete 50 (root) from the tree")
    
    # Delete a non-existing value
    if not bst.delete(100):
        print("PASS: Could not delete 100 as it does not exist in the tree")
    else:
        print("FAIL: Deleted 100, but it should not be in the tree")

def test_traversals():
    """
    Test the traversal operations.
    """
    print("\n=== Testing Traversals ===")
    bst = BST()
    
    # Insert some values
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)
    
    # Test in-order traversal
    print("In-order traversal (expected: 20, 30, 40, 50, 60, 70, 80):")
    bst.in_order_traversal()
    
    # Test pre-order traversal
    print("\nPre-order traversal (expected: 50, 30, 20, 40, 70, 60, 80):")
    bst.pre_order_traversal()
    
    # Test post-order traversal
    print("\nPost-order traversal (expected: 20, 40, 30, 60, 80, 70, 50):")
    bst.post_order_traversal()

def test_min_max():
    """
    Test the findMin and findMax operations.
    """
    print("\n=== Testing Min/Max ===")
    bst = BST()
    
    # Test on empty tree
    if bst.find_min() == sys.maxsize * -1:
        print("PASS: find_min returns -sys.maxsize for empty tree")
    else:
        print("FAIL: find_min does not return -sys.maxsize for empty tree")
    
    if bst.find_max() == sys.maxsize:
        print("PASS: find_max returns sys.maxsize for empty tree")
    else:
        print("FAIL: find_max does not return sys.maxsize for empty tree")
    
    # Insert some values
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)
    
    # Test find_min
    if bst.find_min() == 20:
        print("PASS: find_min returns 20")
    else:
        print("FAIL: find_min does not return 20")
    
    # Test find_max
    if bst.find_max() == 80:
        print("PASS: find_max returns 80")
    else:
        print("FAIL: find_max does not return 80")

def test_height():
    """
    Test the getHeight operation.
    """
    print("\n=== Testing Height ===")
    bst = BST()
    
    # Test on empty tree
    if bst.get_height() == -1:
        print("PASS: get_height returns -1 for empty tree")
    else:
        print("FAIL: get_height does not return -1 for empty tree")
    
    # Insert root only
    bst.insert(50)
    if bst.get_height() == 0:
        print("PASS: get_height returns 0 for tree with only root")
    else:
        print("FAIL: get_height does not return 0 for tree with only root")
    
    # Insert more values
    bst.insert(30)
    bst.insert(70)
    if bst.get_height() == 1:
        print("PASS: get_height returns 1 for tree with height 1")
    else:
        print("FAIL: get_height does not return 1 for tree with height 1")
    
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)
    if bst.get_height() == 2:
        print("PASS: get_height returns 2 for tree with height 2")
    else:
        print("FAIL: get_height does not return 2 for tree with height 2")
    
    # Insert to create an unbalanced tree
    bst.insert(10)
    if bst.get_height() == 3:
        print("PASS: get_height returns 3 for tree with height 3")
    else:
        print("FAIL: get_height does not return 3 for tree with height 3")

def main():
    """
    Main method to run the tests.
    """
    print("Running Binary Search Tree Tests...")
    print("Using implementation:", "BinarySearchTreeSolution" if BST == BinarySearchTreeSolution else "BinarySearchTreeTemplate")
    
    test_insert()
    test_search()
    test_delete()
    test_traversals()
    test_min_max()
    test_height()
    
    print("All tests completed.")

if __name__ == "__main__":
    main()
