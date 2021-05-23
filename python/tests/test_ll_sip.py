from python.linked_list.ll_zip import LinkedList
import pytest



def test_zipLists():
    new_list = LinkedList() 
    new_list.append(3) 
    new_list.append(2) 
    new_list.append(1) 
    new_list2 = LinkedList() 
    new_list2.append(8) 
    new_list2.append(7) 
    new_list2.append(6)
    assert LinkedList.zipLists(new_list,new_list2) == "{'6'} ->{'1'} ->{'7'} ->{'2'} ->{'8'} ->{'3'} ->"

def test_zipLists2():
    llist1 = LinkedList() 
    llist1.append(3) 
    llist1.append(2) 
    llist1.append(1) 
    llist1.append(0) 
    llist1.append(0) 
    llist2 = LinkedList() 
    llist2.append(8) 
    llist2.append(7) 
    llist2.append(6)
    assert LinkedList.zipLists(llist1,llist2) == "{'0'} ->{'6'} ->{'0'} ->{'7'} ->{'1'} ->{'8'} ->{'2'} ->{'3'} ->"

def test_zipLists3(): 
    llist1 = LinkedList() 
    llist1.append(3) 
    llist1.append(2) 
    llist1.append(1) 
    llist2 = LinkedList() 
    llist2.append(8) 
    llist2.append(7) 
    llist2.append(6)
    llist2.append(5) 
    llist2.append(5)
    assert LinkedList.zipLists(llist1,llist2) == "{'5'} ->{'1'} ->{'5'} ->{'2'} ->{'6'} ->{'3'} ->{'7'} ->{'8'} ->"



