# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    for ai in a:
        ans += max(ai)

    print(ans)


if __name__ == "__main__":
    main()
