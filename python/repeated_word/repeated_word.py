
from collections import defaultdict
 
def first_repeating_word(sentence):
    """[summary]
    a funcction to calculate the most repeated words in a string
    Args:
        sentence ([string]): [multi line string from a text file or a sentence ]

    Returns:
        [string]: [the most repeated word in a sentence]
    """
    
    word_count = defaultdict(lambda: 0)
 
    for i in sentence.split():
        i = i.lower()
        word_count[i] += 1
 
        if word_count[i] > 1:
            return i
 
    return 'No word is being repeated'
 




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
    print(first_repeating_word(string))
    print("\n\n\n")
    print(first_repeating_word(mult_str))
    print("\n\n\n")
    print(first_repeating_word(last_str))








### The word 'the' is repeated 14 times  
### The word 'of' is repeated 12 times 
### The word 'it' is repeated only 10 times 
###### who is it possible that it should out but only 


