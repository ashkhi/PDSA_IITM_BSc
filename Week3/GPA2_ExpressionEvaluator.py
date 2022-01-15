import string
import operator

def EvaluateExpression(inputStr):
    myStack = []
    myOperators = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv, '**':operator.pow}
    expStr = inputStr.split(' ')

    for ch in expStr:
        if(ch.isnumeric()):
            myStack.append(float(ch))
        elif(ch in myOperators and len(myStack) >= 2):            
            num2 = myStack[-1]
            num1 = myStack[-2]
            myStack = myStack[:-2]
            res = myOperators[ch](num1, num2)
            myStack.append(res)
        else:
            continue
    
    return myStack[0]

print(EvaluateExpression("100 200 + 2 / 5 * 7 +"))