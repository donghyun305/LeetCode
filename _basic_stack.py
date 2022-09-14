stack = [3,4,5]
stack.append(6)
stack.pop()
print(stack)

from collections import deque

queue =deque([1,2,3])
queue.append(4)
queue.popleft()
queue.pop()
print(queue)

tuple = (123, 456, 'abc')
print(tuple[0])