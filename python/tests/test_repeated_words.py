from repeated_word.repeated_word import first_repeating_word

def test_short_string():
    string = "Once upon a time, there was a brave princess who..."
    res = first_repeating_word(string)
    assert res == "a"

def test_long_string():
    string = """
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
    res = first_repeating_word(string)
    assert res == "it"

def test_comma_string():
    string = """
    It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, 
    and I didn’t know what I was doing in New York..."""
    res = first_repeating_word(string)
    assert res == "the"

def test_no_repeating_string():
    string = "My phone needs a new cover"
    res = first_repeating_word(string)
    assert res == "No word is being repeated"

def test_Capitalized_string():
    string = "Django X is the same as django but with more features"
    res = first_repeating_word(string)
    assert res == "django"








