# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0

    for ai in a:
        if ai < 0:
            ai *= -1

        if ai % k != 0:
            continue

        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
