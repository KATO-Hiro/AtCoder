# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    x, k, d = map(int, input().split())
    kd = k * d

    if 0 < kd <= abs(x):
        print(abs(x - kd))
    elif x == 0:
        if k % 2 == 0:
            print(0)
        else:
            print(d)
    elif x == d:
        if k % 2 == 0:
            print(d)
        else:
            print(0)
    else:
        m = abs(x) // d
        print(min(abs(abs(x) - m * d), abs(abs(x) - (m + 1) * d)))


if __name__ == '__main__':
    main()
