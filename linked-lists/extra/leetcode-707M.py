class MyListNode:
    def __init__(self, val = None, nextNode = None):
        self.val = val
        self.next = nextNode


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.sentinel = MyListNode(0) # Sentinal node
        

    def __str__(self):
        curr = self.head
        ans = ""
        try:
            while curr.next:
                ans += str(curr.val) + " -> "
                curr = curr.next
            ans += str(curr.val)
        except AttributeError:
            return ans
        return ans
    

    def get(self, index: int) -> int:
        curr = self.head
        try:
            if index == 0:
                return curr.val
            for i in range(index):
                curr = curr.next
            return curr.val
        except AttributeError:
            return -1

    def addAtHead(self, val: int) -> None:
        nextNode = self.head
        self.head = MyListNode(val)
        self.sentinel = self.head
        self.head.next = nextNode

    def addAtTail(self, val: int) -> None:
        curr = self.sentinel.next
        try:
            while curr.next:
                curr = curr.next
        except AttributeError:
            curr = MyListNode(val)
        curr.next = MyListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head
        prev = self.sentinel

        if index == 0:
            self.addAtHead(val)
        for _ in range(index):
            prev = curr
            curr = curr.next
        prev.next = MyListNode(val)
        prev.next.next = curr

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        prev = self.sentinel
        if index == 0:
            self.head = self.head.next
            self.sentinel = self.head
        for _ in range(index):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        

obj = MyLinkedList()
print(obj)

obj.addAtTail(1)
print(obj)

print(obj.get(0))

# print("noaisofjasdf")
# obj.deleteAtIndex(0)
# print(obj)
# obj.addAtTail(3)
# print(obj)
# obj.addAtIndex(1,2)
# print(obj)

# print(obj.get(1))
# obj.deleteAtIndex(1)
# print(obj.get(1))
# print(obj)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)