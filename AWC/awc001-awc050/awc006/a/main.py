# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, l, w = map(int, input().split())
    d = list(map(int, input().split()))
    left, right = l - w, l + w
    ans = 0

    for di in d:
        if left <= di <= right:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
