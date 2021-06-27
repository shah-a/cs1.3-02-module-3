from LinkedListStack import LinkedListStack
from LinkedListQueue import LinkedListQueue

def test_stack_methods():
  ll_stack = LinkedListStack()

  ll_stack.push(5)
  ll_stack.push(10)
  ll_stack.push(30)

  assert ll_stack.peek() == 30

  ll_stack.pop()
  ll_stack.pop()

  assert ll_stack.peek() == 5
  

def test_queue_methods():
  ll_queue = LinkedListQueue()

  ll_queue.enqueue(5)
  ll_queue.enqueue(10)
  ll_queue.enqueue(30)

  assert ll_queue.front() == 5

  ll_queue.dequeue()
  ll_queue.dequeue()

  assert ll_queue.front() == 30