print ("""
Instructions: 
    Follow the structure below for solving equations.
    num operation num
    Eg.   1 + 1 - 1 ** 1 ....
        100 * 100 / 50 ....
    """)

def user_input():
    """ 
    Grabbing user input for problem solving and storing it in a list
    """
    equationList = []
    givenEquation = input("Solve: ")
    equationList += givenEquation.split()
    return equationList


def compiler(givenInput):    
    """ 
    Looping through the list to separate numbers and operators 
    """
    numberSet = []
    operatorSet = []
    for num in range(1, len(givenInput), 2):
        operatorSet.append(givenInput[num])
    for num in range(0, len(givenInput) + 1, 2):
        numberSet.append(float(givenInput[num]))       
    return numberSet, operatorSet


def calculate(numberSet, operatorSet):
    """
    Calculating problem by running through numberSet, and executed by the given operator in the operatorSet
    """
    currentAnswer = numberSet.pop(0)
    count = 0
    for num in numberSet:
        if operatorSet[count] == "+":
            currentAnswer += num
            count += 1
        elif operatorSet[count] == "-":
            currentAnswer -= num
            count += 1
        elif operatorSet[count] == "*":
            currentAnswer *= num
            count += 1
        elif operatorSet[count] == "/":
            currentAnswer /= num
            count += 1
        elif operatorSet[count] == "%":
            currentAnswer %= num
            count += 1
        else:
            currentAnswer **= num
            count += 1
    
    print(f"= {currentAnswer}")

    
givenInput = user_input()
a, b = compiler(givenInput)
calculate(a, b)









