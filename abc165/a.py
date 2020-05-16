# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    k = int(input())
    a, b = map(int, input().split())

    for i in range(a, b + 1):
        if i % k == 0:
            print('OK')
            exit()

    print('NG')


if __name__ == '__main__':
    main()
