# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    p = [[] for _ in range(n)]

    for i in range(m):
        ai, bi = map(int, input().split())

        ai -= 1
        bi -= 1

        p[ai].append(h[bi])
        p[bi].append(h[ai])

    ans = 0

    for index, pi in enumerate(p):
        p_count = len(pi)

        if p_count == 0:
            ans += 1
            continue

        pmax = max(pi)

        if h[index] > pmax:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
