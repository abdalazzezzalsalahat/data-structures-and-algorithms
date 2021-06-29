from graph.graph import *
import pytest



# 1) Node can be successfully added to the graph ###

# 2) An edge can be successfully added to the graph ###

# 3) A collection of all nodes can be properly retrieved from the graph ###

# 4) All appropriate neighbors can be retrieved from the graph ###

# 5) Neighbors are returned with the weight between nodes included ###

# 6) The proper size is returned, representing the number of nodes in the graph ###

# 7) A graph with only one node and edge can be properly returned ###

# 8) An empty graph properly returns null ###

# 9) Test Breadth First Search ### 

@pytest.fixture
def vertix_fixture():
    v = Vertex("one")
    return v

@pytest.fixture
def graph_fexture():
    g = Graph()
    one = g.add_vertix('one')
    two = g.add_vertix('two')
    three = g.add_vertix('three')
    four = g.add_vertix('four')
    five = g.add_vertix('five')

    g.add_edge(one, two)
    g.add_edge(two, one)

    g.add_edge(one, three)
    g.add_edge(three, one)

    g.add_edge(three, three)
    g.add_edge(four, three)

    g.add_edge(three, four)
    g.add_edge(two, three)

    g.add_edge(three, two)
    g.add_edge(two, four)

    g.add_edge(four, two)
    g.add_edge(one, five)
    
    g.add_edge(four, five)
    g.add_edge(five, four)
    return g

@pytest.fixture
def DFS_fixture():
    gl = Graph()

    A = gl.add_vertix('A')
    B = gl.add_vertix('B')
    C = gl.add_vertix('C')
    G = gl.add_vertix('G')
    D = gl.add_vertix('D')
    E = gl.add_vertix('E')
    H = gl.add_vertix('H')
    F = gl.add_vertix('F')

    gl.add_edge(A, B)
    gl.add_edge(A, D)
    gl.add_edge(B, C)
    gl.add_edge(C, G)
    gl.add_edge(D, E)
    gl.add_edge(D, H)
    gl.add_edge(D, F)
    gl.add_edge(H, F)

    gl.add_edge_reverced(A, B)
    gl.add_edge_reverced(A, D)
    gl.add_edge_reverced(B, C)
    gl.add_edge_reverced(C, G)
    gl.add_edge_reverced(D, E)
    gl.add_edge_reverced(D, H)
    gl.add_edge_reverced(D, F)
    gl.add_edge_reverced(H, F)

    return gl

def test_add_vertix(): ## 1
    """
    Node can be successfully added to the graph
    """
    
    graph = Graph()
    actual = graph.add_vertix('testing').value
    expected = 'testing' 
    assert actual == expected

def test_add_edge_start(): ## 2 ## 1
    """[summary]
    An edge can be successfully added to the graph
    """
    g = Graph()
    one = g.add_vertix('one')
    two = g.add_vertix('two')
    g.add_edge(one, two)

def test_add_edge_other_case():  ## 2 ## 2
    
    g = Graph()
    one = g.add_vertix('one')
    two = g.add_vertix('two')
    g.add_edge(two, one)
    
def test_size(graph_fexture): ## 3
    """[summary]
        test if the Graph size is as expected
    Args:
        graph_fexture ([function]): [fuxture function]
    """
    expected = 5
    actual = graph_fexture.size()
    assert actual == expected

def test_get_neighbors(graph_fexture, vertix_fixture): ## 4
    """[summary]
        All appropriate neighbors can be retrieved from the graph
    Args:
        graph_fexture ([type]): [description]
    """
    one = graph_fexture.add_vertix('one')
    two = graph_fexture.add_vertix('two')
    test = graph_fexture.add_vertix("test")
    graph_fexture.add_edge(test, one)
    graph_fexture.add_edge(test, two)
    lst = []
    n = graph_fexture.get_neighbors(test)
    for edge in n: 
        lst.append(edge.vertix.value)
    
    expected = ['one','two']
    actual = lst
    assert actual == expected

def test_neighbors_with_weight_between_nodes(graph_fexture): ## 5
    """[summary]
        Neighbors are returned with the weight between nodes included
    Args:
        graph_fexture ([type]): [description]
    """
    one = graph_fexture.add_vertix('one')
    two = graph_fexture.add_vertix('two')
    test = graph_fexture.add_vertix("test")
    graph_fexture.add_edge(test, one, 5)
    graph_fexture.add_edge(test, two, 2)

    expected = {('one', 5),('two', 2)}
    actual = graph_fexture.get_tuple_neighbors(test)
    assert actual == expected

def test_size_neighbors(graph_fexture): ## 6
    """[summary]
        The proper size is returned, representing the number of nodes in the graph
    Args:
        graph_fexture ([type]): [description]
    """
    test = graph_fexture.add_vertix("test")
    two = graph_fexture.add_vertix("two")
    
    graph_fexture.add_edge(test, two)

    actual = graph_fexture.get_tuple_neighbors(test)
    expected = {'two'}
    assert actual == expected

def test_one_node_and_one_edge(): ## 7
    """[summary]
        A graph with only one node and edge can be properly returned
    """
    g = Graph()
    test = g.add_vertix("test")

    g.add_edge(test, test, 5)
    actual = g.get_tuple_neighbors(test)
    expected = {("test", 5)}
    assert g.size() == 1
    assert actual == expected

def test_empty_graph(): ## 8
    """[summary]
    An empty graph properly returns null
    """
    g = Graph()
    expected = 'Graph is empty'
    actual = g.size()
    assert actual == expected

####################################################   BFS   ###########################################################

def test_BFS(): ## 9
    """[summary]
    testing the BFS
    """
    g = Graph()
    Pandora = g.add_vertix('Pandora')
    Arendelle = g.add_vertix('Arendelle')
    Metroville = g.add_vertix('Metroville')
    Monstroplolis = g.add_vertix('Monstroplolis')
    Narnia = g.add_vertix('Narnia')
    Naboo = g.add_vertix('Naboo')
    
    g.add_edge(Pandora, Arendelle)
    g.add_edge(Arendelle, Metroville)
    g.add_edge(Arendelle, Monstroplolis)
    g.add_edge(Metroville, Monstroplolis)
    g.add_edge(Metroville, Narnia)
    g.add_edge(Metroville, Naboo)

    expected = {'Naboo', 'Monstroplolis', 'Arendelle', 'Pandora', 'Metroville', 'Narnia'}
    lst = set()
    g.BFS(Pandora, lambda ver: lst.add(ver.value))
    actual = lst
    assert actual == expected

####################################################   DFS   ###########################################################

def test_DFS(DFS_fixture): ## 10 
    """[summary]

    """

    assert DFS_fixture.DFS() == ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']



