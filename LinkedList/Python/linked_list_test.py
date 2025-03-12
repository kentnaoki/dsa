"""
Test class for the LinkedList implementation.
This class provides methods to test various operations of the LinkedList.
"""
from LinkedList.Python.linked_list_template import LinkedListTemplate
from LinkedList.Python.linked_list_solution import LinkedListSolution
import sys

# Uncomment the line below to use your implementation
# LinkedList = LinkedListTemplate
# Comment the line below to use your implementation
LinkedList = LinkedListSolution

def test_insert():
    """
    Test the insert operations.
    """
    print("\n=== Testing Insert ===")
    ll = LinkedList()
    
    # Test insert at beginning
    ll.insert_at_beginning(10)
    if ll.get_size() == 1 and ll.get_head().get_value() == 10:
        print("PASS: insert_at_beginning with empty list")
    else:
        print("FAIL: insert_at_beginning with empty list")
    
    ll.insert_at_beginning(20)
    if ll.get_size() == 2 and ll.get_head().get_value() == 20:
        print("PASS: insert_at_beginning with non-empty list")
    else:
        print("FAIL: insert_at_beginning with non-empty list")
    
    # Test insert at end
    ll = LinkedList()
    ll.insert_at_end(30)
    if ll.get_size() == 1 and ll.get_head().get_value() == 30:
        print("PASS: insert_at_end with empty list")
    else:
        print("FAIL: insert_at_end with empty list")
    
    ll.insert_at_end(40)
    if ll.get_size() == 2 and ll.get_head().get_next().get_value() == 40:
        print("PASS: insert_at_end with non-empty list")
    else:
        print("FAIL: insert_at_end with non-empty list")
    
    # Test insert at position
    ll = LinkedList()
    if not ll.insert_at_position(50, 1):
        print("PASS: insert_at_position with invalid position (empty list)")
    else:
        print("FAIL: insert_at_position with invalid position (empty list)")
    
    ll.insert_at_position(50, 0)
    ll.insert_at_position(60, 1)
    ll.insert_at_position(70, 1)
    if (ll.get_size() == 3 and 
        ll.get_head().get_value() == 50 and 
        ll.get_head().get_next().get_value() == 70 and 
        ll.get_head().get_next().get_next().get_value() == 60):
        print("PASS: insert_at_position with valid positions")
    else:
        print("FAIL: insert_at_position with valid positions")

def test_delete():
    """
    Test the delete operations.
    """
    print("\n=== Testing Delete ===")
    ll = LinkedList()
    
    # Test delete from empty list
    if not ll.delete(10):
        print("PASS: delete from empty list")
    else:
        print("FAIL: delete from empty list")
    
    # Test delete existing values
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    
    if ll.delete(20):
        print("PASS: delete middle element")
    else:
        print("FAIL: delete middle element")
    
    if ll.delete(10):
        print("PASS: delete first element")
    else:
        print("FAIL: delete first element")
    
    if ll.delete(30):
        print("PASS: delete last element")
    else:
        print("FAIL: delete last element")
    
    # Test delete at position
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    
    if not ll.delete_at_position(3):
        print("PASS: delete_at_position with invalid position")
    else:
        print("FAIL: delete_at_position with invalid position")
    
    if ll.delete_at_position(1):
        print("PASS: delete_at_position middle element")
    else:
        print("FAIL: delete_at_position middle element")
    
    if ll.get_size() == 2 and ll.get_head().get_next().get_value() == 30:
        print("PASS: list structure after delete_at_position")
    else:
        print("FAIL: list structure after delete_at_position")

def test_search():
    """
    Test the search operation.
    """
    print("\n=== Testing Search ===")
    ll = LinkedList()
    
    # Test search in empty list
    if not ll.search(10):
        print("PASS: search in empty list")
    else:
        print("FAIL: search in empty list")
    
    # Test search for existing and non-existing values
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    
    if ll.search(20):
        print("PASS: search for existing value")
    else:
        print("FAIL: search for existing value")
    
    if not ll.search(40):
        print("PASS: search for non-existing value")
    else:
        print("FAIL: search for non-existing value")

