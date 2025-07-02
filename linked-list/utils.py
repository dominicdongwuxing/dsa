from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def create_linked_list(arr: list) -> Optional[ListNode]:
    pre_head = ListNode()
    cur = pre_head
    for val in arr:
        new_node = ListNode(val)
        cur.next = new_node
        cur = cur.next
    return pre_head.next

def print_linked_list(head: Optional[ListNode]):
    cur = head
    while cur:
        print(cur.val, end=" ")
        cur = cur.next

def count_linked_list(head: Optional[ListNode]) -> int:
    count = 0
    cur = head
    while cur:
        count += 1
        cur = cur.next
    return count

def sum_linked_list(head: Optional[ListNode]) -> int:
    sum = 0
    cur = head
    while cur:
        sum += cur.val
        cur = cur.next
    return sum

def max_linked_list(head: Optional[ListNode]) -> float:
    max_val = float('-inf')
    cur = head
    while cur:
        max_val = max(max_val, cur.val)
        cur = cur.next
    return max_val

def insert_linked_list(head: Optional[ListNode], idx: int, val: int) -> Optional[ListNode]:
    if idx == 0:
        new_node = ListNode(val)
        new_node.next = head
        return new_node
    
    cur = head
    for i in range(idx - 1):
        if not cur:
            return head
        cur = cur.next

    if not cur:
        return head
    new_node = ListNode(val)
    new_node.next = cur.next
    cur.next = new_node
    return head

def insert_linked_list_sorted(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    cur, prev = head, None
    new_node = ListNode(val)
    if not cur:
        return new_node
    
    while cur and cur.val <= val:
        prev = cur
        cur = cur.next

    if cur == head:
        new_node.next = cur
        return new_node
    
    prev.next = new_node
    new_node.next = cur
    return head

def delete_linked_list(head: Optional[ListNode], idx: int) -> Optional[ListNode]:
    if idx < 1:
        return head
    if idx == 1:
        return head.next
    cur_idx = 1
    cur, prev = head, None
    while cur_idx < idx and cur:
        prev = cur
        cur = cur.next
        cur_idx += 1
    if cur:
        prev.next = cur.next
    return head

def remove_duplicates_from_sorted(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, cur = head, head.next
    while cur:
        if prev.val == cur.val:
            prev.next = cur.next
            cur = cur.next
        else:
            prev = cur
            cur = cur.next

    return head

def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
    r, q ,p = None, None, head
    while p:
        r = q
        q = p
        p = p.next
        q.next = r

    return q


def reverse_recurse(q: Optional[ListNode], p: Optional[ListNode]):
    if p:
        new_head = reverse_recurse(p, p.next)
        p.next = q
        return new_head
    else:
        return q

def concat_linked_list(first: Optional[ListNode], second: Optional[ListNode]) -> Optional[ListNode]:
    head = first
    while first.next:
        first = first.next
    first.next = second
    return head

def merge_linked_list(first: Optional[ListNode], second: Optional[ListNode]) -> Optional[ListNode]:
    third, last = None, None
    if first.val < second.val:
        third = first
        last = first
        first = first.next
    else:
        third = second
        last = second
        second = second.next
    last.next = None

    while first and second:
        if first.val < second.val:
            last.next = first
            last = first
            first = first.next
        else:
            last.next = second
            last = second
            second = second.next
        last.next = None
        
    
    if first:
        last.next = first
    else:
        last.next = second
    return third
                        


if __name__ == "__main__":
    arr = [1,2,3,4]
    arr2 = [3,4]
    first = create_linked_list(arr)
    second = create_linked_list(arr2)
    new_head = merge_linked_list(first, second)
    print_linked_list(new_head)