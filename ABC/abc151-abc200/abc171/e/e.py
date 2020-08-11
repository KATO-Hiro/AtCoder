# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    xor = 0

    for ai in a:
        xor ^= ai

    tmp = xor
    ans = list()

    for ai in a:
        xor ^= ai
        ans.append(xor)
        xor = tmp

    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()
