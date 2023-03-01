class MyListNode:
    def __init__(self, val = None, nextNode = None):
        self.val = val
        self.next = nextNode


class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = MyListNode(0) # Sentinal node
        

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
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        for _ in range(index+1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0

        self.size += 1

        pred = self.head
        for _ in range(index):
            pred = pred.next
        
        to_add = MyListNode(val)
        # Insert
        to_add.next = pred.next
        pred.next = to_add

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        self.size -= 1

        pred = self.head
        for _ in range(index):
            pred = pred.next
        
        # Delete the node
        pred.next = pred.next.next

obj = MyLinkedList()
print(obj)

obj.addAtTail(1)
print(obj)

print(obj.get(0))

# Results: 69.69% time (179ms) 81.6% space (14.6MB)