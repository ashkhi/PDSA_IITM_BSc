def find_Min_Difference(L, P):
    sortedList = sorted(L)
    minDiff = sortedList[-1]
    for i in range((len(L)-(P-1))):
        if(minDiff > (sortedList[i+(P-1)] - sortedList[i])):
            minDiff = (sortedList[i+(P-1)] - sortedList[i])
    return minDiff

print(find_Min_Difference([3,4,1,9,56,7,9,12], 5))