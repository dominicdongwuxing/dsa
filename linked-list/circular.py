from utils import create_linked_list, ListNode

def create(arr: list) -> ListNode:
    pre_head = ListNode()
    cur = pre_head
    for i in range(len(arr)):
        new_node = ListNode(arr[i])
        cur.next = new_node
        cur = cur.next
    cur.next = pre_head.next
    return pre_head.next

def display(head: ListNode):
    def print_recur(p: ListNode):
        nonlocal flag
        if p != head or flag == 0:
            flag = 1
            print(p.val, end=" ")
            print_recur(p.next)
    flag = 0
    print_recur(head)

def insert(head: ListNode, index: int, val: float) -> ListNode:
    new_node = ListNode(val)
    p = head
    if index == 0:
        if not head:
            new_node.next = new_node
            return new_node
        while p.next != head:
            p = p.next
        p.next = new_node
        new_node.next = head
        return new_node
    else:
        for i in range(index - 1):
            p = p.next
        new_node.next = p.next
        p.next = new_node
        return head

def delete(head: ListNode, index: int) -> ListNode:
    q, p = None, head
    if index < 1:
        return head
    if index == 1:
        while p.next != head:
            p = p.next
        p.next = head.next
        return head.next
    else:
        for i in range(index - 1):
            q = p
            p = p.next
        q.next = p.next
        if p == head:
            return head.next
        return head

if __name__ == "__main__":
    head = create([1,2,3,4,5])
    head = delete(head, 6)
    display(head)