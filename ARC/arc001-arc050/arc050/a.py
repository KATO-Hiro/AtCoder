# -*- coding: utf-8 -*-


def main():
    large_c, c = list(map(str, input().split()))

    if large_c.lower() == c:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
