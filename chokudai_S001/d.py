# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    print(' '.join(map(str, a)))


if __name__ == '__main__':
    main()
