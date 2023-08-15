#---------------------
# Summer Davis
# COSC 1336
# Project 4
#---------------------
# Objective
# This program will find and display the sum of even integers
# from 1 up to the number a user enters.
#
# The program will ask the user for a positive integer value.
#
# The program will use a loop to validate that the input is
# a positive integer.
#
# The program will use a loop to find and display the sum of
# even integers from 1 up to the input integer.
#---------------------


# This function displays the start of the project
def header ():
    print('\n    User\'s Entry')
    print('    ' + ('-' * 80))

# This function will collect and organize the program tasks
def main():
    
    # Header of the project
    header()

    # Get positive integer & validate input
    integer = getIntegerData('    Enter a positive integer: ') 

    # Calculate sum of even numbers
    evenSum = calculateSum(integer)

    # Display sum of even numbers
    displaySum(integer, evenSum)
    
    # End of project display
    footer()

# This function displays the results from calculateSum()
def displaySum(integer, evenSum):
    print('\n')
    print('    ' + ('-' * 80))
    print('    Summary: Sum of Even Numbers')
    print('    ' + ('-' * 80))
    print('    The sum of even numbers between ' +
          f'1 and {integer} is {evenSum}')
    print('\n')


# This function will calculate the sum of even numbers
# between 1 and the passed parameter
def calculateSum(lastNum):
    counter = 1
    evenSum = 0
    while (counter <= lastNum):
        if counter % 2 == 0:
            evenSum += counter
        counter += 1
    return evenSum

# This function will get user input as an integer and validate
# that it is a positive number
def getIntegerData(prompt): 
    value = int(input(prompt))
    while value < 0:
        print('    Cannot enter a negative number.')
        value = int(input(prompt))
    return value
    
# This function displays the end of the project
def footer():
    print('-' * 80)
    print('End of Project 4')

# Call the main function
main()
