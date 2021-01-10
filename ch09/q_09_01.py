class Node(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.node = None
        self.size = 0
    
    def add(self, value):
        self.size += 1

        if self.node is None:
            self.node = Node(value, None)
        else:
            node = self.node
            while node.next is not None:
                node = node.next
            node.next = Node(value, None)


    def remove(self, index):
        self.size -= 1

        if index == 0:
            value = self.node.value
            self.node = self.node.next
            return value    
        else:
            node1 = None
            node2 = self.node
            for _ in range(index):
                node1 = node2
                node2 = node2.next
            value = node2.value
            node1.next = node2.next
            return value


class Stack(object):
    def __init__(self):
        self.linked_list = LinkedList()
    
    def push(self, value):
        self.linked_list.add(value)
    
    def pop(self):
        return self.linked_list.remove(self.linked_list.size-1)

class Queue(object):
    def __init__(self):
        self.linked_list = LinkedList()

    def enqueue(self, value):
        self.linked_list.add(value)

    def dequeue(self):
        return self.linked_list.remove(0)


import unittest

class TestLinkedList(unittest.TestCase):
    def test_removeはi番目の要素を削除する(self):
        linked_list = LinkedList()
        linked_list.add('A')
        linked_list.add('B')
        linked_list.add('C')
        self.assertEqual(linked_list.remove(0), 'A')
        self.assertEqual(linked_list.remove(1), 'C')
        self.assertEqual(linked_list.remove(0), 'B')

class TestStack(unittest.TestCase):
    def test_LIFOを実現する(self):
        stack = Stack()
        stack.push('A')
        stack.push('B')
        stack.push('C')
        self.assertEqual(stack.pop(), 'C')
        self.assertEqual(stack.pop(), 'B')
        self.assertEqual(stack.pop(), 'A')

class TestQueue(unittest.TestCase):
    def test_FIFOを実現する(self):
        queue = Queue()
        queue.enqueue('A')
        queue.enqueue('B')
        queue.enqueue('C')
        self.assertEqual(queue.dequeue(), 'A')
        self.assertEqual(queue.dequeue(), 'B')
        self.assertEqual(queue.dequeue(), 'C')


if __name__ == '__main__':
    unittest.main(verbosity=2)