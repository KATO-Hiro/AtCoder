# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    s = [0] + list(map(int, input().split()))
    c = [0] + list(map(int, input().split()))
    inf = 10**18

    for _ in range(q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            l, r, v = query[1:]

            for i in range(l, r + 1):
                if c[i] == inf:
                    continue

                c[i] += v
        elif query[0] == 2:
            x = query[1]
            c[x] = inf
        else:
            l, r = query[1:]
            ans = 0

            for i in range(l, r + 1):
                if c[i] == inf or c[i] > 0:
                    continue

                ans += s[i]

            print(ans)


if __name__ == "__main__":
    main()
