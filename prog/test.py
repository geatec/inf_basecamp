number = 1234
string = str (number)

total = 0
expression =' + '.join ([char for char in string])
for digit in string:
    total += int (digit)

print (expression, '=', total)
