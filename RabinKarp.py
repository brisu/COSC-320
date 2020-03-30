text = "This is the text to check"
pattern = "check"

def hashFunction(string, x):
    prime = 11
    hash = 0

    # dunno how to write it but for everything in string
    # from 1 to the index x do the following hash fucntion
    text = string[1:x]
    for i in text:
        hash += i**(i-1)
    return hash
    #end for

    print("Hash value is: " + hash)
#return hash somehow idk python

hashFunction("Hello world", 11)



def hashReCalc(string, current, prime, hash):
    hash = hash - string[current] # does this return the letter of string at index current?
    hash = hash/prime
    m = len(string)
    new = current + m - 1
    hash = hash + string(new)**(m-1)
    return hash



def stringMatch(text, pattern, m):
    length = len(pattern) + m - 1
    newT = text[m:length]
    for i in newT:
        if text[i] != pattern[i]:
            return false
        #end if
    # end for
    return true

#start of hash
def RBK(text, pattern, q):
    n = len(text)
    m = len(pattern)
    result = []
    hashT = hashFunction(text, m)
    hashP = hashFunction(pattern, m)

        for i in range(n-m+1):
            if hashT == hashP and stringMatch(tocheck,pattern,i):
                return i
            #end if
            #dunno what the sudo code meant by the field string
            hashP = hashReCalc(String, i+1, q, hashP)
        #end for
    return -1
    # end function

    # result = false
