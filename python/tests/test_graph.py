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

    expected = [('one', 5),('two', 2)]
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
    expected = ['two']
    assert actual == expected

def test_one_node_and_one_edge(): ## 7
    """[summary]
        A graph with only one node and edge can be properly returned
    """
    g = Graph()
    test = g.add_vertix("test")

    g.add_edge(test, test, 5)
    actual = g.get_tuple_neighbors(test)
    expected = [("test", 5)]
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