def test_get_value():
    """
    Test the get_value_at_position operation.
    """
    print("\n=== Testing Get Value ===")
    ll = LinkedList()
    
    # Test get value from empty list
    if ll.get_value_at_position(0) == sys.maxsize * -1:
        print("PASS: get_value_at_position from empty list")
    else:
        print("FAIL: get_value_at_position from empty list")
    
    # Test get value at valid positions
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    
    if ll.get_value_at_position(1) == 20:
        print("PASS: get_value_at_position at valid position")
    else:
        print("FAIL: get_value_at_position at valid position")
    
    if ll.get_value_at_position(3) == sys.maxsize * -1:
        print("PASS: get_value_at_position at invalid position")
    else:
        print("FAIL: get_value_at_position at invalid position")

def test_reverse():
    """
    Test the reverse operation.
    """
    print("\n=== Testing Reverse ===")
    ll = LinkedList()
    
    # Test reverse empty list
    ll.reverse()
    if ll.is_empty():
        print("PASS: reverse empty list")
    else:
        print("FAIL: reverse empty list")
    
    # Test reverse with one element
    ll.insert_at_end(10)
    ll.reverse()
    if ll.get_head().get_value() == 10:
        print("PASS: reverse single element list")
    else:
        print("FAIL: reverse single element list")
    
    # Test reverse with multiple elements
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.reverse()
    if (ll.get_head().get_value() == 30 and 
        ll.get_head().get_next().get_value() == 20 and 
        ll.get_head().get_next().get_next().get_value() == 10):
        print("PASS: reverse multiple element list")
    else:
        print("FAIL: reverse multiple element list")

def test_cycle():
    """
    Test the cycle detection operation.
    """
    print("\n=== Testing Cycle Detection ===")
    ll = LinkedList()
    
    # Test cycle detection in empty list
    if not ll.has_cycle():
        print("PASS: cycle detection in empty list")
    else:
        print("FAIL: cycle detection in empty list")
    
    # Test cycle detection in list without cycle
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    if not ll.has_cycle():
        print("PASS: cycle detection in list without cycle")
    else:
        print("FAIL: cycle detection in list without cycle")
    
    # Create a cycle and test
    last = ll.get_head()
    while last.get_next() is not None:
        last = last.get_next()
    last.set_next(ll.get_head().get_next())  # Create cycle to second node
    
    if ll.has_cycle():
        print("PASS: cycle detection in list with cycle")
    else:
        print("FAIL: cycle detection in list with cycle")

def test_middle():
    """
    Test the find middle operation.
    """
    print("\n=== Testing Find Middle ===")
    ll = LinkedList()
    
    # Test find middle in empty list
    if ll.find_middle() is None:
        print("PASS: find middle in empty list")
    else:
        print("FAIL: find middle in empty list")
    
    # Test find middle with one element
    ll.insert_at_end(10)
    middle = ll.find_middle()
    if middle is not None and middle.get_value() == 10:
        print("PASS: find middle in single element list")
    else:
        print("FAIL: find middle in single element list")
    
    # Test find middle with odd number of elements
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    middle = ll.find_middle()
    if middle is not None and middle.get_value() == 20:
        print("PASS: find middle in odd-length list")
    else:
        print("FAIL: find middle in odd-length list")
    
    # Test find middle with even number of elements
    ll.insert_at_end(40)
    middle = ll.find_middle()
    if middle is not None and middle.get_value() == 30:
        print("PASS: find middle in even-length list")
    else:
        print("FAIL: find middle in even-length list")

def main():
    """
    Main method to run the tests.
    """
    print("Running LinkedList Tests...")
    print("Using implementation:", "LinkedListSolution" if LinkedList == LinkedListSolution else "LinkedListTemplate")
    
    test_insert()
    test_delete()
    test_search()
    test_get_value()
    test_reverse()
    test_cycle()
    test_middle()
    
    print("All tests completed.")

if __name__ == "__main__":
    main()
