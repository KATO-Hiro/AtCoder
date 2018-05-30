'''input
WBWBWBWBWB
9

BBBWW
1

WWWWWW
0

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    s = input()
    count = 0
    previous = s[0]

    for i in range(1, len(s)):
        current = s[i]

        if previous != current:
            count += 1

        previous = current

    print(count)
