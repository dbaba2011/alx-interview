#!/usr/bin/python3
'''
calculates the minimum number of operations required
to create a specific number of characters.
Assumes that there are only two operations available:
copying all characters and pasting them
'''


def minOperations(n):
    k = 0
    m = 2

    while n > 1:
        while n % m == 0:
            k += m
            n /= m
        m += 1
    return k
