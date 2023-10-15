import copy as cp

aDict = {1: {10: 100}, 2: {20: 200}, 3: {30: 300}}
bDict = aDict
cDict = aDict.copy ()
dDict = cp.copy (aDict)
eDict = cp.deepcopy (aDict)

aDict [2] = {2000: 20000}
aDict [3][30] = {30000}

print ('original', aDict)
print ('nocopy  ', bDict)
print ('.copy   ', cDict)
print ('copy    ', dDict)
print ('deepcopy', eDict)
