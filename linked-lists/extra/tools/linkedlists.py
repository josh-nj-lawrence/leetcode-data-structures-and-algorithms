from typing import List
# Common class definitions
# Singly linked list
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
# Doubly linked list
class dListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
# Print Method
def print_list(head):
    if head is None:
        print("Null")
    ans = ""
    while head.next:
        ans += str(head.val) + " -> "
        head = head.next
    ans += str(head.val)
    print(ans)

# Build LList from Array input
def build_ll(arr:List) -> ListNode:
    head = None
    for x in reversed(arr):
        node = ListNode(x)
        node.next = head
        head = node
    return head

if __name__ == "__main__":
    print("Module with linked list tools")