# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = sorted(set([int(input()) for _ in range(n)]), reverse=True)
    print(a[1])


if __name__ == '__main__':
    main()
