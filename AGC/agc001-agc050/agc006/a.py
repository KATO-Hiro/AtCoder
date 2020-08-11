'''input
3
abc
cde
5

1
a
z
2

4
expr
expr
4

'''

# -*- coding: utf-8 -*-

# AtCoder Grand Contest
# Problem A


if __name__ == '__main__':
    n = int(input())
    s = input()
    t = input()

    # See:
    # https://www.youtube.com/watch?v=VX8cGy7kNTE
    for l in range(n, 2 * n + 1):
        s_end = s[-(2 * n - l):]
        t_start = t[:2 * n - l]

        if s_end == t_start:
            print(len(s) + len(t) - len(s_end))
            exit()

    print(len(s) + len(t))
