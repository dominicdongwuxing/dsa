from typing import Optional
class ListNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.next: Optional['ListNode'] = None

class StackLinkedList:
    def __init__(self, max_size: int):
        self.top: Optional[ListNode] = None
        self.max_size = max_size
        self.current_size = 0
    
    def push(self, val: int):
        if self.current_size >= self.max_size:
            print("Stack overflow")
            return
        t = ListNode(val)
        t.next = self.top 
        self.top = t
        self.current_size += 1
    
    def pop(self) -> Optional[int]:
        if not self.top:
            print("Stack underflow")
            return None
        else:
            t = self.top
            self.top = self.top.next
            self.current_size -= 1
            return t.val
    
    def display(self):
        p = self.top
        while p:
            print(p.val, end=" ")
            p = p.next

operators = {
    "+": [1,2],
    "-": [1,2],
    "*": [3,4],
    "/": [3,4],
    "^": [6,5],
    "(": [7,0],
    ")": [0,-1]
}

class Stack:
    def __init__(self, size: int = 10):
        self.items = []
        self.top = -1
        self.size = size

    def is_empty(self) -> bool:
        return self.top == -1

    def is_full(self) -> bool:
        return self.top == self.size - 1
    
    def push(self, val: float):
        if self.top == self.size - 1:
            print("Stack overflow")
        else:
            self.top += 1
            self.items.append(val)
    
    def pop(self) -> Optional[float]:
        if self.top == -1:
            print("Stack underflow")
        else:
            self.top -= 1
            return self.items.pop()
    
    def peek(self, index: int) -> Optional[float]:
        if index > self.top or index < 0:
            print("Out of index")
        else:
            return self.items[index]
    
    def get_size(self):
        return self.size

def is_operator(char: str) -> bool:
    return char in operators.keys()

def pre(char: str, is_in: bool) -> int:
    return operators.get(char, [-1, -1])[int(is_in)]

def convert(expression: str) -> str:
    stack = Stack(len(expression))
    post = ""
    i = 0
    while i < len(expression):
        cur = expression[i]
        if is_operator(cur):
            if stack.top < 0:
                stack.push(cur)
                i += 1
            else:
                top = stack.peek(stack.top)
                if pre(cur, False) > pre(top, True):
                    stack.push(cur)
                    i += 1
                elif pre(cur, False) == pre(top, True):
                    stack.pop()
                    i += 1
                else:
                    post += stack.pop()
        else:
            post += cur
            i += 1
    
    while stack.top >= 0:
        post += stack.pop()
    return post

def evaluate(postfix: str) -> float:
    stack = Stack(len(postfix))
    for i in postfix:
        if is_operator(i):
            x2 = int(stack.pop())
            x1 = int(stack.pop())
            if i == "+":
                stack.push(x1 + x2)
            elif i == '-':
                stack.push(x1 - x2)
            elif i == '*':
                stack.push(x1 * x2)
            elif i == '/':
                stack.push(x1 / x2)
        else:
            stack.push(int(i))
    return stack.pop()

if __name__ == "__main__":
    expression1 = "a+b*c-d/e"
    expression2 = "((a+b)*c)-d^e^f"
    expression3 = "3*5+6/2-4"
    postfix1 = "35*62/+4-"
    print(convert("A+B*(C+D)/F+D*E"))