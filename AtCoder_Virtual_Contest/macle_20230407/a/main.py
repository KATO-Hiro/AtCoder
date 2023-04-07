# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    abc = sorted(list(map(int, input().split())))
    k = int(input())
    d = abc[-1] * 2 ** k
    print(sum(abc[:2]) + d)


if __name__ == "__main__":
    main()
