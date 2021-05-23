from linked_list.linked_list import LinkedList


def test_instance(): ## 1 ## 1
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert isinstance(ll, LinkedList)

def append(): ## 1 ## 2
    m_m = LinkedList
    m_m.append(2)
    m_m.append(3)
    m_m.append(4)
    expected = "{'2'} ->{'3'} ->{'4'} ->"
    actual = m_m()
    assert expected == actual

def test_insert(): ## 1 ## 3
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    result = ''
    linked_list = ll.head
    while linked_list:
        result += f'{linked_list.value},'
        linked_list = linked_list.next
    assert result == '3,2,1,'

def test_fisrt_elment(): ## 1 ## 4
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.head.value == 3

def test_false_value(): ## 1 ## 5
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.includes(5) == False

def test_true(): ## 1 ## 6
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.includes(2) == True

def test_str(): ## 1 ## 7
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.__str__() == "{'3'} ->{'2'} ->{'1'} ->"

####################################################################

def test_insert_before(): ## 2  ## 1
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert_before(2,3)
    assert ll.__str__() == "{'3'} ->{'2'} ->{'1'} ->"

def test_insert_before_head(): ## 2  ## 2
    ll = LinkedList()
    ll.append(5)
    ll.append(6)
    ll.insert_before(5,4)
    assert ll.__str__() == "{'4'} ->{'5'} ->{'6'} ->"

def test_insert_after_last(): ## 2  ## 3
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_after(3,4)
    assert ll.__str__() == "{'1'} ->{'2'} ->{'3'} ->{'4'} ->"

def test_insert_after(): ## 2  ## 4
    ll = LinkedList()
    ll.insert(5)
    ll.append(6)
    ll.insert_after(6,8)
    ll.insert(7)
    assert ll.__str__() == "{'7'} ->{'5'} ->{'6'} ->{'8'} ->"

#####################################################################

def test_LinkedList_kth_from(): ## 3  ## 1
    ll = LinkedList()
    ll.insert(2)
    ll.insert(8)
    ll.insert(3)
    ll.insert(1)
    actual = ll.kth_from_end(0)
    expected = 2
    assert actual == expected

def test_LinkedList_kth(): ## 3  ## 2
    ll = LinkedList()
    ll.insert(2)
    ll.insert(8)
    ll.insert(3)
    ll.insert(1)
    actual = ll.kth_from_end(2)
    expected = 3
    assert actual == expected

def test_check_last_value(): ## 3  ## 3
    li = LinkedList()
    li.append(1)
    li.append(2)
    li.append(3)
    expected = 1
    actual = li.kth_from_end(3)
    assert actual == expected

def test_linked_list_size_1(): ## 3  ## 4
    li = LinkedList()
    li.append(1)
    actual = li.kth_from_end(1)
    expected = 1    
    assert actual == expected

def test_value_in_the_middle(): ## 3 ## 5
    li = LinkedList()
    li.append(1)
    li.append(2)
    li.append(3)
    actual = li.kth_from_end(2)
    expected = 1
    assert actual == expected 

###################################

def test_value_zero(): ## 4 ## 1
    li = LinkedList()
    li.append(1)
    li.append(2)
    li.append(3)
    actual = li.kth_from_end(-1)
    expected = 'index can\'t be less the zero'
    assert actual == expected 

def test_value_not_exist(): ## 4 ## 2
    li = LinkedList()
    li.append(1)
    li.append(2)
    li.append(3)
    actual = li.kth_from_end(5)
    expected = 'index not found'
    assert actual == expected 

#####################################################################

def test_LinkedList_kth_from_second(): ## 5 ## 1
    ll = LinkedList()
    ll.insert(2)
    ll.insert(8)
    ll.insert(3)
    ll.insert(1)
    actual = ll.kth_from_end_second(0)
    expected = 1
    assert actual == expected

def test_LinkedList_kth_second(): ## 5 ## 2
    ll = LinkedList()
    ll.insert(2)
    ll.insert(8)
    ll.insert(3)
    ll.insert(1)
    actual = ll.kth_from_end_second(2)
    expected = 8
    assert actual == expected

def test_check_last_value_second(): ## 5 ## 3
    li = LinkedList()
    li.append(1)
    li.append(2)
    li.append(3)
    expected = None
    actual = li.kth_from_end_second(3)
    assert actual == expected

def test_linked_list_size_1_second(): ## 5 ## 4
    li = LinkedList()
    li.append(1)
    actual = li.kth_from_end_second(1)
    expected = None    
    assert actual == expected

def test_value_in_the_middle_second(): ## 5 ## 5
    li = LinkedList()
    li.append(1)
    li.append(2)
    li.append(3)
    actual = li.kth_from_end_second(2)
    expected = 3
    assert actual == expected 
