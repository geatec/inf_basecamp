import copy as cp

aList = [[1, 2], [3, 4], [5, 6]]
bList = cp.deepcopy (aList)

bList [1] = [7, 8]
bList [2][0] = 9

print (aList)
print (bList)
