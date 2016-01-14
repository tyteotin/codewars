"""
Create a function that accepts dimensions, of Rows x Columns, as parameters in order to create a multiplication 
table sized according to the given dimensions. **The return value of the function must be an array, and the numbers
 must be Fixnums, NOT strings.

Example:

multiplication_table(3,3)

1 2 3
2 4 6
3 6 9

-->[[1,2,3],[2,4,6],[3,6,9]]

Each value on the table should be equal to the value of multiplying the number in its first row times the number in
 its first column.
 """
 
def multiplication_table(row,col):
    lst = []
    for i in xrange(0, row, 1):
        lst.append(range(i+1, (i+1)*col+1, i+1))
    return lst