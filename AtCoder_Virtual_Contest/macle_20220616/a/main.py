# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = sorted(input().rstrip())

    if ''.join(s) == "abc":
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
