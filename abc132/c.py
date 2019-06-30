# -*- coding: utf-8 -*-


def main():
    n = int(input())
    d = sorted(list(map(int, input().split())))
    print(d[n // 2] - d[n // 2 - 1])


if __name__ == '__main__':
    main()
