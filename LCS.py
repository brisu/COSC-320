from array import *

#first formulate the table of content
# currently working with diff values for each input
def LCSTable(x, y):
    m = len(x)
    n = len(y)
    # produce 2D array
        #table = [[0]*cols]*rows
    # Alt method for table population
    table = [[0]*(m+1)]*(n+1)
    #table = [[None]*(m+1) for i in range(n+1)]

    # table population error, it is populating but not making
    # the first row full of zeroes

    for i in range(n):
        for j in range(m):
            if x[j] == y[i]:
                table[i+1][j+1] = table[i][j] + 1
            else:
                table[i+1][j+1] = max(table[i-1][j], table[i][j-1])
    # return method returns an error that it is outside function
    for i in table:
        print(i)
    return table[n][m]

def printLCS(table, x, y):
    S = ""
    m = len(x) # i
    n = len(y) # j

    # tried to do: while table[m][n] > 0
    # error that int is not subscriptable
    while m != 0 and n != 0:
        # the if statement varies from source to source dunno which to use yet
        if x[m-1] == y[n-1]:
            S += (x[m-1])
            m = m - 1
            n = n -1
        # more error that int is not subscriptable
        elif (table[m-1][n]) >= (table[m][n-1]):
            m = m - 1
        else:
            n = n - 1
    temp = S[::-1]
    print(temp)

t = "hellothisisatestfortheLCSSalgorithm"
x = "accdcdadbdacabdabcabdacabbdbd"
y = "bdbd" #only work with this string
p = "hellothisatestfortheKMPalgrothmi"

printLCS(LCSTable(x, y), x, y)
