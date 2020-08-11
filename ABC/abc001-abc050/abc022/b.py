# -*- coding: utf-8 -*-


def main():
    n = int(input())

    # See:
    # https://www.slideshare.net/chokudai/abc022
    print(n - len(set([int(input()) for _ in range(n)])))


if __name__ == '__main__':
    main()
