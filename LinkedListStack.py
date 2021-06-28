from SinglyLinkedList import LinkedList

class LinkedListStack:

  def __init__(self):
    self.ll_stack = LinkedList()

  def __str__(self):
    return f"<LinkedListStack, stack head: {self.ll_stack.head}>"

  def __repr__(self):
    return self.__str__()

  def push(self, new_data):
    """
    Adds `new_data` to the top of `ll_stack`.
    Time complexity: O(1) (constant).
    """
    self.ll_stack.prepend(new_data)
    print("Item added.")

  def pop(self):
    """
    Removes the item at the top of `ll_stack`.
    Time complexity: O(1) constant.
    Note: If we used `append` and `delete_from_tail` instead
    of `prepend` and `deleted_from_head`, then the complexity
    of `pop()` would be O(n) due to the way `SignlyLinkedList`
    is implemeneted.
    """
    self.ll_stack.delete_from_head()
    print("Item deleted.")

  def peek(self):
    """
    Returns whatever item is at the stack's top.
    Time complexity: O(1) (constant).
    """
    return self.ll_stack.head.data
