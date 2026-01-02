from collections import deque

#q1

class Queue:
    def __init__(self):
        self.items = []

    def enqueue (self, item):
        self.items.append(item)

    def dequeue (self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty (self):
        return len(self.items) == 0

    def reverse(self):
        if self.is_empty():
            return []

        front = self.dequeue()
        self.reverse()
        self.enqueue(front)
        return self.items

    def find_min(self, current_min=1000000):
        if self.is_empty():
            return current_min

        front = self.dequeue()
        current_min = min (current_min, front)
        min_val = self.find_min(current_min)
        self.enqueue(front)
        return min_val

q = Queue()
for num in [5, 3, 9, 1, 7]:
    q.enqueue(num)

print(q.reverse())
print(q.find_min())

#q2
def generate_binary_numbers(n):
    q = deque()
    q.append("1")
    result = []

    for i in range(n):
        front = q.popleft()
        result.append(front)
        q.append(front + "0")
        q.append(front + "1")

    return result

print(generate_binary_numbers(16))

#q3
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

def process_sequence(sequence):
    stack = Stack()
    popped_values = []

    for ch in sequence:
        if ch == "*":
            if not stack.is_empty():
                popped_values.append(stack.pop())
        else:
            stack.push(ch)

    return popped_values

print(process_sequence("EAS*Y*QUE***ST***IO*N***"))

#q4

class Queue:
    def __init__(self):
        self.items = deque()

    def put(self, item):
        self.items.append(item)

    def get(self):
        if not self.is_empty():
            return self.items.popleft()
        return None

    def is_empty(self):
        return len(self.items) == 0

def sequence(sequence):
    queue = Queue()
    get_values = []

    for ch in sequence:
        if ch == "*":
            value = queue.get()
            if value is not None:
                get_values.append(value)
        else:
            queue.put(ch)

    return get_values

print(sequence("EAS*Y*QUE***ST***IO*N***"))

#q5
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

sequence = "Test Sequence"
stack = Stack()

for ch in sequence:
    stack.push(ch)

reversed_sequence = ("")
while not stack.is_empty():
    reversed_sequence += stack.pop()

print(reversed_sequence)

#q6
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

def evaluate_postfix(expression):
    stack = Stack()
    operators = '+-*/^'

    for ch in expression:
        if ch.isdigit():
            stack.push(int(ch))

        elif ch in operators:
            b = stack.pop()
            a = stack.pop()
            if ch == "+":
                stack.push(a + b)
            elif ch == "-":
                stack.push(a - b)
            elif ch == "*":
                stack.push(a * b)
            elif ch == "/":
                stack.push(a / b)
            elif ch == "^":
                stack.push(a ** b)
    return stack.pop()

expression = "1432^*+147--+"
print(evaluate_postfix(expression))

#q7

class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if not self.is_empty():
            return self.items.pop(0)

    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def is_palindrome(word):
    d = Deque()
    word = word.lower()

    for ch in word:
        d.add_rear(ch)

    while len(d.items) > 1:
        if d.remove_front() != d.remove_rear():
            return False

    return True


print(is_palindrome("Bob"))
print(is_palindrome("Navan"))
print(is_palindrome("False"))