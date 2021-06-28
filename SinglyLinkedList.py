class Node:

  def __init__(self, data):
    self.data = data
    self.next = None

  def __str__(self):
    return f"<Node, data: {self.data}>"

  def __repr__(self):
    return self.__str__()

class LinkedList:
  """Implements a basic linked list"""

  def __init__(self):
    self.head = None
    self.tail = None

  def __str__(self):
    return f"<LinkedList, head: {self.head}, tail: {self.tail}>"

  def __repr__(self):
    return self.__str__()

  def append(self, new_data):
    

    new_node = Node(new_data)

    if self.head == None:
      self.head = new_node
      self.tail = new_node
      return

    self.tail.next = new_node
    self.tail = new_node

  def prepend(self, new_data):
    new_node = Node(new_data)

    if self.head == None:
      self.head = new_node
      self.tail = new_node
      return

    new_node.next = self.head
    self.head = new_node

  def delete_from_head(self):
    self.head = self.head.next

  def delete_from_tail(self):
    
    current = self.head
    #get the node right before the tail
    while current != None:
      if current.next == self.tail:
        break
      current = current.next
    self.tail = current
    current.next = None

  def print_list(self):
    current = self.head
    while current != None:
      print(current.data)
      current = current.next