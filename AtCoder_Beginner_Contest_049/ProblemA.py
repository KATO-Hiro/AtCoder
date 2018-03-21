'''input
z
consonant

a
vowel

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    s = input()
    vowels = ['a', 'e', 'i', 'o', 'u']

    if s in vowels:
        print('vowel')
    else:
        print('consonant')
