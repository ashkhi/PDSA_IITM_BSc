import math

def Goldbach(n):
    listOfPrimePairs = []
    mid = int(n/2)
    for i in range(2, mid+1):
        if(isPrime(i) and isPrime(n-i)):
            listOfPrimePairs.append((i, n-i))
    return listOfPrimePairs

def isPrime(a):
    for i in range(2, int(math.sqrt(a))+1):
        if a%i == 0:
            return False
    return True

print(Goldbach(26))