# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, d = map(int, input().split())
    s = input().rstrip()
    count = s.count("@")
    print(n - (count - d))


if __name__ == "__main__":
    main()
