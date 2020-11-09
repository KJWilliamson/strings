#!/usr/bin/env python3
"""
Kenzie assignment: Strings!
"""
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Instructions:
# Complete each function below by writing the code for it. main() is already
# set up to test all the functions with a few different inputs, printing 'OK'
# for each function once it returns the correct result.
# The starter code for each function includes a bare 'return' which is just a
# placeholder for your code.

# Your name, plus anyone who helped you with this assignment.
# Give credit where credit is due.
__author__ = "Kamela Williamson"
# https://docs.python.org/3/tutorial/
# https://www.w3schools.com/python/
# https://www.youtube.com/watch?v=k9TUPpGqYTo&feature=emb_logo
# https://pythonprinciples.com/lessons/

# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# Example:
#   donuts(5) returns 'Number of donuts: 5'
#   donuts(23) returns 'Number of donuts: many'


def donuts(count):
    # your code here
    if count < 10:
        return 'Number of donuts: ' + str(count)
    else:
        return 'Number of donuts: many'


# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 characters of the original string.
# However, if the string length is less than 2, return
# an empty string instead.
# Example:
#   'spring' -> 'spng'


def both_ends(s):
    # your code here
    if len(s) > 2:
        return s[:2] + s[-2:]
    else:
        return ""


# C. fix_start
# Given a string s, return a string where all occurrences
# of its first character have been changed to '*', except
# do not change the first character itself.
# Example:
#   'babble' -> 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.


def fix_start(s):
    # your code here
    # first character itself
    first = s[0]
    # everything after 1st character
    everything_else = s[1:]
    everything_else_changed = everything_else.replace(first, '*')
    return first + everything_else_changed


# D. mix_up
# Given strings a and b, return a single string with a and
# b separated by a space '<a> <b>', except swap the first
# 2 characters of each string.
# Example:
#   'mix', 'pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.


def mix_up(a, b):
    # your code here
    return b[:2] + a[2:] + " " + a[:2] + b[2:]


# E. verbing
# Given a string, if its length is at least 3, add 'ing' to its
# end unless it already ends in 'ing', in which case add 'ly'
# instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.


def verbing(s):
    # your code here
    if len(s) < 3:
        return s
    # -3 last 3 characters
    elif s[-3:] == 'ing':
        return s + 'ly'
    else:
        return s + 'ing'


# F. not_bad
# Given a string, find the first occurrence of the substrings
# 'not' and 'bad'. If the 'bad' follows the 'not', replace
# the whole 'not'...'bad' substring with 'good'.
# Return the resulting string.
# Example:
#   'This dinner is not that bad!' -> 'This dinner is good!'
# this took me forever. my brain hurts


def not_bad(s):
    # your code here
    s_not = s.find('not')
    s_bad = s.find('bad')

    if s_not != -1 and s_bad != -1 and s_bad > s_not:
        s = s[:s_not] + 'good' + s[s_bad+3:]
    return s


# G. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same
# length. If the length is odd, we'll say that the extra
# character goes in the front half.
#   e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form:
#   a-front + b-front + a-back + b-back
# did this take anyone else hours to get


def front_back(a, b):
    # your code here
    a_part = len(a) // 2
    b_part = len(b) // 2

    if len(a) % 2 == 1:
        a_part = a_part + 1
    if len(b) % 2 == 1:
        b_part = b_part + 1

    return a[:a_part] + b[:b_part] + a[a_part:] + b[b_part:]
