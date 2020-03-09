# -*- coding: utf-8 -*-


def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))

    if sum(a) >= h:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
