from utils import create_linked_list, ListNode

def is_loop(head: ListNode) -> bool:
    p, q = head, head.next
    while p and q and p != q:
        p = p.next 
        q = q.next 
        if q:
            q = q.next
    return p == q

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    head_no_loop = create_linked_list(arr)
    head_loop = create_linked_list(arr)
    head_loop.next.next.next.next.next = head_loop.next.next
    print(is_loop(head_loop))
    