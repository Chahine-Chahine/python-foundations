'''Graphs and trees are fundamental data structures used in computer science and programming for various purposes.
They are often employed to represent and manipulate relationships between data elements. Here's an overview of graphs and trees:

Graphs:

A graph is a collection of nodes (vertices) connected by edges. Each edge represents a relationship or connection between two nodes.
Graphs come in various forms and can be categorized into different types based on their properties. Two common types of graphs are:

Directed Graph (Digraph): In a directed graph, each edge has a direction, indicating a one-way relationship between nodes.
It can be visualized as arrows pointing from one node to another.

Directed Graph

Undirected Graph: In an undirected graph, edges have no direction, and the relationships between nodes are bidirectional.

Undirected Graph

Common applications of graphs include representing networks, social connections, web pages and links, transportation routes, and more.
Graph traversal algorithms (e.g., depth-first search and breadth-first search) are frequently used to explore and analyze graphs'''



'''
Trees:

A tree is a specific type of graph that has the following characteristics:

Hierarchy: Trees are hierarchical data structures. 
They consist of nodes organized into levels or layers, with each node having a parent-child relationship, except for the root node, which has no parent.

Acyclic: Trees do not contain any cycles, meaning there are no closed loops or circular paths.

Single Root: There is a single designated root node that serves as the starting point for the tree.

Connected: All nodes in a tree are connected by edges, and there is a unique path between any two nodes.

No Cross-Edges: In a tree, there are no edges that connect nodes outside the hierarchical structure.

A few common types of trees include:

Binary Tree: Each node has at most two children, referred to as the left child and the right child.

Binary Search Tree (BST): A type of binary tree where nodes are organized such that for each node:

All nodes in its left subtree have values less than the node's value.
All nodes in its right subtree have values greater than the node's value.
Binary Search Tree

N-ary Tree: A tree in which each node can have more than two children.

Trees are commonly used for hierarchical data representation, file systems, organization structures, parsing expressions, and more. 
Various tree traversal algorithms (e.g., in-order, pre-order, post-order) are used for processing and analyzing tree structures.

'''

'''
🔍 Exploring BFS and DFS: Key Differences 🔄

Breadth-First Search (BFS) and Depth-First Search (DFS) are two fundamental graph traversal algorithms in computer science. 🌐

🔵 BFS explores nodes level by level and is perfect for finding the shortest path in unweighted graphs. It guarantees completeness and uses a queue for traversal.

🔴 DFS, on the other hand, delves as deep as possible down one branch before backtracking. While it's useful for tasks like topological sorting and cycle detection, it may not guarantee completeness, depending on the graph structure. DFS relies on a stack or recursion for traversal.

Understanding the differences between these two algorithms is crucial for effectively solving a wide range of graph-related challenges. 📊
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            current = self.root
            while current is not None:
                if data < current.data:
                    if current.left is None:
                        current.left = node
                        break
                    else:
                        current = current.left
                elif data >= current.data:
                    if current.right is None:
                        current.right = node
                        break
                    else:
                        current = current.right
        print(f"We added the node with value {data}")

    def search(self, data):
        if self.root is None:
            return "Tree is empty"
        current = self.root
        while current is not None:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            elif data >= current.data:
                current = current.right
        return False
#Deleting using pointers manipulation
    def findMinNode(self, node):
        while node.left is not None:
            node = node.left
        return node

   
#Deleting using swapping

    def delete(self, data):
        self.root = self.deleteRecursive(self.root, data)

    def deleteRecursive(self, root, data):
        if root is None:
            return root

        if data < root.data:
            root.left = self.deleteRecursive(root.left, data)
        elif data > root.data:
            root.right = self.deleteRecursive(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Find the in-order successor (the smallest node in the right subtree)
            temp = self.findMinNode(root.right)

            # Swap the data of the node to be deleted with the data of the in-order successor
            root.data = temp.data

            # Delete the in-order successor
            root.right = self.deleteRecursive(root.right, temp.data)

        return root

    def delete2(self, data):
            self.root = self.deleteRecursive(self.root, data)

            def deleteRecursive(self, root, data):
                if root is None:
                    return root

                if data < root.data:
                    root.left = self.deleteRecursive(root.left, data)
                elif data > root.data:
                    root.right = self.deleteRecursive(root.right, data)
                else:
                    if root.left is None:
                        return root.right
                    elif root.right is None:
                        return root.left

                    temp = self.findMinNode(root.right)
                    root.data = temp.data
                    root.right = self.deleteRecursive(root.right, temp.data)

                return root


 # Depth-First Search (DFS) Traversal (In-order)
    def dfs_traversal(self, node):
        if node is not None:
            # Visit the left subtree
            self.dfs_traversal(node.left)
            # Visit the current node
            print(node.data, end=" ")
            # Visit the right subtree
            self.dfs_traversal(node.right)

    # Breadth-First Search (BFS) Traversal
    def bfs_traversal(self):
        if self.root is None:
            print("Tree is empty")
            return

        queue = []
        queue.append(self.root)

        while queue:
            current = queue.pop(0)
            print(current.data, end=" ")

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

def main():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(8)
    bst.insert(3)
    bst.insert(18)
    bst.insert(9)
    bst.insert(12)
    bst.insert(6)
    bst.insert(25)

    print(bst.search(3))
    print("root is", bst.root.data)
    print(bst.root.left.left.data)

    bst.delete(8)  # Example of deleting a node
    print("After deleting 8:")
    print("root is", bst.root.data)
    print(bst.root.left.data)

    print("DFS Traversal (In-order):")
    bst.dfs_traversal(bst.root)
    print("\nBFS Traversal:")
    bst.bfs_traversal()

main()