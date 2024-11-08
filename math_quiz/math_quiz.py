import random
import warnings

def generateRandomInteger(min: int, max: int) -> int:
    """
    Generate a random integer between min and max.
    
    Parameters:
        min (int): The lower bound of the range (inclusive).
        max (int): The upper bound of the range (inclusive).
        
    Returns:
        int: A random integer between min and max.
        
    Raises:
        ValueError: If min is greater than max.
    
    """
    if min > max:
        raise ValueError("The minimum (min) value is bigger than the maximum (max) value")
    
    if not isinstance(min, int) or not isinstance(max, int):
        min = int(min)
        max = int(max)
        warnings.warn("The value of min and max should ideally be an integer. Proceeding with float conversion.", UserWarning)
        # raise TypeError(f"Both min and max must be integers. Got {type(min).__name__} and {type(max).__name__}.")

    return random.randint(min, max)


def getRandomOperator() -> str:
    """
    Select a random arithmetic operator from a predifined list (e.g. '+', '-', '*')
    Returns:
        str: A randomly operator is choosen.   
    """
    return random.choice(['+', '-', '*'])


def calculateExpression(num1: float, num2: float, operator) -> tuple[str, float]:
    """ Generates a mathematical expression based on the given numbers and operator, 
        and calculates the result by applying an inverted operation ('+' or '-') or multiplication. 
    Parameters: 
        num1 (int): The first number. 
        num2 (int): The second number. 
        operator (str): The operator to use ('+', '-', or '*'). 
    Returns: 
        tuple: A tuple containing the string representation of the expression and the calculated result. 
    """
    expression = f"{num1} {operator} {num2}"

    if operator== '+': 
        calculatedResult = num1 + num2

    elif operator== '-': 
        calculatedResult = num1 - num2

    else: 
        calculatedResult = num1 * num2
    
    return expression, calculatedResult


def runMathQuiz():
    """
    Conduct a math quiz for an specified number of questions.
    Parameters:
        No required.
    Raises:
        ValueError: 
    """
    score = 0
    numQuestions = int(3)

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(numQuestions):
        num1 = generateRandomInteger(1, 10); 
        num2 = generateRandomInteger(1, 5.5); 
        operator= getRandomOperator()

        problem, answer = calculateExpression(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        
        try:
            useranswer = int(input("Your answer: "))
        
        except ValueError:
            print("Valid input. Please enter an integer")
            continue

        if useranswer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{numQuestions}")

if __name__ == "__main__":
    runMathQuiz()
