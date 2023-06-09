# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    lr = sorted(
        [tuple(map(int, input().split())) for _ in range(n)], key=lambda x: (x[1], x[0])
    )
    prev = 0
    ans = 0

    for li, ri in lr:
        if prev <= li:
            ans += 1
            prev = ri

    print(ans)


if __name__ == "__main__":
    main()
