# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    wx = [tuple(map(int, input().split())) for _ in range(n)]
    ans = 0

    for start in range(24):
        candidate = 0

        for wi, xi in wx:
            t = (start + xi) % 24

            if 9 <= t < 18:
                candidate += wi

        ans = max(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
