# Q4 ---------------------------------------
def selectionSort(L):
    n = len(L)
    if n<1:
        return(L)
    for i in range(n):
        mpos = i
        for j in range(i+1, n):
            if L[j] < L[mpos]:
                mpos = j
                print("1---", L, i)
        (L[i], L[mpos]) = (L[mpos], L[i])
        print("2---", L, i)
    return(L)

# selectionSort([9, 4, 5, 2, 3, 7, 6, 8, 1]) # 5

# Q5 ---------------------------------------
def insertionSort(L):
    n = len(L)
    if n<1:
        return(L)
    for i in range(n):
        j = i
        while(j > 0 and L[j] < L[j-1]):
            (L[j], L[j-1]) = (L[j-1], L[j])
            j = j-1
        print("1---", L, i, j)
    return(L)

#insertionSort([9, 4, 5, 2, 3, 7, 6, 8, 1])
# The sort is stable and it sorts in-place
# After m iterations of the for-loop, the first m elements in the list are in sorted order

def updateDict(d):
       d["rollno"] = 12
Dict = {"name" : "John", "Age" : 21}
updateDict(Dict)
print(Dict)