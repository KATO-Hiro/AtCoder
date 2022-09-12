# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    ans = set(map(int, input().split()))
    print(len(ans))


if __name__ == "__main__":
    main()
