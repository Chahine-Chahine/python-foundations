'''A stack is another essential linear data structure in computer science, following the Last-In-First-Out (LIFO) principle.
 In a stack, the last element added is the first one to be removed.
 Think of it as a stack of books; the book you placed on top most recently is the one you'll remove first.

Stacks are used to manage data or tasks in a sequential order, where the order of processing is crucial, but the focus is on the most recently added item. 
They find applications in various computer science and software engineering scenarios, including function call management (call stack), undo functionality, 
and expression evaluation.'''


class Node:
  def __init__(self,info):
    self.info = info
    self.next = None

class Stack:
  def __init__(self):
    self.head = None
    self.size = 0

  def isEmpty(self):
    return self.head == None
# How to add to a Stack
  def push(self, value):
    print(f"pushing {value}")
    node = Node(value)
    node.next = self.head
    self.head = node
    self.size += 1
# How to delete from a Stack
  def pop(self):
    print(f"popping {self.head.info}")
    if self.isEmpty():
      return "stack is already empty"
    else:
      current = self.head
      self.head = self.head.next
      current.next = None
      self.size -= 1


def main():
  s = Stack()
  s.push(1)
  s.push(7)
  s.push(3)
  s.push(17)
  s.pop()
  s.pop()
  s.pop()
main()