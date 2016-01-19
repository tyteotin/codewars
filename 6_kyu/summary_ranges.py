"""
Write

summary_ranges(nums)
that given a sorted array of numbers, returns the summary of its ranges.
For example:

summary_ranges([1,2,3,4]) == ['1->4']
summary_ranges([0, 1, 2, 5, 6, 9]) == ["0->2", "5->6", "9"]
summary_ranges([0, 1, 2, 3, 3, 3, 4, 5, 6, 7]) == ["0->7"]
summary_ranges([0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10]) == ["0->7","9->10"]
summary_ranges([-2,0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10, 12]) == ["-2", "0->7", "9->10", "12"]
summary_ranges([1,1,1,1,1]) == ['1']
"""

def summary_ranges(nums):
    if(nums == []):
        return []
    if(nums[1:] == nums[:-1]):
        return [str(nums[0])]
    min, max = nums[0], 0
    n = []
    index = 0
    prev = nums[0]
    while(index < len(nums)):
        if(nums[index] == prev or nums[index] == prev+1):
            prev = nums[index]
            max = nums[index]
            index+=1
        else:
            max = nums[index-1]
            n.append([min, max])  
            min = nums[index]
            prev = nums[index]
            max = nums[index]
            index+=1

    n.append([min, max])
    res = []
    for i in n:
        if(i[0] == i[1]):
            res.append(str(i[1]))
        else:
            res.append(str(i[0]) + "->" + str(i[1]))
    return res