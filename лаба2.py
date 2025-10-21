#пример использования мультисписка
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
class MultiList:
    def __init__(self):
        self.root = None
    def add_child(self, parent, child):
        parent.children.append(child)
# Пример использования
root = Node("Root")
child1 = Node("Child 1")
child2 = Node("Child 2")
multi_list = MultiList()
multi_list.root = root
multi_list.add_child(root, child1)
multi_list.add_child(root, child2)

#пример использования очереди
rom collections import deque
queue = deque()
queue.append(1)  # Добавление элемента
queue.append(2)
print(queue.popleft())  # Удаление и вывод первого элемента

#пример использования дек
from collections import deque
deque_example = deque()
deque_example.append(1)  # Добавление в конец
deque_example.appendleft(2)  # Добавление в начало
print(deque_example.pop())  # Удаление и вывод последнего элемента

#пример использования приоритетной очереди
import heapq
priority_queue = []
heapq.heappush(priority_queue, (1, 'task 1'))  # (приоритет, задача)
heapq.heappush(priority_queue, (0, 'task 2'))
print(heapq.heappop(priority_queue))  # Удаление и вывод элемента

