from hash.hash import *

def unique (string):
    string = string.replace(" ", "")
    string = string.lower()
    hash_map = Hashtable()
     
    for key in string:
        if hash_map.contains(key):
            return False
        hash_map.add(key, '0')
    return True

if __name__ == "__main__":
    
    print(unique('I love cats'))
    print(unique('The quick brown fox jumps over the lazy dog'))
    print(unique('Donald the duck'))



