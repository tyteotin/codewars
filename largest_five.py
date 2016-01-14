"""
In the following 6 digit number:
283910
91 is the greatest sequence of 2 digits.

Complete the solution so that it returns the largest five digit number found within the number given.. The number will be passed in
as a string of only digits. It should return a five digit integer. The number passed may be as large as 1000 digits.
"""

import re
def solution(digits):
    max_num = 0
    for i in digits:
        if(max_num < int(i)):
            max_num = int(i)

    # Lookahead assertion ?= matches pattern but doesn't consume string.
    # Useful for overlapping patterns
    match = re.findall(r"(?=(9[0-9]{4}))", digits)
    res = max([int(i) for i in match])
    return res
