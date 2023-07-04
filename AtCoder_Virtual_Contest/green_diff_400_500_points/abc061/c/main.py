# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, k = map(int, input().split())
    d = defaultdict(int)

    for _ in range(n):
        ai, bi = map(int, input().split())
        d[ai] += bi

    for key in sorted(d.keys()):
        k -= min(k, d[key])

        if k == 0:
            print(key)
            exit()


if __name__ == "__main__":
    main()
