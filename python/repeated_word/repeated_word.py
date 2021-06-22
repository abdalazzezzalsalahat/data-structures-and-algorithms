import re 
from collections import defaultdict
from .hash import Hashtable


def repeated_word_using_hashmap(sentance):
    hash = Hashtable()

    w_lst = re.findall(r'\w+', sentance)

    for word in w_lst:
        lwr_word = word.lower()
        if not hash.contains(lwr_word):
            hash.add(lwr_word, 'word')
        else:
            return lwr_word






if __name__ == "__main__":

    string = "Once upon a time, there was a brave princess who..."
    mult_str = """
    It was the best of times, 
    it was the worst of times, 
    it was the age of wisdom, 
    it was the age of foolishness, 
    it was the epoch of belief, 
    it was the epoch of incredulity, 
    it was the season of Light, 
    it was the season of Darkness, 
    it was the spring of hope, 
    it was the winter of despair, 
    we had everything before us, 
    we had nothing before us, 
    we were all going direct to Heaven, 
    we were all going direct the other way – in short, 
    the period was so far like the present period, 
    that some of its noisiest authorities insisted on its being received, 
    for good or for evil, 
    in the superlative degree of comparison only..."""
    last_str = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."

    print(repeated_word_using_hashmap(string))
    print("\n\n\n")
    print(repeated_word_using_hashmap(mult_str))
    print("\n\n\n")
    print(repeated_word_using_hashmap(last_str))



