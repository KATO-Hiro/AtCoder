'''input
vwxyz
25
zz

abcde
8
bc

aeiou
22
ue

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    from itertools import product

    s = input()
    n = int(input())

    alphabets = list(product(list(s), repeat=2))[n - 1]
    print(alphabets[0] + alphabets[1])
