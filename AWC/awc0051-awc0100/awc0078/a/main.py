# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    r = list(map(int, input().split()))
    ans = 0

    for _ in range(m):
        fi, si = map(int, input().split())
        fi -= 1

        if r[fi] >= si:
            r[fi] -= si
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
