# Given an array of one's and zero's convert the equivalent binary value to an integer.

# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1

def binary_array_to_number(arr):
    totalValue = 0
    positional_value = 0
    for i in reversed(arr):
            totalValue += (2**positional_value) * i
            positional_value += 1
    return totalValue

    