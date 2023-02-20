from typing import List
# Common class definitions
# Singly linked list
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
    # Print Method
    def __str__(self):
        res = ""
        ptr = self
        while ptr:
            res += str(ptr.val) + " -> "
            ptr = ptr.next
        res = res.strip(" -> ")

        if len(res):
            return res
        else:
            return "Null"

# Doubly linked list
class dListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

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