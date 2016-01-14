"""
You are given an array (which will have a length of at least 3, but could be very large) containing 
integers. The integers in the array are either entirely odd or entirely even except for a single integer
 N. Write a method that takes the array as an argument and returns N.

For example:

[2, 4, 0, 100, 4, 11, 2602, 36]

Should return: 11

[160, 3, 1719, 19, 11, 13, -21]

Should return: 160
"""

def find_outlier(integers):
    odd = 0
    even = 0
    even_num = 0
    odd_num = 0
    for i in integers:
        if(i%2 == 0):
            even = even + 1
            even_num = i
        if(i%2 != 0):
            odd = odd + 1
            odd_num = i
    if(even > odd):
        return odd_num
    else:
        return even_num