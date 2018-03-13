'''input
fajsonlslfepbjtsaayxbymeskptcumtwrmkkinjxnnucagfrg
d
atcoderregularcontest
b
abcdefghijklmnopqrstuvwxyz
None
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    S = sorted(set(list(input())))
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                 'y', 'z']

    if len(S) == 26:
        print('None')
    else:
        for alphabet in alphabets:
            if alphabet not in S:
                print(alphabet)
                break
