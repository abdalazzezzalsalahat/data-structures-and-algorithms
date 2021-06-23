import pytest
from hash.hash import Hashtable
from hash_join.hash_left_join import left_join_hash


def test_get(): ## 1
    one = Hashtable()
    one.add('fond','enamored')        
    one.add('wrath', 'anger')          
    one.add('diligent', 'employed')    
    one.add('outfit', 'garb')           
    one.add('guide', 'usher')

    assert one.find('fond') == 'enamored'

def test_contains(): ## 2
    one = Hashtable()
    one.add('fond','enamored')        
    one.add('wrath', 'anger')          
    one.add('diligent', 'employed')    
    one.add('outfit', 'garb')           
    one.add('guide', 'usher')

    assert one.contains('fond') == True

def test_left_join(): ## 3
    one = Hashtable()
    one.add('fond','enamored')        
    one.add('wrath', 'anger')          
    one.add('diligent', 'employed')    
    one.add('outfit', 'garb')           
    one.add('guide', 'usher')           

    two = Hashtable()
    two.add('fond', 'averse')
    two.add('wrath', 'delight')
    two.add('diligent', 'idle')
    two.add('guide', 'follow')
    two.add('flow', 'jam')
    assert left_join_hash(one, two) == "outfit: ['garb', None]\ndiligent: ['employed', 'idle']\nwrath: ['anger', 'delight']\nfond: ['enamored', 'averse']\nguide: ['usher', 'follow']"

def test_left_join_if_no_any_matching(): ## 4
    one = Hashtable()
    one.add('pond','enamored')        
    one.add('rath', 'anger')          
    one.add('adiligent', 'employed')    
    one.add('poutfit', 'garb')           
    one.add('hangguide', 'usher')           

    two = Hashtable()
    two.add('fond', 'averse')
    two.add('wrath', 'delight')
    two.add('diligent', 'idle')
    two.add('guide', 'follow')
    two.add('flow', 'jam')

    assert left_join_hash(one, two) == "hangguide: ['usher', None]\npond: ['enamored', None]\nrath: ['anger', None]\npoutfit: ['garb', None]\nadiligent: ['employed', None]"




