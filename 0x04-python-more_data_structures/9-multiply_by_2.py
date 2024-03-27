#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    A function that returns a new dictionary
    with all values multiplies by 2
    """
    return {key: value * 2 for key, value in a_dictionary.items()}
