from SinglyLinkedList import LinkedList

class LinkedListQueue:

  def __init__(self):
    self.ll_queue = LinkedList()

  def enqueue(self, new_data):
    """
    Enqueues `new_data` to the back of `ll_queue`.
    Time complexity: O(1) (constant).
    """
    self.ll_queue.append(new_data)
    # print("Item enqueued.")

  def dequeue(self):
    """
    Dequeues the item at the front of `ll_queue`.
    Time complexity: O(1) constant.
    Note: If we used `prepend` and `delete_from_tail` instead
    of `append` and `delete_from_head`, then the complexity
    of `dequeue()` would be O(n) due to the way `SignlyLinkedList`
    is implemeneted.
    """
    self.ll_queue.delete_from_head()
    # print("Item dequeued.")

  def front(self):
    """
    Returns whatever item is at the queue's front.
    Time complexity: O(1) (constant).
    """
    return self.ll_queue.head.data
