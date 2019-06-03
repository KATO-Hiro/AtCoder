# -*- coding: utf-8 -*-


def main():
    n, a, b, c, d = map(int, input().split())
    s = input()

    # See:
    # https://www.youtube.com/watch?v=4GKc4CsoaCE
    if ('##' in s[a - 1:c]) or ('##' in s[b - 1:d]):
        print('No')
        exit()

    if (c > d) and ('...' not in s[b - 2: d + 1]):
        print('No')
        exit()

    print('Yes')


if __name__ == '__main__':
    main()
