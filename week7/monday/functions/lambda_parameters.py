def compute (aFunction):
    firstNumber = float (input ('Eerste getal: '))
    secondNumber = float (input ('Tweede getal: '))
    result = aFunction (firstNumber, secondNumber)
    print (result)


compute (lambda firstNumber, secondNumber: firstNumber + secondNumber)
compute (lambda firstNumber, secondNumber: firstNumber - secondNumber)
compute (lambda firstNumber, secondNumber: firstNumber * secondNumber)
compute (lambda firstNumber, secondNumber: firstNumber / secondNumber)
