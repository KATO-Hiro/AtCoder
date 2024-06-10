# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    lower_count = 0

    for si in s:
        if si.islower():
            lower_count += 1

    upper_count = n - lower_count

    if lower_count > upper_count:
        print(s.lower())
    else:
        print(s.upper())


if __name__ == "__main__":
    main()
