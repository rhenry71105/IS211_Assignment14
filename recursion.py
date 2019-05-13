#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
	Author: Rickardo Henry.
	
	Description: 
				Week 14 Assignment - Recursion
"""


def fibonnaci(n):
    """Returns the nth element in the Fibonnaci sequence.

    Args:
        n (int): Number representing the nth element in a sequence.

    Returns:
        int: The number that is the given nth element in the fibonnaci sequence.

    Examples:
        >>> fibonnaci(1)
        1

        >>> fibonnaci(10)
        55
    """
    if n == 1 or n == 2:
        return 1
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)


def gcd(a, b):
    """Returns the greatest common divisor of two numbers.

    Args:
        a (int): an integer to find the greatest common divisor with b
        b (int): an integer to find the greatest common divosor with a

    Returns:
        int: An integer representing the largest number that divides both given
        integers a and b without leaving a remainder.

    Examples:
        >>> gcd(252, 105)
        21

        >>> gcd(100, 27)
        1
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def compareTo(s1, s2):
    """Compares two strings and returns a value depending on the comparison of
    the two strings.

    Args:
        s1(str): a string to be compared to another given string in the second
        argument.
        s2(str): a string to be compared to the first given argument (s1).

    Returns:
        int: A value corresponding with the comparison of two strings; A
        positive value if s1 > s2, a negative value if s1 < s2, and 0 if they
        are the same.

    Examples:
        >>> compareTo("abracadabra", "poof")
        -112
        >>> compareTo("lmno", "hijkl")
        108
        >>> compareTo("", "")
        0
        >>> compareTo("boo", "book")
        -111
    """
    if s1 == '' and s2 == '':
        return 0
    elif ord(s1[0]) > ord(s2[0]):
        return 0 + ord(s1[0])
    elif ord(s1[0]) < ord(s2[0]):
        return 0 - ord(s2[0])
    elif s1[1:2] == '' and not s2[1:2] == '':
        return 0 - ord(s2[0])
    elif s2[1:2] == '' and not s1[1:2] == '':
        return 0 + ord(s1[0])
    elif s1[1:2] == '' and s2[1:2] == '':
        return 0
    else:
        return compareTo(s1[1:], s2[1:])
