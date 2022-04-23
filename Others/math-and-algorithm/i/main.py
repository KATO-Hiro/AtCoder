# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    bits = 1

    for ai in a:
        bits |= bits << ai
    
    if bits >> s & 1:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
