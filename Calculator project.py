print ("""
Instructions: 
    Follow the structure below for solving equations.
    num operation num
    Eg.   1 + 1
        100 + 100
    """)

def user_input():
    equationList = []
    givenEquation = input("Solve: ")
    equationList += givenEquation.split()
    return equationList


def calculate():
    """  Converting given strings in the list into floats  """
    """  Separating operation for calculating  """

    numberSet = user_input()
    operation = numberSet[1]
    firstSet = float(numberSet[0])
    secondSet = float(numberSet[2])
    answer = 0

    if operation == "+":
        answer += firstSet + secondSet
    elif operation == "-":
        answer += firstSet - secondSet
    elif operation == "*":
        answer += firstSet * secondSet
    elif operation == "/":
        answer += firstSet / secondSet
    elif operation == "**":
        answer += firstSet ** secondSet
    else:
        print ("Invalid operation! Please try again.")

    answer_message = f"\n= {answer}\n"
    print (answer_message)
    calculate()


calculate()