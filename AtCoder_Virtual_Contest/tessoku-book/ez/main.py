# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = sorted(list(map(int, input().split())), reverse=True)
    print(sum(a[:2]))


if __name__ == "__main__":
    main()
