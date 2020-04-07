tocheck = "palgiarizing abacac palgiarizing plagiarized document ohh nono."
pattern = "plagiarizing plagiarized document"
IPS = []

def makeIPS():
    #initializing the IPS
    for i in range(len(pattern)+1):
        IPS.append(0)
    prefix = [pattern[0]]

    num = 1
    increment = 0
    for i in range( 1, len(pattern) ):

        if ( pattern[i] == prefix[(0 + increment)] ):
            IPS[(i+1)] = num
            num = num + 1
            increment = increment + 1
            prefix.append(pattern[increment])
        else:

            prefix.clear()
            prefix.append(pattern[0])

            num = 1
            increment = 0



def didYouPlagiarize():
    j = 0
    start = 0
    end = 0
    for i in range(len(tocheck)):
        if tocheck[i] == pattern[(j + 1)]:
            j = j + 1
            if j == len(pattern)-1:
                start = i - len(pattern) +1
                end = i
                j = 0
        else:
            gobackpoint = IPS[j]
            if gobackpoint != 0:
                i = i-1
                j = gobackpoint
    if ( start != 0 and end != 0 ) :
        print("Start the Same From Location:",start," | End at the Location:", end)
        print("On the file:" , tocheck[start:(end+1)])
        f.write("Start the Same From Location: "+ str(start) +" | End at the Location: " + str(end) + '\n' )
        f.write("The sentance is: " + tocheck[start:(end+1)] + '\n')

oneP=[]
f1 = open( "original.txt" , "r" )
f2 = open( "UBetterNotCopyMyWork.txt" , "r" )
f = open("Summary.txt", "a")
tocheck = f2.read()
for x in f1:
    if ( x != "" or x != None or x != '\n'):
        oneP = x.split(".")
        for y in oneP:
            if ( len(y) > 3 ):
                pattern = y
                makeIPS()
                # print("The text to be check: " , tocheck)
                print("The pattern:" , pattern)
                print("Length of the pattern:" ,len(y))
                # print("The Pi Cahrt/ IPS: " , IPS)
                didYouPlagiarize()
    else:
        oneP.clear()
f1.close()
f2.close()
f.close()
