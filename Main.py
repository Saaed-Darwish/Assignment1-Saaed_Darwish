# calculator.py
# Saaed Darwish, ENSF 300 F22
#
# A terminal-based calculator application for determining the result of a mathematical expression containing three values and two operators.
#

# function of addition
def addition(add_value1, add_value2):
    '''
    Addition of two values together

    Parameters:
    add_value1 -- the first value to be added with the second value
    add_value2 -- the second value to be added with the first value

    Returns:
    added_value -- the value of the addition of the two values
    '''
    added_value = add_value1 + add_value2
    return added_value

# function of subtraction
def subtraction(subtract_value1, subtract_value2):
    '''
    Subtraction of two values together

    Parameters:
    subtract_value1 -- the first value to be subtracted by the second value
    subtract_value2 -- the second value to subtract from the first value

    Returns:
    subtracted_value -- the value of the subtraction of the two values
    '''
    subtracted_value = subtract_value1 - subtract_value2
    return subtracted_value

# function of multiplication
def multiplication(multiply_value1, multiply_value2):
    '''
    Multiplication of two values together

    Parameters:
    multiply_value1 -- the first value to be multiplied with the second value
    multiply_value2 -- the second value to be multipled with the first value

    Returns:
    multiplied_value -- the value of the multiplication of the two values
    '''
    multiplied_value = multiply_value1 + multiply_value2
    return multiplied_value

# function of division
def division(divided_value1, divide_value2):
    '''
    Division of two values

    Parameters:
    divided_value1 -- the first value to be divided by the second value
    divide_value2 -- the second value dividing the first value

    Returns:
    division_value -- the value of the division of the two values
    '''
    division_value = divided_value1 / divide_value2
    return division_value

# user prompts
print('Calculator - solves expressions with three integer values and two operators')
print('Valid integer values are an element of the natural numbers')
print('Valid operators include: + (add), - (subtract), * (multiply), / (divide)')

while True:                                                         # continually do this (checking for valid inputs)
    try:                                                               # try command - if an error occurs will not terminate
        print('Enter the first value:', end=' ')                       # prompt user for first value
        first_value = int(input())                                     # read user input for first value
    except ValueError:                                                 # if there is a value error from converting input into integer
        print('Not an integer ex: -2, 0, 1')                           # telling user the input is not valid
    else:                                                              # if there is no error then a valid integer input was made therefore break
        break
    
while True:
    break


# precedence determination

# calculations with functions

# answers & output
