# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().split())
    total = 0
    count = 0

    for i in range(n):
        ai = int(input())
        total += ai
        count += 1

        if total >= k:
            print(count)
            exit()


if __name__ == '__main__':
    main()
