from design_circular_deque import MyCircularDeque
k = 3
m = MyCircularDeque(k)
print(m.insertLast(1))
print(m.insertLast(2))
print(m.insertFront(3))
print(m.insertFront(4))
print(m.getRear())
print(m.isFull())
print(m.deleteLast())
print(m.insertFront(4))
print(m.getFront())
