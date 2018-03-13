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

    # See:
    # https://beta.atcoder.jp/contests/abc071/submissions/2194657
    alphabets = [chr(ord('a') + i) for i in range(26)]

    if len(S) == 26:
        print('None')
    else:
        for alphabet in alphabets:
            if alphabet not in S:
                print(alphabet)
                break
