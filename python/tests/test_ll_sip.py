from linked_list.ll_zip import LinkedList, zipLists
import pytest



def test_zipLists(): ## 1
    new_list = LinkedList() 
    new_list.append(3) 
    new_list.append(2) 
    new_list.append(1) 
    new_list2 = LinkedList() 
    new_list2.append(8) 
    new_list2.append(7) 
    new_list2.append(6)
    assert zipLists(new_list,new_list2) == "{'3'} ->{'8'} ->{'2'} ->{'7'} ->{'1'} ->{'6'} ->"

def test_zipLists2(): ## 2
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
    assert zipLists(llist1,llist2) == "{'3'} ->{'8'} ->{'2'} ->{'7'} ->{'1'} ->{'6'} ->{'0'} ->{'0'} ->"

def test_zipLists3(): ## 3
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
    assert zipLists(llist1,llist2) == "{'3'} ->{'8'} ->{'2'} ->{'7'} ->{'1'} ->{'6'} ->{'5'} ->{'5'} ->"

