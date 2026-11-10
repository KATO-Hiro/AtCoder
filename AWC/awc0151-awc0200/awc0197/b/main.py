# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = -1

    for i, ai in enumerate(a, 1):
        if ai >= k:
            ans = i

    print(ans)


if __name__ == "__main__":
    main()
