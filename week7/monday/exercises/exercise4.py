def isSorted (aList):
    return all (aList [i+1] > aList [i] for i in range (len (aList) - 1))

print (isSorted ([1, 2, 3, 4]))
print (isSorted ([1, 2, 5, 4]))

# lambda niet nodig
