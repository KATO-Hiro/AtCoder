# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().split())
    p = sorted(list(map(int, input().split())))

    print(sum(p[:k]))


if __name__ == '__main__':
    main()
