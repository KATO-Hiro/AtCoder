# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    k = int(input())
    # See:
    # https://atcoder.jp/contests/abc234/submissions/28379688
    result = bin(k)[2:]
    print(result.replace('1', '2'))


if __name__ == "__main__":
    main()
