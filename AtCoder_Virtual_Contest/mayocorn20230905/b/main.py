# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    edges = set()

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
        edges.add((ai, bi))

    ans = 0
    # print(edges)

    for a in range(n):
        for b in range(n):
            for c in range(n):
                count = 0

                if (a, b) in edges:
                    count += 1
                if (b, c) in edges:
                    count += 1
                if (a, c) in edges:
                    count += 1

                if count == 3:
                    # print(a, b, c)
                    ans += 1

    print(ans)


if __name__ == "__main__":
    main()
