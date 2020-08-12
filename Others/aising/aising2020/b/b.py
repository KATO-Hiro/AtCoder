# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    count = 0

    for index, ai in enumerate(a, 1):
        if index % 2 == 1 and ai % 2 == 1:
            count += 1

    print(count)


if __name__ == '__main__':
    main()
