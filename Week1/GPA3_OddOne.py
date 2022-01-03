def odd_one(L):
    typeDict = {'int':0, 'float':0, 'str':0, 'bool':0}
    for i in range(len(L)):
        typeDict[str(type(L[i]))[8:-2]] = typeDict[str(type(L[i]))[8:-2]] + 1

    if(typeDict['int'] == 1):
        return 'int'
    elif(typeDict['float'] == 1):
        return 'float'
    elif(typeDict['str'] == 1):
        return 'str'
    elif(typeDict['bool'] == 1):
        return 'bool'

print(odd_one([1,2,3.4,5,10]))