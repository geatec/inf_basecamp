aList = [1, 2, 3, 4, 7, 8, 9]
evenList = list (filter (lambda x: x%2 == 0, aList))
oddList = list (filter (lambda x: x%2 == 1, aList))
print (aList, evenList, oddList)
