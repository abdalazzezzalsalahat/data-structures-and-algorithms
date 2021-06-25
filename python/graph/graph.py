# from stacks_and_queues.stacks_and_queues import *
# import collections
from collections import deque
# from typing import List
# from sets import Set
# from stacks_and_queues.stacks_and_queues import Queue, Stack


class Queue():

    def __init__(self) -> None:
        """[summary]
        initializing a Queue object
        """
        self.dq = deque()
        
    def enqueue(self, value):
        """[summary]
        adding element to a Queue
        Args:
            value ([string]): [the value to be added into a queue]
        """
        self.dq.appendleft(value)

    def dequeue(self):
        """[summary]
        removing element from a Queue
        Returns:
            [string]: [the value of removed element]
        """
        return self.dq.pop()

    def __len__(self):
        """[summary]
        calculates the length of a Queue
        Returns:
            [int]: [length of a Queue]
        """
        return len(self.dq)

class Vertex:
    def __init__(self, value) -> None:
        """[summary]
        initializing a Graph Vertex (Node)
        Args:
            value ([string]): [value to be stored in a vertex]
        """
        self.value = value

class Edge:
    def __init__(self, vertix, wheight ) -> None:
        """[summary]
            initializing a connection (Graph Edge) between two vertcies
        Args:
            vertix ([type]): [description]
            wheight ([int]): [the wheight of an Edge]
        """
        self.vertix = vertix
        self.wheight = wheight

class Graph():

    def __init__(self):
        """[summary]
        initializing a private list of all vertcies
        """
        self._adjacency_list = {}

    def __str__(self):
        """[summary]
            a function to return list of nodsd in formated string format
        """
        pass

    def add_vertix(self, value):
        """[summary]
            function to add a new vertex to the graph
        Args:
            value ([string]): [value to pe stored in ]

        Returns:
            [type]: [description]
        """
        vert = Vertex(value)
        self._adjacency_list[vert] = []
        return vert

    def add_edge(self, start_vertix, end_vertix, weight = 0):
        """[summary]
            a function to add an Edge between two vertcies
        Args:
            start_vertix ([type]): [description]
            end_vertix ([type]): [description]
            weight (int, optional): [description]. Defaults to 0.

        Raises:
            KeyError: [description]
            KeyError: [description]
        """
        if start_vertix not in self._adjacency_list:
            raise KeyError("Starting point not found")

        if end_vertix not in self._adjacency_list:
            raise KeyError("Ending point not found")

        self._adjacency_list[start_vertix].append(Edge(end_vertix, weight))

    def size(self):
        """[summary]
            function to return the size of a Graph
        Returns:
            [int]: [description]
        """
        return len(self._adjacency_list)

    def find_all_paths(self, start_vertix):
        """[summary]
            a function to find all paths between all points
        Args:
            start_vertix ([type]): [description]
        """
        pass

    def shortest_path(self, start_vertix):
        """[summary]
            a function to find the shortest path between a starting point and ending point 
        Args:
            start_vertix ([type]): [description]
        """
        pass

    def get_neighbors(self, vertix):
        """[summary]
            to get al the neighbors of a vertex in a graph
        Args:
            vertix ([type]): [description]

        Returns:
            [type]: [description]
        """
        return self._adjacency_list.get(vertix, [])

    def get_nodes(self):
        """[summary]
            get all the nodes in a Graph
        Returns:
            [type]: [description]
        """
        return self._adjacency_list.keys()

    def BFS(self, start_vertix, action = (lambda x : None)):
        """[summary]
            Graph Breadth First Search function
        Args:
            start_vertix ([type]): [description]
            action (tuple, optional): [description]. Defaults to (lambda x : None).
        """
        # nods = List()
        queue = Queue()
        visited = set() ## Set(), [False] * (max(self.g) + 1)
        
        visited.add(start_vertix)
        queue.enqueue(start_vertix)

        while len(queue):
            currnt_ver = queue.dequeue()
            action(currnt_ver)
            neighbrs = self.get_neighbors(currnt_ver)
            # print(neighbrs)
            for edge in neighbrs:
                n_vert = edge.vertix

                if n_vert in visited:
                    continue
                else:
                    visited.add(n_vert)
                queue.enqueue(n_vert)





if __name__ == "__main__":
    g = Graph()
    one = g.add_vertix('ojsffvwi')
    two = g.add_vertix('ojsdb')
    three = g.add_vertix('ojsdbfpiieio')
    four = g.add_vertix('osd00000')
    g.add_edge(one, two)
    g.add_edge(one, four)
    g.add_edge(four, three)
    print(g.size())
    # print(g.get_nodes())
    g.BFS(one, lambda ver: print(ver.value))


