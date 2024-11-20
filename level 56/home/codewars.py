#1Build a function that returns an array of integers from n to 1 where n>0.

# Example : n=5 --> [5,4,3,2,1]

def reverse_seq(n):
    res = []
    for i in range(n):
        res.append(n)
        n -= 1
    return res
#=============================

# The starship Enterprise has run into some problem when creating a program to greet everyone as they come aboard. It is your job to fix the code and get the program working again!

# Example output:

# Hello, Mr. Spock

def say_hello(name):
    return "Hello, "+name
#=============================

# I'm new to coding and now I want to get the sum of two arrays... Actually the sum of all their elements. I'll appreciate for your help.

# P.S. Each array includes only integer numbers. Output is a number too.
def array_plus_array(arr1,arr2):
    return sum(arr1 + arr2)
#===================================

# You take your son to the forest to see the monkeys. You know that there are a certain number there (n), but your son is too young to just appreciate the full number, he has to start counting them from 1.

# As a good parent, you will sit and count with him. Given the number (n), populate an array with all numbers up to and including that number, but excluding zero.

# For example(Input --> Output):

# 10 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#  1 --> [1]

def monkey_count(n):
    return list(range(1,n + 1))
#=================================

# Complete the solution so that it reverses all of the words within the string passed in.

# Words are separated by exactly one space and there are no leading or trailing spaces.

# Example(Input --> Output):

# "The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"


def reverse_words(s):
     return " ".join(s.split(" ")[::-1])