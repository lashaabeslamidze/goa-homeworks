# Given an array of numbers, return a new array of length number containing the last even numbers from the original array (in the same order). The original array will be not empty and will contain at least "number" even numbers.

def even_numbers(arr,n):
    return[i for i in arr if i % 2 == 0][-n:]
#===============================

# A sequence or a series, in mathematics, is a string of objects, like numbers, that follow a particular pattern. The individual elements in a sequence are called terms. A simple example is 3, 6, 9, 12, 15, 18, 21, ..., where the pattern is: "add 3 to the previous term".

# In this kata, we will be using a more complicated sequence: 0, 1, 3, 6, 10, 15, 21, 28, ... This sequence is generated with the pattern: "the nth term is the sum of numbers from 0 to n, inclusive".


def sum_of_n(n):
    negative = False
    if n < 0:
        negative = True
        n = abs(n)
    listn = []
    x = 0
    while len(listn) < n+1:
        sum = 0
        for i in range(0,x+1):
            sum += i
        if negative == True:
            listn.append(sum*-1)
        else:
            listn.append(sum)
        x += 1
    return listn


