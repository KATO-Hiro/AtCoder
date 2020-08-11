# -*- coding: utf-8 -*-


def main():
    n = int(input())
    p = sorted([int(input()) for _ in range(n)])

    # See:
    # https://img.atcoder.jp/abc115/editorial.pdf
    print(sum(p) - max(p) // 2)


if __name__ == '__main__':
    main()
