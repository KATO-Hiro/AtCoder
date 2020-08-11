# -*- coding: utf-8 -*-


def main():
    low, high = list(map(int, input().split()))
    n = int(input())
    a = [int(input()) for _ in range(n)]

    for ai in a:
        if ai > high:
            print(-1)
        else:
            print(max(0, low - ai))


if __name__ == '__main__':
    main()
