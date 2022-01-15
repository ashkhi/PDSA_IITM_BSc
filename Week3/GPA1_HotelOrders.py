def DishPrepareOrder(nums):
    orderDictDishToCount = {}
    for i in range(len(nums)):
        if(nums[i] in orderDictDishToCount):
            orderDictDishToCount[nums[i]] = orderDictDishToCount[nums[i]] + 1
        else:
            orderDictDishToCount[nums[i]] = 1
    
    orderDictCountToDish = {}
    for key, value in orderDictDishToCount.items():
        if(value in orderDictCountToDish):
            orderDictCountToDish[value].append(key)
        else:
            orderDictCountToDish[value] = [key]

    reverseSortedCounts = sorted(orderDictCountToDish, reverse=True)
    finalOrderList = []
    for count in reverseSortedCounts:
        keySortedOrders = sorted(orderDictCountToDish[count])
        finalOrderList += keySortedOrders

    return finalOrderList

print(DishPrepareOrder([1006, 1008, 1009, 1008, 1007, 1005, 1008, 1001, 1003, 1009, 1006, 1003, 1004, 1002, 1008, 1005, 1004, 1007, 1006, 1002, 1002, 1001, 1004, 1001, 1003, 1007, 1007, 1005, 1004, 1002]))
