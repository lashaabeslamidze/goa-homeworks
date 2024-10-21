#1 You get an array of numbers, return the sum of all of the positives ones.

# Example [1,-4,7,12] => 1 + 7 + 12 = 20

# Note: if there is nothing to sum, the sum is default to 0.


def positive_sum(arr):
    sum = 0
    for e in arr:
        if e > 0:
            sum = sum + e
    return sum



#======================================


#2 Complete the square sum function so that it squares each number passed into it and then sums the results together.
# For example, for [1, 2, 2] it should return 9 because 

# 1² + 2² + 2² = 9

def square_sum(numbers):
    return sum(x * x for x in numbers) 

#===============================


#3 Complete the solution so that it reverses the string passed into it.

def solution(string):
    return string[::-1]

#================================


#4 Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.


def bool_to_word(boolean):
    return "Yes" if boolean else "No"

#==========================================




#5 Given an array of integers your solution should find the smallest integer.

# For example:

# Given [34, 15, 88, 2] your solution will return 2
# Given [34, -345, -1, 100] your solution will return -345
# You can assume, for the purpose of this kata, that the supplied array will not be empty.

def find_smallest_int(arr):
    return min(arr)
#=================================



















