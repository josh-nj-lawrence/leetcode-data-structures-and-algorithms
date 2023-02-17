from typing import List

"""
    Fast & slow pointers is an implementation of the two
    pointers technique. The idea centers around managing two 
    pointers, where the move at different 'speeds', begin at
    different locations or some other difference.

"""

# Common class definitions
  # Singly linked list
class s_ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
  # Doubly linked list
class dbl_ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
  # Print Method
def print_list(head):
    ans = ""
    while head.next:
        ans += str(head.val) + " -> "
        head = head.next
    ans += str(head.val)
    print(ans)

    # Build LList from Array input
def build_dll(arr:List) -> dbl_ListNode:
    head = None
    for x in reversed(arr):
        node = dbl_ListNode(x)
        node.next = head
        head = node
    return head
    
  # Example List
lst1 = build_dll([1,4,6,3,7,8,3])
print_list(lst1)
# Example 1: given head of LL with odd number of nodes head, 
# return value of the node in the middle
def get_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val

print(f"get middle: {get_middle(lst1)}")