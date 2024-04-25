queue1 = []
queue1.append("name")
queue1.append("age")
queue1.append("phone number")
queue1.append("country")
print(queue1)

#removing elements from a queue
queue1.pop(0)
print(queue1.pop(0))

#implementation of queue.Queue
from queue import Queue
q = Queue(maxsize = 4)

#inserting elements
q.put(10)
q.put(20)
q.put(30)
q.put(40)

#checking if the queue if full
print(q.full())

#checking if the queue is empty
print(q.empty())

#removing an element from the queue
print(q.get())