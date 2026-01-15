# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    ab = []

    for i in range(n):
        ai, bi = map(int, input().split())
        ab.append((ai, bi, i + 1))

    ab.sort()
    ans = []

    for i in range(n - 1):
        ai, bi, id = ab[i]
        aj, _, _ = ab[i + 1]

        if (aj - ai) < bi * k:
            ans.append(id)

    ans.sort()
    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()
