from queue import LifoQueue


def multi_bracket_validation(value: str):
    """
    The function should take a string as its only argument,
    and should return a boolean representing whether or not the brackets in the string are balanced.
    There are 3 types of brackets: {} [] ()
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.
    """

    if len(value) % 2 != 0:
        return False
    closing_values = {'(': ')', '{': '}', '[': ']'}
    open_chars = closing_values.keys()
    stack = LifoQueue(len(value))
    for char in value:
        if char in open_chars:
            stack.put(char)
        else:
            if stack.empty():
                return False
            if closing_values[stack.get()] != char:
                return False

    return stack.empty() 
    
