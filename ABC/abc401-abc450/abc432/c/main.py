# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))

    z = y * min(a)
    ans = 0

    for ai in a:
        amount = ai * y - z
        diff = y - x

        if amount % diff != 0:
            ans = -1
            break

        count = amount // diff

        if count > ai:
            ans = -1
            break

        ans += ai - count

    print(ans)


if __name__ == "__main__":
    main()
