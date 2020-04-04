#first formulate the table of content
def LCSTable(x, y):

    Table = [0][0]

    m = len(x)
    n = len(y)

    for i in range(1,m):
        Table[0][i] = 0
    for i in range(1 , n):
        Table[i][0] = 0
    for i in range(1 , n):
        for j in range(1 , m):
            if y[i] == x[i]:
                Table[i][j] = Table[i-1][j-1] + 1
            else:
                Table[i][j] = max(Table[i-1][j], Table[i][j])
    return Table[n][m]

def printLCS(length, x, y):
    temp = length
    S = stack()
    i = len(x)
    j = len(y)

    while i != 0 and j != 0:
        if Talbe[i-1][j-1] == Table[i][j] - 1 and x[j]==j[i]:
            S.push(x[j])
            i = i - 1
            j = j -1
        elif Table[i-1][j] == Table [i][j]:
            i = i - 1
        else:
            j = j - 1

    while S:
        print(S.pop)

test = "hellothisisatestfortheLCSSalgorithm"
pattern = "hellothisatestfortheKMPalgrothmi"
printLCS(LCSTable(test,pattern), test, pattern)
