# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 1

    for ai in a:
        ans *= ai

        if len(str(ans)) > k:
            ans = 1

    print(ans)


if __name__ == "__main__":
    main()
