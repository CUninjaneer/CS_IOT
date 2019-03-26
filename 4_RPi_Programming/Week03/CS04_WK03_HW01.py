################################################################################
# The Raspberry Pi Platform and Python Programming for the Raspberry Pi
# Course 4 in the IoT Specialization
# Module 3
# Assignment 1
# Adam Britt
# March 25, 2019
################################################################################
# Problem Statement:
#
# Write a Python program that prompts the user to input 3 numbers, one at a
# time. The Python program should put the numbers in a list, sort the list, and
# print the sorted list. Executing the program should produce results something
# like this:
#
# Enter a number:
#
# 5
#
# Enter a number:
#
# 4
#
# Enter a number:
#
# 3
#
# 3, 4, 5
#
# Submittal Instructions:
#
# Turn in your source code and a screenshot showing a full execution of your
# program and the result that it prints to the screen. In the execution that
# you take a screenshot of, you should enter the numbers in non-sorted order so
# that we can tell that sorting did occur.
################################################################################
i = 0
lst = []
while i<3:
    n = input('Enter a number:\n\n')
    try:
        lst.append(int(n))
        i = i + 1
    except:
        print('Please enter an integer value. Try again.')
    print('')
lst.sort()
print(lst[0],', ',lst[1],', ',lst[2],'\n')
