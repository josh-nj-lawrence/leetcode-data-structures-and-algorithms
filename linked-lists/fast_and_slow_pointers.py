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

# Example 3: Give the head of a linked list and an integer k, 
# return the kth node from the end
# For example given 1 - 2 - 3 - 4 - 5 and k = 2 return 4
def get_k_from_end(head, k):
    ans = head
    curr = head
    for _ in range(k):
        curr = curr.next
    while curr:
        ans = ans.next
        curr = curr.next
    return ans

lst2 = build_dll([1,2,3,4,5])
print(get_k_from_end(lst2,2))

# Time complexity is O(n) as we only need to itterate over the length of the list
# Space complexity is O(1) as we just need to define two pointers.

