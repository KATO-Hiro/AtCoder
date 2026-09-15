# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    t = list(map(int, input().split()))
    ans = n - len(set(t))
    print(ans)


if __name__ == "__main__":
    main()
