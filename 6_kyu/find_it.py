"""
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""

def find_it(seq):
    dupDict = {x:seq.count(x) for x in seq}
    k, v = dupDict.keys(), dupDict.values()
    ix = [i for i in v if i%2 != 0]
    return (key for key, value in dupDict.items() if value == ix[0]).next()
