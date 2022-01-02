import math

def Twin_Primes(n, m):
    listOfTwinPrimes = []
    start = n
    if n < 2:
        start = 2
    for i in range(start, m-1):
        if (Check_Prime(i) and Check_Prime(i+2)):
            listOfTwinPrimes.append((i, i+2))
    return listOfTwinPrimes

def Check_Prime(a):
    for i in range(2, int(math.sqrt(a))+1):
        if a%i == 0:
            return False
    return True
        
print(Twin_Primes(0,19))