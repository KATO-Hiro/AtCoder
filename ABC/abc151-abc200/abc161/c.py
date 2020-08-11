# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().split())
    mod = n % k

    print(min(mod, abs(mod - k)))


if __name__ == '__main__':
    main()
