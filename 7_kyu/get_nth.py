"""
Linked Lists - Get Nth

Implement a GetNth() function that takes a linked list and an integer index and returns the node stored at the Nth index position.
GetNth() uses the C numbering convention that the first node is index 0, the second is index 1, ... and so on. So for the 
list 42 -> 13 -> 666, GetNth() with index 1 should return Node(13);

getNth(1 -> 2 -> 3 -> null, 0).data === 1
getNth(1 -> 2 -> 3 -> null, 1).data === 2
The index should be in the range [0..length-1]. If it is not, GetNth() should throw/raise an exception. You should also raise
an exception if the list is empty/null/None.
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def get_nth(node, index):
    tmp = node
    count = 0
    i = 0
    if(node == None or index < 0):
        raise Exception('None linked list')
    while(tmp.next != None):
        tmp = tmp.next
        count = count + 1
    if(index > count):
        raise Exception('Index out of bound')
    tmp = node
    while(i < index):
        tmp = tmp.next
        i = i + 1
    return tmp
