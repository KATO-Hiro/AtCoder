# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0

    for ai in a:
        p, _ = divmod(ai, k)
        count += p

    if count >= m:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
