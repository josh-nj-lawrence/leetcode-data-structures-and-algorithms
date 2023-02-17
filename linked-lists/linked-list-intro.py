from tools import timing
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

def print_linked_list(head):
    ans = ""
    while head.next:
        ans += str(head.val) + " -> "
        head = head.next
    ans += str(head.val)

    print(ans)
            

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
two.next = three
one.next = two
head = one

print(head.val)
print(head.next.val)
print(head.next.next.val)

# Itterate over a node and sum
@timing.method_timer
def get_sum(head):
    ans = 0
    while head:
        ans += head.val
        head = head.next
    return ans
@timing.method_timer
def get_sum_rec(head):
    if not head:
        return 0
    return head.val + get_sum(head.next)

print(get_sum(one))
print(get_sum_rec(one))

@timing.method_timer
def insert_node(prev_node, node_to_add):
    node_to_add.next = prev_node.next
    prev_node.next = node_to_add

def delete_node(prev_node):
    prev_node.next = prev_node.next.next

ten = ListNode(10)
insert_node(two,ten)
print_linked_list(head)

class Double_ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

# Node being at position i
def add_double_node(node,node_to_add):
    prev = node.prev
    node_to_add.next = node
    node_to_add.prev = prev
    node.prev = node_to_add
    prev.next = node_to_add


# Linked Lists with Sentinel Nodes
"""
    Sentinal nodes point to the head and tail nodes of the linked list
    and are not elements of the list themselves
    head points to first element in the list
    tail points to last element in the list
"""

head = Double_ListNode(None)
tail = Double_ListNode(None)
head.next = tail
tail.prev = head

# Traverse list with dummy head var
def get_sum_dummy(head):
    ans = 0
    curr = head
    while curr:
        ans += curr.val
        curr = curr.next
    return ans

head = one
print("get sum with dummy head traversal:")
print(get_sum_dummy(head))