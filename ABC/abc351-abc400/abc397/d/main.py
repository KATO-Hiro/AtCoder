# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    def f(a, b):
        return a * a * a - b * b * b

    for d in range(1, 10**6 + 1):
        ok, ng = 1, int(1e9)

        while (ng - ok) > 1:
            wj = (ok + ng) // 2

            if f(wj + d, wj) <= n:
                ok = wj
            else:
                ng = wj

        if f(ok + d, ok) == n:
            print(ok + d, ok)
            exit()

    print(-1)


if __name__ == "__main__":
    main()
