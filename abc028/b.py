# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


def main():
    s = input()
    values = [0] * 6

    for si in s:
        if si == 'A':
            values[0] += 1
        elif si == 'B':
            values[1] += 1
        elif si == 'C':
            values[2] += 1
        elif si == 'D':
            values[3] += 1
        elif si == 'E':
            values[4] += 1
        elif si == 'F':
            values[5] += 1

    print(' '.join(map(str, values)))


if __name__ == '__main__':
    main()
