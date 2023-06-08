# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, b = map(int, input().split())
    a = list(map(int, input().split()))
    c = sum(list(map(int, input().split())))
    ans = n * m * b

    for ai in a:
        ans += m * ai + c

    print(ans)


if __name__ == "__main__":
    main()
