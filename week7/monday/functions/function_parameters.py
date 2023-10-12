def compute (aFunction):
    firstNumber = float (input ('Eerste getal: '))
    secondNumber = float (input ('Tweede getal: '))
    result = aFunction (firstNumber, secondNumber)
    print (result)

def sum (firstNumber, secondNumber):
    print ('Som')
    return firstNumber + secondNumber

def difference (firstNumber, secondNumber):
    print ('Verschil')
    return firstNumber - secondNumber

def product (firstNumber, secondNumber):
    print ('Product')
    return firstNumber * secondNumber

def quotient (firstNumber, secondNumber):
    print ('Quotient')
    return firstNumber / secondNumber

compute (sum)
compute (difference)
compute (product)
compute (quotient)
