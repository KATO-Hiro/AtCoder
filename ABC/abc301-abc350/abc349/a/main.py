# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = sum(a) * -1
    print(ans)


if __name__ == "__main__":
    main()
