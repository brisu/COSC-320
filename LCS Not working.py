from array import *

#first formulate the table of content
def LCSTable(x, y):
    # get length of the strings to start populating the LCS table
    m = len(x)
    n = len(y)
    # produce 2D array
        #table = [[0]*cols]*rows
    # Alt method for table population
    table = [[0]*(m+1)]*(n+1)
    #table = [[None]*(m+1) for i in range(n+1)]

    # set first element of 2d array as 0
    table[0][0] = 0

    # attempt to set first row of table[1][m] to zero as it represents empty subsequence of y
    for i in range(1,m):
       table[0][i] = 0

    # attempt to set first column of table[1][m] to zero as it represents empty subsequence of x
    for i in range(1 , n):
        table[i][0] = 0

    for i in table:
        print(table)
    # table population error, it is populating but not making
    # the first row full of zeroes

    # this method currently doesn't work
    for i in range(1 , n):
        for j in range(1 , m):
            if x[j] == y[i]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    # return method returns an error that it is outside function


    for i in table:
        print(table)

    return table[n][m]

def printLCS(table, x, y):
    S = ""
    i = len(x)
    j = len(y)
    while i != 0 and j != 0:
        if table[i-1][j-1] == (table[i][j] - 1) and x[j]==j[i]:
            S.push(x[j])
            i = i - 1
            j = j -1
        elif table[i-1][j] == table [i][j]:
            i = i - 1
        else:
            j = j - 1
    while S:
        print(S.pop)

test = "hellothisisatestfortheLCSSalgorithm"
x = "accdcdbdbd"
y = "bdbd"
pattern = "hellothisatestfortheKMPalgrothmi"

printLCS(LCSTable(x,y), x, y)
