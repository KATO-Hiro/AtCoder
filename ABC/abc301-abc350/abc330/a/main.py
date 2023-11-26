# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, l = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0

    for ai in a:
        if ai >= l:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
