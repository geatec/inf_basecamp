aList = []

for i in range (1, 10, 2):
    aList.append ((i, i + 1))

print (aList)

bList = filter (lambda item: item [0] % 3 == 0, aList)
print (list (bList))

# % 3 i.s.o. % 2 to not remove everything
