'''
A linked list is a linear data structure made up of nodes, where each node contains two parts: data and a reference (or link) to the next node in the sequence.
 Linked lists are used to represent sequences of elements and are particularly useful when you need dynamic memory allocation, such as when elements are frequently added or removed.
   There are different types of linked lists, including singly linked lists, doubly linked lists, and circular linked lists.

Here are some key concepts and operations related to linked lists:

Node: Each element in a linked list is represented by a node. 
A node typically contains data and a reference (or link) to the next node (and, in the case of doubly linked lists, to the previous node as well).

Head: The first node in the linked list is called the head. It serves as the starting point for traversing the list.

Tail: The last node in the linked list is called the tail.
 In singly linked lists, the tail's reference is usually set to None. In doubly linked lists, the tail points to the previous node.

Singly Linked List: In a singly linked list, each node has a reference to the next node only.

Doubly Linked List: In a doubly linked list, each node has references to both the next node and the previous node.

Circular Linked List: In a circular linked list, the last node's reference points back to the head, creating a loop.
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# A singly linked list class 
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def isEmpty(self):
        return self.head == None
    
    def display(self):
        if self.isEmpty():
            print("Linked list is empty, there is nothing to display")
        else:
            current = self.head
            while current != None:
                print(current.data)
                current = current.next
    
    def add(self, data):
        node = Node(data)
        if self.isEmpty():
            self.head = node
            self.size += 1
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
            self.size += 1

    def remove(self, value):
        if self.isEmpty():
            print("The list is empty, there is nothing to remove")
        current = self.head
        previous = current
        while current.next != None:
            previous = current
            current = current.next
            if self.head.data == value:
              self.head = self.head.next
              self.size -= 1
            elif current.data == value:
              previous.next = current.next
              self.size -= 1
        return print(f"All instances of the number {value} have been removed!")
    

def main():
    singly_list = LinkedList()
    singly_list.add(7)
    singly_list.add(9)
    singly_list.add(23)
    singly_list.add(4)
    singly_list.add(66)
    singly_list.add(8)
    singly_list.display()
    singly_list.remove(8)
    singly_list.display()

main()