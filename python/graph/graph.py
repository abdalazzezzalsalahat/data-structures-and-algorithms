# from stacks_and_queues.stacks_and_queues import *
import collections
from collections import deque
from typing import List
# from sets import Set
# from stacks_and_queues.stacks_and_queues import Queue, Stack


class Queue():

    def __init__(self) -> None:
        self.dq = deque()
        
    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)

class Vertex:
    def __init__(self, value) -> None:
        self.value = value

class Edge:
    def __init__(self, vertix, wheight ) -> None:
        self.ertix = vertix
        self.wheight = wheight

class Graph():

    def __init__(self):
        self._adjacency_list = {}

    def __str__(self, vertix):
        pass

    def add_vertix(self, value):
        vert = Vertex(value)
        self._adjacency_list[vert] = []
        return vert

    def add_edge(self, start_vertix, end_vertix, weight = 0):

        if start_vertix not in self._adjacency_list:
            raise KeyError("Starting point not found")

        if end_vertix not in self._adjacency_list:
            raise KeyError("Ending point not found")

        self._adjacency_list[start_vertix].append(Edge(end_vertix, weight))

    def size(self):
        return len(self._adjacency_list)

    def find_all_paths(self, start_vertix):
        pass

    def shortest_path(self, start_vertix):
        pass

    def get_neighbors(self, vertix):
        return self._adjacency_list.get(vertix, [])

    def get_nodes(self):
        return self._adjacency_list.keys()

    def BFS(self, start_vertix, action = (lambda x : None)):
        # nods = List()
        queue = Queue()
        visited = {} ## Set(), [False] * (max(self.g) + 1)
        visited[start_vertix] = True
        queue.enqueue(start_vertix)
        # visited.add(start_vertix)

        while len(queue):
            currnt_ver = queue.dequeue()
            action(currnt_ver)
            neighbrs = self.get_neighbors(currnt_ver)
            print(neighbrs)
            for edge in neighbrs:
                n_vert = edge

                if n_vert in visited:
                    continue
                else:
                    visited[n_vert] = True
                queue.enqueue(n_vert)

        # return nods

if __name__ == "__main__":
    g = Graph()
    one = g.add_vertix('ojsffvwi')
    two = g.add_vertix('ojsdb')
    three = g.add_vertix('ojsdbfpiieio')
    four = g.add_vertix('osd00000')
    g.add_edge(one, two)
    g.add_edge(one, four)
    g.add_edge(four, two)
    g.add_edge(three, two)
    g.add_edge(three, four)
    print(g.size())
    print(g.get_nodes())
    g.BFS(one, lambda ver: print(ver))


