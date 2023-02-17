from tools.linkedlists import ListNode, dListNode, print_list, build_ll

# reverse a linked list
def reverse_ll(head):
    prev = None
    curr = head
    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    return prev

lst1 = build_ll([1,2,3,4,5])
print_list(reverse_ll(lst1))
