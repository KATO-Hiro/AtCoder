# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, m, s = map(int, input().split())
    d = int(input())
    seconds = h * 3600 + m * 60 + s
    seconds += d
    seconds %= 24 * 60 ** 2
    h2 = seconds // 3600
    m2, s2 = divmod(seconds - h2 * 3600, 60)

    print("{:0=2}:{:0=2}:{:0=2}".format(h, m, s))
    print("{:0=2}:{:0=2}:{:0=2}".format(h2, m2, s2))


if __name__ == "__main__":
    main()
