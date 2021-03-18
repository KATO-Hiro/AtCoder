# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = list(input().rstrip())
    t = reversed(s)
    n = len(s)
    diff = 0

    for si, ti in zip(s, t):
        if si != ti:
            diff += 1

    if diff == 0:
        n -= n % 2
        ans = n * 25
    elif 1 <= diff <= 3:
        ans = n * 25 - 2
    else:
        ans = n * 25

    print(ans)


if __name__ == "__main__":
    main()
