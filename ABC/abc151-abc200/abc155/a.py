# -*- coding: utf-8 -*-


def main():
    alpha = set(map(int, input().split()))

    if len(alpha) == 2:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
