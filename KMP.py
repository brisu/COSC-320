tocheck = "palgiarizing abacac palgiarizing plagiarized document ohh nono."
pattern = "plagiarizing plagiarized document"
IPS = []

def makeIPS(): 
    #initializing the IPS 
    for i in range(len(pattern)+1):
        IPS.append(0)
    prefix = [pattern[0]]
    # print("show before:" , prefix)
    num = 1
    increment = 0    
    for i in range( 1, len(pattern) ):
        #print(pattern[i])
        #print(prefix[(0 + increment)])
        if ( pattern[i] == prefix[(0 + increment)] ):
            IPS[(i+1)] = num
            num = num + 1
            increment = increment + 1
            prefix.append(pattern[increment])
        else:
            # print("before clear:", prefix)
            prefix.clear()
            prefix.append(pattern[0])
            # print( "after clear :", prefix)
            num = 1
            increment = 0    
        
makeIPS()
print("The text to be check: " , tocheck)
print("The pattern: " , pattern)
print("The Pi Cahrt/ IPS: " , IPS)

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
print("Start the Same From Location: ",start," | End at the Location: ", end)
print(tocheck[start:(end+1)])          



    
    

