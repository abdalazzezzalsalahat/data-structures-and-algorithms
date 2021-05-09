from linked_list.linked_list import LinkedList


def test_import():
    assert LinkedList

def test_instance():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert isinstance(ll, LinkedList)

def append() : 
    m_m=LinkedList
    m_m.append(2)
    m_m.append(3)
    m_m.append(4)
    acepted = "{'2'} ->{'3'} ->{'4'} ->"
    actual = m_m()

def test_insert():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    result = ''
    linked_list = ll.head
    while linked_list:
        result += f'{linked_list.value},'
        linked_list = linked_list.next
    assert result == '1,2,3,'

def test_head():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.head.value == 1

def test_false():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.includes(5) == False

def test_true():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.includes(2) == True

def test_str():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.__str__() == "-> {'1'} -> {'2'} -> {'3'} "
