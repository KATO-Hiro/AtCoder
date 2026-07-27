# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    d = list(map(int, input().split()))
    d_max = max(d)
    ans = 0

    for _ in range(m):
        _, hi = map(str, input().split())
        hi = int(hi)

        if hi <= d_max:
            continue

        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
