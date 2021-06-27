from collections import deque, defaultdict

from _pytest import capture


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
    def __init__(self, vertix, weight ) -> None:
        """[summary]
            initializing a connection (Graph Edge) between two vertcies
        Args:
            vertix ([type]): [description]
            weight ([int]): [the weight of an Edge]
        """
        self.vertix = vertix
        self.weight = weight

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
        res = "Vertices: "
        for vert in self._adjacency_list:
            res += str(vert) + " "
        return res

    def __iter__(self):
        """[summary]
            magic function to iterate over the Graph
        Returns:
            [type]: [description]
        """
        self._iter_obj = iter(self._adjacency_list)
        return self._iter_obj

    def __next__(self):
        """[summary]
        magic function to iterate over vertices
        """
        return next(self._iter_obj)

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
        if len(self._adjacency_list):
            return len(self._adjacency_list)
        return 'Graph is empty'

    def get_neighbors(self, vertix):
        """[summary]
            to get al the neighbors of a vertex in a graph
        Args:
            vertix ([type]): [description]

        Returns:
            [type]: [description]
        """
        return self._adjacency_list.get(vertix, [])

    def get_tuple_neighbors(self, vertix):
        """[summary]
            a function to return a tuple of all neighbors with their weights
        Args:
            vertix ([type]): [description]

        Raises:
            KeyError: [description]

        Returns:
            [type]: [description]
        """
        lst = []
        n = self.get_neighbors(vertix)
        if n: 

            for edge in n:

                if edge.weight:
                    lst.append((str(edge.vertix.value), edge.weight))

                else:
                    lst.append(str((edge.vertix.value)))

            return lst

        raise KeyError("No neighbors found")

    def get_vertices(self):
        """[summary]
            get all the nodes in a Graph
        Returns:
            [type]: [description]
        """
        return self._adjacency_list.keys()

    def get_edge(self, vertix):
        """[summary]
            returns a list of all the edges of a vertice
        Args:
            vertix ([type]): [description]

        Returns:
            [list]: [all edges of a vertix]
        """
        return self._adjacency_list[vertix]

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

    def DFS(self, start_vertix, action = (lambda x : None)):
        """[summary]
            tree
        Args:
            start_vertix ([type]): [description]
            action (tuple, optional): [description]. Defaults to (lambda x : None).
        """
        visited = set()
        visited.add(start_vertix)
        neighbrs = self.get_neighbors(start_vertix)

        for vertix in neighbrs:
            action(start_vertix)

            if vertix not in visited:
                self.DFS(vertix)
                visited.add(vertix)

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

    def get_neighbors_second(self,vertex):
        result = []
        if len(self._adjacency_list.get(vertex)):
            # print('whats wront with', self._adjacency_list.get(vertex))
            for l in range(len(self._adjacency_list.get(vertex))):
                result.append([self._adjacency_list.get(vertex)[l].vertix.value,
                            self._adjacency_list.get(vertex)[l].weight])
        return result





if __name__ == "__main__":
    g = Graph()
    one = g.add_vertix('one')
    two = g.add_vertix('two')
    three = g.add_vertix('three')
    four = g.add_vertix('four')
    five = g.add_vertix('five')
    
    g.add_edge(one, two)
    g.add_edge(two, one, 5)

    g.add_edge(one, three)
    g.add_edge(three, one, 2)
    g.add_edge(three, three)
    
    g.add_edge(four, three)
    g.add_edge(three, four, 7)
    
    g.add_edge(two, three)
    g.add_edge(three, two, 4)
    
    g.add_edge(two, four)
    g.add_edge(four, two, 3)

    g.add_edge(one, five)
    g.add_edge(four, five)
    g.add_edge(five, five, 5)

    gs = Graph()

    Pandora = gs.add_vertix('Pandora')
    Arendelle = gs.add_vertix('Arendelle')
    Metroville = gs.add_vertix('Metroville')
    Monstroplolis = gs.add_vertix('Monstroplolis')
    Narnia = gs.add_vertix('Narnia')
    Naboo = gs.add_vertix('Naboo')
    
    gs.add_edge(Pandora, Arendelle)
    gs.add_edge(Arendelle, Metroville)
    gs.add_edge(Arendelle, Monstroplolis)
    gs.add_edge(Metroville, Monstroplolis)
    gs.add_edge(Metroville, Narnia)
    gs.add_edge(Metroville, Naboo)

    print(gs.BFS(Pandora, lambda ver: None))
    # print(g.size())
    # print(g.get_vertices())
    # g.BFS(four, lambda ver: print(ver.value))

    # g.DFS(four, lambda ver: print(ver.value))

    # print(next(g))



