#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    A function that adds all unique
    integers in a list (only once for each intger)
    """
    unique_numbers = set(my_list)
    return sum(unique_numbers)
