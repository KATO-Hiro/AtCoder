# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    odd_patterns = 1

    for ai in a:
        if ai % 2 == 0:
            odd_patterns *= 2

    print(3 ** n - odd_patterns)


if __name__ == '__main__':
    main()
