# -*- coding: utf-8 -*-


def main():
    n, k = map(int, input().split())

    if n % k == 0:
        print(0)
    else:
        print(n - k)


if __name__ == '__main__':
    main()
