'''A queue is a linear data structure in computer science that follows the First-In-First-Out (FIFO) principle.
 In a queue, the first element added (enqueued) is the first one to be removed (dequeued).
 Think of it as a real-life queue of people waiting in line; the person who arrived first is the first one to be served and leave the queue.

Queues are used to manage data or tasks in a sequential order, where the order of processing is critical. 
They find applications in various computer science and software engineering scenarios, including job scheduling,
 task management, print spooling, and breadth-first search algorithms.'''

#Here is an implimentation of a Normal Queue and a priority queue:
#It needs two classes to work the first class is Node the other for the queue itself

#Queue implimentation using linked list
class Node:
  def __init__(self,info):
    self.info = info
    self.next = None

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def displayNode(self):
    current = self.head
    while current != None:
      print(current.info)
      current = current.next

  def isEmpty(self):
    return self.head == None
#How to add to a QUEUE
  def enqueue(self, value):
    node = Node(value)
    if self.isEmpty():
      self.head = node
      self.tail = node
      self.size += 1
    else:
      self.tail.next= node
      self.tail = node
      self.size += 1
#How to DELETE from a QUEUEs
  def dequeue(self):
    if self.isEmpty():
      return "The queue is already empty"
    if self.size == 1:
      self.head = None
      self.tail = None
      self.size -= 1
    else:
      current = self.head
      self.head = current.next
      current.next = None
      self.size -= 1

#-------------------------------------------------------------
class PriorityQueue:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def displayNodes(self):
    current = self.head
    while current != None:
      print(current.info)
      current = current.next

  def isEmpty(self):
    return self.head == None

  def enqueue(self,value):
    node = Node(value)
    if self.isEmpty():
      self.head = node
      self.tail = node
      self.size += 1
    else:
      if node.info < self.head.info:
        node.next = self.head
        self.head = node
        self.size += 1
      else:
        current = self.head
        previous = current
        while current != None and current.info <= node.info:
          previous = current 
          current = current.next
        if current == None :
          self.tail = node

        previous.next = node
        node.next = current
        self.size += 1
      

  def dequeue(self):
    if self.isEmpty():
      return "PQ is already empty"
    elif self.size == 1 :
      self.head = Node
      self.tail = Node
      self.size -= 1
    else:
      current = self.head
      self.head = self.head.next
      current.next = None
      self.size -= 1
#--------------------------------------------------------

def main():
  print("Queue")
  queue = Queue()
  queue.enqueue(16)
  queue.enqueue(5)
  queue.enqueue(53)
  queue.enqueue(45)
  queue.displayNode()
  queue.dequeue()
  queue.displayNode()
  queue.dequeue()
  queue.displayNode()
  queue.dequeue()
  queue.displayNode()
  print("--------------------------------")
  print("PQ")
  pq = PriorityQueue()
  pq.enqueue(19)
  pq.displayNodes()
  pq.enqueue(26)
  pq.displayNodes()
  pq.enqueue(8)
  pq.displayNodes()
  pq.enqueue(12)
  pq.displayNodes()
  pq.enqueue(59)
  pq.displayNodes()
  pq.enqueue(35)
  pq.displayNodes()
  print("Dequeueing")
  pq.dequeue()
  pq.displayNodes()
  pq.dequeue()
  pq.displayNodes()
  pq.dequeue()
  pq.displayNodes()
  pq.dequeue() 
  print("---------------------------------")
  
main()