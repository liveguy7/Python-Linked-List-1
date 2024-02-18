
class Node:

  def __init__(self, data=None):
    self.data = data
    self.next = None

class Head:

  def __init__(self):
    self.head = None

  def print(self):
    h = self.head
    while h is not None:
      print(h.data)
      h = h.next

  def insert(self, newdata):
    newNode = Node(newdata)
    newNode.next = self.head
    self.head = newNode

pointer = Head()
pointer.head = Node('90')
p2 = Node('9')
p3 = Node('3')

pointer.head.next = p2
p2.next = p3

pointer.insert('1')
pointer.print()














