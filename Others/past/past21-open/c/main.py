# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    ans = []

    for _ in range(n):
        si, ti = map(int, input().split())
        p, q = divmod(si, k)
        ti = min(ti, si + (k - q))
        ans.append(ti - si)

    print(*ans)


if __name__ == "__main__":
    main()
