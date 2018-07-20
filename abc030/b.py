# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


def main():
    n, m = list(map(int, input().split()))
    short = (n % 12) * 30 + m / 2
    long = 6 * m
    diff = abs(short - long)
    print(min(diff, 360 - diff))


if __name__ == '__main__':
    main()
