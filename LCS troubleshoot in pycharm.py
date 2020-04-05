from array import *

#first formulate the table of content
def LCSTable(x, y):

    # get length of the strings to start populating the LCS table
    m = len(x)
    n = len(y)
    # produce 2D array
        #table = [[0]*cols]*rows
    table = [[0]*m]*n
    # set first element of 2d array as 0
    table[0][0] = 0
    for i in table:
        print(table)
    # attempt to set first row of table[1][m] to zero as it represents empty subsequence of y
    for i in range(1,m):
       table[0][i] = 0
    # attempt to set first column of table[1][m] to zero as it represents empty subsequence of x
    for i in range(1 , n):
        table[i][0] = 0
    # table population error, it is populating but not making
    # the first row full of zeroes
    for i in table:
        print(table)
    # this method currently doesn't work
    for i in range(1 , n):
        for j in range(1 , m):
            if y[i] == x[i]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j], table[i][j])
    for i in table:
        print(table)
    print("This is m and n")
    print(m)
    print(n)
    for i in range(1,m):
        print(table[0][i])
    print("Seperate m above and n below")
    for i in range(1,n):
        print(table[i][0])
    # return method returns an error that it is outside function
    return table[m][n]

def printLCS(length, x, y):
    table = length
    S = stack()
    i = len(x)
    j = len(y)
    while i != 0 and j != 0:
        if table[i-1][j-1] == table[i][j] - 1 and x[j]==j[i]:
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
LCSTable(x,y)

printLCS(LCSTable(x,y), x, y)
