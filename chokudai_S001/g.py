# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    print(int(''.join(map(str, a))) % mod)


if __name__ == '__main__':
    main()
