class DoubleNode:
    def __init__(self, val = 0, next: 'DoubleNode' = None, prev: 'DoubleNode' = None):
        self.val = val
        self.next = next
        self.prev = prev

def create(arr: list) -> DoubleNode:
    if len(arr) == 0:
        return None
    head = last = DoubleNode(arr[0])
    for i in range(1,len(arr)):
        t = DoubleNode(arr[i])
        last.next = t
        t.prev = last
        last = t
    return head

def length(head: DoubleNode) -> int:
    l = 0
    while head:
        l += 1
        head = head.next
    return l

def display(head: DoubleNode):
    p = head
    if p:
        print(p.val, end=" ")
        display(p.next)

def insert(head: DoubleNode, index: int, val: float) -> DoubleNode:
    if index < 0 or index > length(head): 
        return head
    t = DoubleNode(val)
    if index == 0:
        t.next = head
        head.prev = t
        return t
    p = head
    for i in range(index - 1):
        p = p.next
    if p.next:
        p.next.prev = t
        t.next = p.next
    p.next = t
    t.prev = p
    return head

def delete(head: DoubleNode, index: int) -> DoubleNode:
    if index < 1 or index > length(head):
        return head
    if index == 1:
        head = head.next
        if head:
            head.prev = None
        return head
    p = head
    for i in range(index - 1):
        p = p.next
    p.prev.next = p.next
    if p.next:
        p.next.prev = p.prev
    return head

def reverse(head: DoubleNode) -> DoubleNode:
    p = head
    new_head = None
    while p:
        temp = p.next
        p.next = p.prev
        p.prev = temp
        new_head = p
        p = p.prev
    return new_head

def middle_two_pointers(head: DoubleNode) -> DoubleNode:
    p, q = head, head
    while q:
        q = q.next
        if q:
            q = q.next
        if q:
            p = p.next
    return p

if __name__ == "__main__":
    arr = [1]
    node = middle_two_pointers(create(arr))
    print(node.val)