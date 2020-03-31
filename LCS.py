#Naive method
def LCSTable(x, y,m,n):

    # base case
    if m == 0: return True
    if n == 0: return False


    it = iter(x)
    for y in it:
        print(x)
        break

    # return all(c in it for c in y)

    """
    # i is start of index of the array x
    i = 0
    # i is start of index of the array y
    j = 0

    while i < m and j < n:
        if x[j] == y[j]:
            j = j + 1
        i = i + 1

    return j == m
    print(m)
    """

#    it = iter(y)
#    return all(c in it for c in x)

    text = "thisisatestwithinatestaha"
    pattern = "test"
    m = len(text)
    n = len(pattern)
    LCSTable(text,patter,m,n)
